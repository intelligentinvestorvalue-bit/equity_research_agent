<#
  Start the equity research web app for PC + same-Wi-Fi iPhone/iPad.
  Usage:  .\scripts\start_local.ps1
#>
$ErrorActionPreference = "Stop"
Set-Location (Split-Path $PSScriptRoot -Parent)

if (-not (Test-Path ".venv\Scripts\python.exe")) {
  Write-Host "Creating venv..."
  py -3.11 -m venv .venv
  if ($LASTEXITCODE -ne 0) { py -3 -m venv .venv }
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\pip.exe install -r requirements.txt

# LAN IP hint
$ip = (Get-NetIPAddress -AddressFamily IPv4 |
  Where-Object { $_.IPAddress -notlike "127.*" -and $_.PrefixOrigin -ne "WellKnown" } |
  Select-Object -First 1 -ExpandProperty IPAddress)
if (-not $ip) { $ip = "YOUR_LAN_IP" }

Write-Host ""
Write-Host "Ollama should be running locally (llama3 pulled)."
Write-Host "On this PC:    http://127.0.0.1:8000"
Write-Host "On iPhone/iPad (same Wi-Fi): http://${ip}:8000"
Write-Host "Allow Windows Firewall inbound TCP 8000 if the phone cannot connect."
Write-Host ""

& .\.venv\Scripts\python.exe -m uvicorn app.api:app --host 0.0.0.0 --port 8000
