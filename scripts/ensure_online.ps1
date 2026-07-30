# Keep Equity Research Agent online (local web UI). Cloudflare tunnel is optional.
#
# Never kills a process that is already listening / tracked as the app.
# Only starts uvicorn when nothing is running on the port.
#
# Usage:
#   .\scripts\ensure_online.ps1
#   .\scripts\ensure_online.ps1 -SkipTunnel
#   .\scripts\ensure_online.ps1 -NotifyAlways
#   .\scripts\ensure_online.ps1 -ForceRestart   # explicit recycle only
#
# Schedule: .\scripts\install_ensure_online.ps1

param(
  [switch]$NotifyAlways,
  [switch]$SkipTunnel,
  [switch]$ForceRestart
)

$ErrorActionPreference = "Continue"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$LogDir = Join-Path $Root "data"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$WatchLog = Join-Path $LogDir "ensure_online.log"
$PidFile = Join-Path $LogDir "app.pid"
$UrlFile = Join-Path $LogDir "tunnel_url.txt"
$NotifiedFile = Join-Path $LogDir "tunnel_url_notified.txt"
$ServerOut = Join-Path $LogDir "app.out.log"
$ServerErr = Join-Path $LogDir "app.err.log"

function Write-EnsureLog([string]$Message) {
  $line = "{0} {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
  Add-Content -Path $WatchLog -Value $line -Encoding UTF8
  Write-Host $line
}

function Import-DotEnv {
  $envPath = Join-Path $Root ".env"
  if (-not (Test-Path $envPath)) { return }
  Get-Content $envPath | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) { return }
    $eq = $line.IndexOf("=")
    if ($eq -lt 1) { return }
    $key = $line.Substring(0, $eq).Trim()
    $val = $line.Substring($eq + 1).Trim()
    if ($val.StartsWith('"') -and $val.EndsWith('"')) { $val = $val.Substring(1, $val.Length - 2) }
    if ($val.StartsWith("'") -and $val.EndsWith("'")) { $val = $val.Substring(1, $val.Length - 2) }
    if (-not [string]::IsNullOrWhiteSpace($key)) {
      Set-Item -Path "Env:$key" -Value $val
    }
  }
}

function Test-AppHealthy([int]$Port, [int]$TimeoutSec = 8) {
  try {
    $r = Invoke-WebRequest -Uri "http://127.0.0.1:${Port}/health" -UseBasicParsing -TimeoutSec $TimeoutSec
    return ($r.StatusCode -ge 200 -and $r.StatusCode -lt 300)
  } catch {
    return $false
  }
}

function Test-AppHealthyRetry([int]$Port, [int]$Attempts = 3, [int]$DelaySec = 2) {
  for ($i = 1; $i -le $Attempts; $i++) {
    if (Test-AppHealthy $Port) { return $true }
    if ($i -lt $Attempts) {
      Write-EnsureLog "Health check miss $i/$Attempts - retrying in ${DelaySec}s (will not kill app)"
      Start-Sleep -Seconds $DelaySec
    }
  }
  return $false
}

function Get-PortListenerPids([int]$Port) {
  $pids = @()
  try {
    $conns = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    foreach ($c in $conns) {
      if ($c.OwningProcess -and ($pids -notcontains $c.OwningProcess)) {
        $pids += $c.OwningProcess
      }
    }
  } catch { }
  return $pids
}

function Get-TrackedAppPid {
  if (-not (Test-Path $PidFile)) { return $null }
  $raw = (Get-Content $PidFile -Raw).Trim()
  if (-not $raw) { return $null }
  $proc = Get-Process -Id $raw -ErrorAction SilentlyContinue
  if ($proc) { return [int]$raw }
  return $null
}

function Set-TrackedAppPid([int]$ProcessId) {
  $ProcessId | Set-Content -Path $PidFile -Encoding ascii
}

function Test-AppProcessAlive([int]$Port) {
  $tracked = Get-TrackedAppPid
  if ($tracked) { return $true }
  $listeners = Get-PortListenerPids $Port
  return ($listeners.Count -gt 0)
}

