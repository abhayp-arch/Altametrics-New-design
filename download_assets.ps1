# Verify all local asset references actually exist in the assets folder
$localRefs = @(
    "assets/altametrics-dashboard-light.png",
    "assets/ap_automation_mockup_v1_1774608102475.png",
    "assets/enterprise_financial_summary_v1_1774608121305.png",
    "assets/famous_daves_story.png",
    "assets/inventory_cogs_analytics_mockup_v2_1774438423534.png",
    "assets/inventory_invoice_ocr_mockup_v3_retry_1774437480462.png",
    "assets/inventory_mobile_counting_mockup_v2_retry_1774437455466.png",
    "assets/inventory_prep_forecasting_mockup_v2_retry_1774437532523.png",
    "assets/inventory_recipe_costing_mockup_v3_retry_1774437500125.png",
    "assets/inventory_supply_chain_automation_mockup_v2_1774438441071.png",
    "assets/mooyah_story.png",
    "assets/nadia_lynn_headshot_1774440753442.png",
    "assets/peets_coffee_lifestyle_success_story_1774440734280.png",
    "assets/reporting_custom_builder_1774537985972.png",
    "assets/reporting_daily_activity_1774537945391.png",
    "assets/reporting_hero_dashboard_1774537901842.png",
    "assets/reporting_loss_prevention_1774537968323.png",
    "assets/reporting_multiunit_scorecard_1774538003560.png",
    "assets/reporting_realtime_insights_1774537921224.png",
    "assets/workforce_ai_forecasting_dashboard_v2_1774435088598.png",
    "assets/workforce_compliance_alerts_mockup_1774435067858.png",
    "assets/workforce_enterprise_heatmap_1774434945580.png",
    "assets/workforce_mobile_app_redesign_1774434898056.png",
    "assets/workforce_plumclock_mockup_1774435793224.png",
    "assets/12246591_1920_1080_30fps.mp4"
)

Write-Host "=== LOCAL ASSET EXISTS CHECK ==="
$missing = @()
foreach ($ref in $localRefs) {
    if (Test-Path $ref) {
        Write-Host "[OK]     $ref"
    } else {
        Write-Host "[MISSING] $ref"
        $missing += $ref
    }
}

Write-Host ""
Write-Host "=== EXTERNAL IMAGES (need to download) ==="
$externalImages = @(
    "https://altametrics.com/assets/images/pages/Buffalo-180-31da30fa2.webp",
    "https://altametrics.com/assets/images/pages/Chipotle-180-d39d5b0f0.webp",
    "https://altametrics.com/assets/images/pages/Jamba-bg-180-34687ebfe.webp",
    "https://altametrics.com/assets/images/pages/Noodles-180-fa0c39df2.webp",
    "https://altametrics.com/assets/images/pages/Peets-180-c3ab70114.webp",
    "https://altametrics.com/assets/images/pages/Pizza-bg-180-5dc7b1bfa.webp",
    "https://altametrics.com/assets/images/pages/Taco-Bell-bg-180-8e2d707da.webp",
    "https://altametrics.com/assets/images/pages/Tokyo-bg-180-c5e968a47.webp"
)

foreach ($url in $externalImages) {
    $filename = [System.IO.Path]::GetFileName($url)
    Write-Host "Downloading: $filename"
    try {
        Invoke-WebRequest -Uri $url -OutFile "assets/$filename" -TimeoutSec 15 -ErrorAction Stop
        Write-Host "  -> Saved to assets/$filename"
    } catch {
        Write-Warning "  -> FAILED: $_"
    }
}
