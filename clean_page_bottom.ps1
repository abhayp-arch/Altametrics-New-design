$htmlFiles = Get-ChildItem -Filter *.html

foreach ($file in $htmlFiles) {
    Write-Host "Cleaning up bottom of page in $($file.Name)"
    $content = Get-Content $file.FullName -Raw
    
    # 1. Remove the Information Modal block
    # Note: Use a very broad regex to ensure we catch anything that looks like the modal
    $content = $content -replace '(?s)<!-- Learn More Modal -->\s*<div id="info-modal" class="modal-overlay">.*?</div>', ""
    # In case the comment is missing or different
    $content = $content -replace '(?s)<div id="info-modal" class="modal-overlay">.*?</div>', ""
    
    # 2. Remove the Chatbot Widget block
    $content = $content -replace '(?s)<!-- Chatbot Widget -->\s*<div class="chatbot-widget">.*?</div>', ""
    # In case the comment is missing or different
    $content = $content -replace '(?s)<div class="chatbot-widget">.*?</div>', ""
    
    $content | Set-Content $file.FullName
}