function Sync-PidFileFromListener([int]$Port) {
  $listeners = Get-PortListenerPids $Port
  if ($listeners.Count -gt 0) {
    $listenPid = [int]$listeners[0]
    $tracked = Get-TrackedAppPid
    if ($tracked -ne $listenPid) {
      Set-TrackedAppPid $listenPid
      if ($tracked) {
        Write-EnsureLog "Updated app.pid $tracked → $listenPid (actual port listener)"
      } else {
        Write-EnsureLog "Adopted existing listener pid $listenPid into app.pid"
      }
    }
    return $listenPid
  }
  return (Get-TrackedAppPid)
}

function Stop-AppServer([int]$Port, [string]$Reason) {
  Write-EnsureLog "ForceRestart: stopping app ($Reason)"
  $tracked = Get-TrackedAppPid
  if ($tracked) {
    Stop-Process -Id $tracked -Force -ErrorAction SilentlyContinue
  }
  foreach ($lp in (Get-PortListenerPids $Port)) {
    Stop-Process -Id $lp -Force -ErrorAction SilentlyContinue
  }
  Remove-Item -Force -ErrorAction SilentlyContinue $PidFile
  Start-Sleep -Seconds 1
}

function Start-AppServer([int]$Port) {
  $py = Join-Path $Root ".venv\Scripts\python.exe"
  if (-not (Test-Path $py)) {
    Write-EnsureLog "ERROR: venv missing - run .\scripts\start_local.ps1 once first"
    return $false
  }

  # Safety: never start (or kill) if something is already bound / tracked.
  if (Test-AppProcessAlive $Port) {
    Sync-PidFileFromListener $Port | Out-Null
    if (Test-AppHealthyRetry $Port 2 2) {
      Write-EnsureLog "App already running - left untouched"
      return $true
    }
    Write-EnsureLog "WARN: app process is alive but /health failing - NOT killing it (pass -ForceRestart to recycle)"
    return $true
  }

  # Clean stale pid file only when the process is gone
  if (Test-Path $PidFile) {
    $old = (Get-Content $PidFile -Raw).Trim()
    if ($old -and -not (Get-Process -Id $old -ErrorAction SilentlyContinue)) {
      Remove-Item -Force -ErrorAction SilentlyContinue $PidFile
      Write-EnsureLog "Removed stale pid file (process $old not running)"
    }
  }

  # Do not truncate live logs if somehow a listener appeared
  if ((Get-PortListenerPids $Port).Count -gt 0) {
    Write-EnsureLog "WARN: port $Port became busy before start - aborting start, leaving existing process"
    Sync-PidFileFromListener $Port | Out-Null
    return $true
  }

  Remove-Item -Force -ErrorAction SilentlyContinue $ServerOut, $ServerErr
  Write-EnsureLog "Starting Equity Research Agent on port $Port (background)"

  $proc = Start-Process -FilePath $py `
    -ArgumentList @(
      "-m", "uvicorn", "app.api:app",
      "--host", "0.0.0.0",
      "--port", "$Port"
    ) `
    -WorkingDirectory $Root `
    -RedirectStandardOutput $ServerOut `
    -RedirectStandardError $ServerErr `
    -WindowStyle Hidden `
    -PassThru

  Set-TrackedAppPid $proc.Id

  for ($i = 0; $i -lt 40; $i++) {
    Start-Sleep -Milliseconds 500
    if (Test-AppHealthy $Port) {
      Write-EnsureLog "App healthy (pid $($proc.Id))"
      return $true
    }
    if (-not (Get-Process -Id $proc.Id -ErrorAction SilentlyContinue)) {
      Write-EnsureLog "ERROR: app exited early - see data\app.err.log"
      return $false
    }
  }
  Write-EnsureLog "ERROR: app did not become healthy in time"
  return $false
}

function Send-Ntfy([string]$Url) {
  $topic = $env:NTFY_TOPIC
  if ([string]::IsNullOrWhiteSpace($topic)) {
    Write-EnsureLog "SKIP notify: set NTFY_TOPIC in .env (see CLOUDFLARE_TUNNEL.md)"
    return
  }

  $server = $env:NTFY_SERVER
  if ([string]::IsNullOrWhiteSpace($server)) { $server = "https://ntfy.sh" }
  $server = $server.TrimEnd("/")
  $endpoint = "$server/$topic"

  $headers = @{
    Title = "Equity Research remote URL"
    Click = $Url
    Priority = "default"
    Tags = "mag,link"
  }
  if (-not [string]::IsNullOrWhiteSpace($env:NTFY_TOKEN)) {
    $headers["Authorization"] = "Bearer $($env:NTFY_TOKEN)"
  }

  $body = "Open Equity Research Agent:`n$Url`n`n(Works from cellular or any Wi-Fi - laptop must stay on.)"
  try {
    Invoke-RestMethod -Method Post -Uri $endpoint -Body $body -Headers $headers -ContentType "text/plain; charset=utf-8" | Out-Null
    Write-EnsureLog "ntfy sent to topic (server $server)"
    $Url | Set-Content -Path $NotifiedFile -Encoding ascii
  } catch {
    Write-EnsureLog ("ERROR ntfy: {0}" -f $_.Exception.Message)
  }
}

