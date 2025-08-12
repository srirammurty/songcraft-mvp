# run from parent folder that contains 'indian-music-starter' folder
Param(
  [string]$Folder = "indian-music-starter",
  [string]$Out = "indian-music-starter.zip"
)
if(!(Test-Path $Folder)){ Write-Error "Folder $Folder not found"; exit 1 }
if(Test-Path $Out){ Remove-Item $Out }
Compress-Archive -Path "$Folder\*" -DestinationPath $Out
Write-Host "Created $Out"
