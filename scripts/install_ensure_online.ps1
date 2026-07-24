# Install keep-alive: start Equity Research Agent at logon and re-check every N minutes.
# Cloudflare tunnel is optional (set ENSURE_SKIP_TUNNEL=1 in .env while tunnel is flaky).
#
# Usage:
#   .\scripts\install_ensure_online.ps1
#   .\scripts\install_ensure_online.ps1 -Minutes 15
#   .\scripts\install_ensure_online.ps1 -Uninstall

param(
  [int]$Minutes = 15,
  [switch]$Uninstall
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$TaskName = "EquityResearch Ensure Online"
$WatchScript = Join-Path $Root "scripts\ensure_online.ps1"

if ($Uninstall) {
  Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
  Write-Host "Removed scheduled task: $TaskName"
  exit 0
}

if (-not (Test-Path $WatchScript)) {
  Write-Host "Missing $WatchScript"
  exit 1
}
if ($Minutes -lt 2) {
  Write-Host "Minutes must be >= 2"
  exit 1
}

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

$arg = "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$WatchScript`" -SkipTunnel"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $arg -WorkingDirectory $Root

$start = (Get-Date).AddMinutes(1)
$repeat = New-ScheduledTaskTrigger -Once -At $start `
  -RepetitionInterval (New-TimeSpan -Minutes $Minutes) `
  -RepetitionDuration (New-TimeSpan -Days 3650)

$atLogon = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME

$settings = New-ScheduledTaskSettingsSet `
  -AllowStartIfOnBatteries `
  -DontStopIfGoingOnBatteries `
  -StartWhenAvailable `
  -MultipleInstances IgnoreNew `
  -ExecutionTimeLimit (New-TimeSpan -Minutes 15) `
  -WakeToRun:$false

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
  -TaskName $TaskName `
  -Action $action `
  -Trigger @($atLogon, $repeat) `
  -Settings $settings `
  -Principal $principal `
  -Description "Equity Research Agent: keep web UI up at logon + every ${Minutes}m (tunnel optional). Log: data\ensure_online.log" `
  | Out-Null

Write-Host "Installed scheduled task: $TaskName"
Write-Host "  At logon + every $Minutes minutes while logged in."
Write-Host "  Keep-alive only (tunnel skipped). Cursor/IDE does NOT need to be open."
Write-Host "  Log: $Root\data\ensure_online.log"
Write-Host "  Local UI: http://127.0.0.1:8000"
Write-Host ""
Write-Host "Checklist:"
Write-Host "  - Power: never sleep when plugged in (Settings -> System -> Power)"
Write-Host "  - Test now:  .\scripts\ensure_online.ps1 -SkipTunnel"
Write-Host "Remove later:"
Write-Host "  .\scripts\install_ensure_online.ps1 -Uninstall"
