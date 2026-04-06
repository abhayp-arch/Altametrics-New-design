$chatbotHtml = @"

    <!-- Chatbot Widget -->
    <div class="chatbot-widget">
        <div class="chat-popup" style="display: none;">
            <button class="chat-close" onclick="document.querySelector('.chat-popup').style.display='none'">&times;</button>
            <div class="chat-avatar">
                <img src="https://api.dicebear.com/7.x/bottts/svg?seed=Felix&backgroundColor=e6f0fa" alt="AI Bot">
            </div>
            <div class="chat-message">
                Want to chat about Altametrics products? I'm an AI bot that's here to help! 🤩
            </div>
        </div>
        <button class="chat-toggle-btn" onclick="const p=document.querySelector('.chat-popup'); p.style.display=(p.style.display==='none'?'block':'none')">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM20 16H5.17L4 17.17V4H20V16Z" fill="white" />
            </svg>
        </button>
    </div>

"@

$htmlFiles = Get-ChildItem -Filter *.html | Where-Object { $_.Name -ne "workforce_temp.html" }

foreach ($file in $htmlFiles) {
    Write-Host "Restoring chatbot and cleaning modal in $($file.Name)"
    $content = Get-Content $file.FullName -Raw
    
    # 1. Broadly target the mangled section between </footer> and <script src="script.js"></script>
    # This regex is greedy to ensure we consume all orphaned </div> tags and other fragments
    if ($content -match '(?s)</footer>(.*?)<script src="script.js"></script>') {
        $foundSection = $matches[1]
        # We replace the captured middle section with our clean chatbot HTML
        $content = $content.Replace($foundSection, $chatbotHtml)
    } else {
        # Fallback if the regex fails: append it before the closing </body> tag
        # and hope the previous cleanup already cleared most of it
        Write-Warning "Could not find standard footer/script section in $($file.Name). Appending before </body> instead."
        $content = $content -replace '</body>', "$chatbotHtml`n</body>"
    }
    
    $content | Set-Content $file.FullName
}
