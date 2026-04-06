$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" | Where-Object { $_.Name -ne "workforce_temp.html" }
$externalRefs = @{}
$localRefs = @{}
$videoRefs = @{}

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw
    
    # Find all img src attributes
    $imgMatches = [regex]::Matches($content, 'src="([^"]+\.(png|jpg|jpeg|gif|svg|webp))"')
    foreach ($match in $imgMatches) {
        $src = $match.Groups[1].Value
        if ($src -match '^https?://') {
            $externalRefs[$src] = $true
        } else {
            $localRefs[$src] = $true
        }
    }
    
    # Find all video src attributes
    $videoMatches = [regex]::Matches($content, 'src="([^"]+\.(mp4|webm|ogg))"')
    foreach ($match in $videoMatches) {
        $src = $match.Groups[1].Value
        $videoRefs[$src] = $true
    }
}

Write-Host "=== EXTERNAL IMAGE REFERENCES ==="
$externalRefs.Keys | Sort-Object | ForEach-Object { Write-Host $_ }
Write-Host ""
Write-Host "=== LOCAL IMAGE REFERENCES ==="
$localRefs.Keys | Sort-Object | ForEach-Object { Write-Host $_ }
Write-Host ""
Write-Host "=== VIDEO REFERENCES ==="
$videoRefs.Keys | Sort-Object | ForEach-Object { Write-Host $_ }
