# Update all HTML files to replace external altametrics.com image references with local paths
$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" | Where-Object { $_.Name -ne "workforce_temp.html" }

$replacements = @{
    "https://altametrics.com/assets/images/pages/Buffalo-180-31da30fa2.webp"    = "assets/Buffalo-180-31da30fa2.webp"
    "https://altametrics.com/assets/images/pages/Chipotle-180-d39d5b0f0.webp"  = "assets/Chipotle-180-d39d5b0f0.webp"
    "https://altametrics.com/assets/images/pages/Jamba-bg-180-34687ebfe.webp"  = "assets/Jamba-bg-180-34687ebfe.webp"
    "https://altametrics.com/assets/images/pages/Noodles-180-fa0c39df2.webp"   = "assets/Noodles-180-fa0c39df2.webp"
    "https://altametrics.com/assets/images/pages/Peets-180-c3ab70114.webp"     = "assets/Peets-180-c3ab70114.webp"
    "https://altametrics.com/assets/images/pages/Pizza-bg-180-5dc7b1bfa.webp"  = "assets/Pizza-bg-180-5dc7b1bfa.webp"
    "https://altametrics.com/assets/images/pages/Taco-Bell-bg-180-8e2d707da.webp" = "assets/Taco-Bell-bg-180-8e2d707da.webp"
    "https://altametrics.com/assets/images/pages/Tokyo-bg-180-c5e968a47.webp"  = "assets/Tokyo-bg-180-c5e968a47.webp"
}

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw
    $changed = $false
    
    foreach ($key in $replacements.Keys) {
        if ($content -match [regex]::Escape($key)) {
            $content = $content.Replace($key, $replacements[$key])
            $changed = $true
            Write-Host "[$($file.Name)] Replaced: $key -> $($replacements[$key])"
        }
    }
    
    if ($changed) {
        $content | Set-Content $file.FullName
        Write-Host "  -> Saved $($file.Name)"
    }
}

Write-Host ""
Write-Host "=== DONE: All external image references updated to local paths ==="