Import-DotEnv

# Prefer SkipTunnel from switch, else .env ENSURE_SKIP_TUNNEL=1|true|yes
if (-not $SkipTunnel) {
  $skipEnv = ($env:ENSURE_SKIP_TUNNEL -as [string])
  if ($skipEnv -match '^(1|true|yes)$') { $SkipTunnel = $true }
}

# Project default is 8000; ignore a foreign PORT left in the shell (e.g. PodSnip 8787)
# unless this repo's .env explicitly set PORT during Import-DotEnv.
$port = 8000
$envFile = Join-Path $Root ".env"
if (Test-Path $envFile) {
  $portLine = Get-Content $envFile | Where-Object { $_ -match '^\s*PORT\s*=' } | Select-Object -First 1
  if ($portLine -and ($portLine -match '^\s*PORT\s*=\s*(\d+)')) {
    $port = [int]$Matches[1]
  }
}

Write-EnsureLog "ensure_online check (port $port; skip_tunnel=$SkipTunnel; force_restart=$ForceRestart)"

$appOk = $false

if ($ForceRestart) {
  Stop-AppServer $port "explicit -ForceRestart"
  if (Start-AppServer $port) { $appOk = $true }
  else {
    Write-EnsureLog "ABORT: could not start app after ForceRestart"
    exit 1
  }
}
elseif (Test-AppHealthyRetry $port 3 2) {
  Sync-PidFileFromListener $port | Out-Null
  Write-EnsureLog "App OK - leaving running process alone"
  $appOk = $true
}
elseif (Test-AppProcessAlive $port) {
  # Process exists; health flaky or busy (e.g. long Ollama work). Do not kill.
  Sync-PidFileFromListener $port | Out-Null
  $alivePid = Get-TrackedAppPid
  Write-EnsureLog "WARN: process alive (pid $alivePid) but /health not OK - NOT restarting (use -ForceRestart if needed)"
  $appOk = $true
}
else {
  Write-EnsureLog "App down (no process on port) - starting"
  if (Start-AppServer $port) { $appOk = $true }
  else {
    Write-EnsureLog "ABORT: could not start app"
    exit 1
  }
}

if ($SkipTunnel) {
  Write-EnsureLog "Tunnel skipped (app keep-alive only). Local UI: http://127.0.0.1:${port}"
  exit 0
}

# Tunnel is best-effort: never fail the job if the local app is healthy.
if ((Test-TunnelAlive) -and (Test-Path $UrlFile)) {
  Write-EnsureLog ("Tunnel OK: {0}" -f (Get-Content $UrlFile -Raw).Trim())
} else {
  Write-EnsureLog "Tunnel down or missing URL - starting (best-effort)"
  & "$Root\scripts\run_tunnel.ps1"
  if ($LASTEXITCODE -ne 0) {
    Write-EnsureLog "WARN: tunnel failed (exit $LASTEXITCODE) - local app remains up at http://127.0.0.1:${port}"
    if ($appOk) { exit 0 }
    exit 1
  }
}

if (-not (Test-Path $UrlFile)) {
  Write-EnsureLog "WARN: no tunnel URL file yet - local app remains up"
  exit 0
}

$url = (Get-Content $UrlFile -Raw).Trim()
if (-not $url) {
  Write-EnsureLog "WARN: empty tunnel URL - local app remains up"
  exit 0
}

$prev = ""
if (Test-Path $NotifiedFile) {
  $prev = (Get-Content $NotifiedFile -Raw).Trim()
}

if ($NotifyAlways -or ($url -ne $prev)) {
  Write-EnsureLog "URL new or NotifyAlways - notifying"
  Send-Ntfy $url
} else {
  Write-EnsureLog "URL unchanged - no push"
}

exit 0
