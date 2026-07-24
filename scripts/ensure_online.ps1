# Keep Equity Research Agent online (local web UI). Cloudflare tunnel is optional.
#
# Usage:
#   .\scripts\ensure_online.ps1
#   .\scripts\ensure_online.ps1 -SkipTunnel          # app keep-alive only (recommended while tunnel is flaky)
#   .\scripts\ensure_online.ps1 -NotifyAlways
#
# Schedule: .\scripts\install_ensure_online.ps1

param(
  [switch]$NotifyAlways,
  [switch]$SkipTunnel
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

function Test-AppHealthy([int]$Port) {
  try {
    $r = Invoke-WebRequest -Uri "http://127.0.0.1:${Port}/health" -UseBasicParsing -TimeoutSec 4
    return ($r.StatusCode -ge 200 -and $r.StatusCode -lt 300)
  } catch {
    return $false
  }
}

function Test-TunnelAlive {
  $tunnelPidFile = Join-Path $LogDir "tunnel.pid"
  if (-not (Test-Path $tunnelPidFile)) { return $false }
  $tid = (Get-Content $tunnelPidFile -Raw).Trim()
  if (-not $tid) { return $false }
  return [bool](Get-Process -Id $tid -ErrorAction SilentlyContinue)
}

function Start-AppServer([int]$Port) {
  $py = Join-Path $Root ".venv\Scripts\python.exe"
  if (-not (Test-Path $py)) {
    Write-EnsureLog "ERROR: venv missing - run .\scripts\start_local.ps1 once first"
    return $false
  }

  if (Test-Path $PidFile) {
    $old = (Get-Content $PidFile -Raw).Trim()
    $op = Get-Process -Id $old -ErrorAction SilentlyContinue
    if ($op) {
      Write-EnsureLog "Stopping stale app pid $old"
      Stop-Process -Id $old -Force -ErrorAction SilentlyContinue
      Start-Sleep -Seconds 1
    }
    Remove-Item -Force -ErrorAction SilentlyContinue $PidFile
  }

  # Also free anything else listening on the port (orphan uvicorn)
  try {
    $listeners = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    foreach ($c in $listeners) {
      Write-EnsureLog "Stopping orphan listener pid $($c.OwningProcess) on port $Port"
      Stop-Process -Id $c.OwningProcess -Force -ErrorAction SilentlyContinue
    }
    if ($listeners) { Start-Sleep -Seconds 1 }
  } catch { }

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

  $proc.Id | Set-Content -Path $PidFile -Encoding ascii

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

Write-EnsureLog "ensure_online check (port $port; skip_tunnel=$SkipTunnel)"

$appOk = $false
if (Test-AppHealthy $port) {
  Write-EnsureLog "App OK"
  $appOk = $true
} else {
  Write-EnsureLog "App down - starting"
  if (Start-AppServer $port) {
    $appOk = $true
  } else {
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
