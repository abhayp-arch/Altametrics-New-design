$gsapScripts = "    <!-- GSAP & ScrollTrigger -->`n    <script src=`"https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js`"></script>`n    <script src=`"https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js`"></script>`n    <script src=`"script.js`"></script>"

$files = Get-ChildItem *.html -Exclude "workforce_temp.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    if ($content -match '<script src="script.js"></script>' -and $content -notmatch 'gsap\.min\.js') {
        Write-Host "Injecting GSAP into $($file.Name)..."
        # Using [regex]::Replace to handle potential variations in spacing better, but sticking to standard exact match for now
        $newContent = $content -replace '<script src="script.js"></script>', $gsapScripts
        $newContent | Set-Content $file.FullName -NoNewline
    }
}
