import os

PAGES = [
    "ai-forecasting", "compliance", "mobile-app", "payroll",
    "waste-reduction", "purchasing", "recipe-costing", "prep-planning",
    "digital-haccp", "field-audits", "food-safety", "task-mgmt",
    "real-time-sales", "bi-analytics", "loss-prevention", "ai-insights",
    "invoice-automation", "general-ledger", "bank-recon", "inventory-sync"
]

FILES_TO_UPDATE = [
    "index.html", "workforce-scheduling.html", "inventory.html", 
    "checklist.html", "reporting.html", "accounting.html", 
    "pricing.html", "integrations.html", "resources.html"
]

def update_files():
    for filename in FILES_TO_UPDATE:
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        for slug in PAGES:
            content = content.replace(f'href="workforce-scheduling.html#{slug}"', f'href="{slug}.html"')
            content = content.replace(f'href="inventory.html#{slug}"', f'href="{slug}.html"')
            content = content.replace(f'href="checklist.html#{slug}"', f'href="{slug}.html"')
            content = content.replace(f'href="reporting.html#{slug}"', f'href="{slug}.html"')
            content = content.replace(f'href="accounting.html#{slug}"', f'href="{slug}.html"')
            
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated links in {filename}")

if __name__ == "__main__":
    update_files()
