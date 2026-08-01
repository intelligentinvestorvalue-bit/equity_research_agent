# Install Task Scheduler job: auto-push data/sync + rebuild GitHub Pages.
# Runs at logon and every N minutes. Research completion sets data/publish_requested;
# this task picks it up so you do not need to commit manually.
#
# Usage:
#   .\scripts\install_publish_sync.ps1
#   .\scripts\install_publish_sync.ps1 -Minutes 10
#   .\scripts\install_publish_sync.ps1 -Uninstall

param(
  [int]$Minutes = 10,
  [switch]$Uninstall
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$TaskName = "EquityResearch Publish Sync"
$Script = Join-Path $Root "scripts\publish_sync.ps1"

if ($Uninstall) {
  Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
  Write-Host "Removed scheduled task: $TaskName"
  exit 0
}

if (-not (Test-Path $Script)) {
  Write-Host "Missing $Script"
  exit 1
}
if ($Minutes -lt 2) {
  Write-Host "Minutes must be >= 2"
  exit 1
}

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

$arg = "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$Script`""
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
  -ExecutionTimeLimit (New-TimeSpan -Minutes 30) `
  -WakeToRun:$false

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
  -TaskName $TaskName `
  -Action $action `
  -Trigger @($atLogon, $repeat) `
  -Settings $settings `
  -Principal $principal `
  -Description "Equity Research: rebuild docs/ + git push data/sync after research (flag: data\publish_requested). Log: data\publish_sync.log" `
  | Out-Null

Write-Host "Installed scheduled task: $TaskName"
Write-Host "  At logon + every $Minutes minutes while logged in."
Write-Host "  After each completed research job, the app sets data\publish_requested;"
Write-Host "  this task rebuilds GitHub Pages and pushes — no manual git steps."
Write-Host "  Log: $Root\data\publish_sync.log"
Write-Host ""
Write-Host "Checklist:"
Write-Host "  1. Stay on branch main (Pages source)"
Write-Host "  2. git push works without a password prompt (Git Credential Manager / gh auth login)"
Write-Host "  3. pip install markdown  (or use .venv with requirements.txt)"
Write-Host "  4. Test now:  .\scripts\publish_sync.ps1 -Force"
Write-Host "Remove later:"
Write-Host "  .\scripts\install_publish_sync.ps1 -Uninstall"
