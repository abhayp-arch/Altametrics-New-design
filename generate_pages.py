import json
import os

PAGES = {
    # WORKFORCE SUITE
    "ai-forecasting": {"title": "AI Demand Forecasting", "cat": "Workforce Suite", "icon": "👥", "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71"},
    "compliance": {"title": "Labor Law Compliance", "cat": "Workforce Suite", "icon": "⚖️", "image": "https://images.unsplash.com/photo-1573164713988-8665fc963095"},
    "mobile-app": {"title": "Employee Mobile App", "cat": "Workforce Suite", "icon": "📱", "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c"},
    "payroll": {"title": "Payroll & Tip Distribution", "cat": "Workforce Suite", "icon": "💸", "image": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c"},
    
    # INVENTORY SUITE
    "waste-reduction": {"title": "Food Waste Reduction", "cat": "Inventory Suite", "icon": "♻️", "image": "https://images.unsplash.com/photo-1556910103-1c02745aae4d"},
    "purchasing": {"title": "Automated Purchasing", "cat": "Inventory Suite", "icon": "🛒", "image": "https://images.unsplash.com/photo-1586880244406-556ebe35f282"},
    "recipe-costing": {"title": "Dynamic Recipe Costing", "cat": "Inventory Suite", "icon": "🍲", "image": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1"},
    "prep-planning": {"title": "Smart Prep Planning", "cat": "Inventory Suite", "icon": "🔪", "image": "https://images.unsplash.com/photo-1507048331197-7d4ac70811cf"},

    # CHECKLIST SUITE
    "digital-haccp": {"title": "Digital HACCP Logs", "cat": "Operations Suite", "icon": "🌡️", "image": "https://images.unsplash.com/photo-1581244277943-fe4a9c777189"},
    "field-audits": {"title": "Mobile Field Audits", "cat": "Operations Suite", "icon": "📋", "image": "https://images.unsplash.com/photo-1515238152791-8216bfdf89a7"},
    "food-safety": {"title": "Food Safety Compliance", "cat": "Operations Suite", "icon": "🛡️", "image": "https://images.unsplash.com/photo-1514933651103-005eec06c04b"},
    "task-mgmt": {"title": "Shift Task Management", "cat": "Operations Suite", "icon": "✅", "image": "https://images.unsplash.com/photo-1484480974693-6ca0a78cb36c"},

    # REPORTING SUITE
    "real-time-sales": {"title": "Real-Time Sales Dashboards", "cat": "Reporting Suite", "icon": "📈", "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f"},
    "bi-analytics": {"title": "Enterprise BI Analytics", "cat": "Reporting Suite", "icon": "📊", "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71"},
    "loss-prevention": {"title": "AI Loss Prevention", "cat": "Reporting Suite", "icon": "🕵️", "image": "https://images.unsplash.com/photo-1581568461706-e82208ebd941"},
    "ai-insights": {"title": "Predictive AI Insights", "cat": "Reporting Suite", "icon": "🧠", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475"},

    # ACCOUNTING SUITE
    "invoice-automation": {"title": "AP Invoice Automation", "cat": "Accounting Suite", "icon": "🧾", "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40"},
    "general-ledger": {"title": "Unified General Ledger", "cat": "Accounting Suite", "icon": "📚", "image": "https://images.unsplash.com/photo-1554224154-26032ffc0d07"},
    "bank-recon": {"title": "Automated Bank Recon", "cat": "Accounting Suite", "icon": "🏦", "image": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc"},
    "inventory-sync": {"title": "Real-Time Inventory Sync", "cat": "Accounting Suite", "icon": "🔄", "image": "https://images.unsplash.com/photo-1586880244406-556ebe35f282"}
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Altametrics {cat}</title>
    <meta name="description" content="Discover how Altametrics {title} can transform your restaurant operations, reduce costs, and streamline your {cat}.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        .feature-hero {{ padding: 180px 5% 100px; text-align: center; background: radial-gradient(circle at top, rgba(99, 102, 241, 0.05), transparent 60%); }}
        .feature-hero h1 {{ font-size: 3.5rem; font-weight: 900; letter-spacing: -0.04em; margin-bottom: 25px; color:#0f172a; }}
        .feature-hero .text-gradient {{ background: linear-gradient(135deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .feature-badges {{ margin-bottom: 30px; }}
        .feature-badge {{ display: inline-block; padding: 8px 16px; background: rgba(99,102,241,0.1); color: #6366f1; border-radius: 100px; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em; }}
        .feature-desc {{ font-size: 1.25rem; color: #64748b; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; }}
        .hero-img {{ width: 100%; max-width: 1000px; margin: 40px auto 0; border-radius: 20px; box-shadow: 0 30px 60px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05); object-fit: cover; height: 500px; }}
        
        .benefits-section {{ padding: 100px 5%; background: white; }}
        .benefits-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; max-width: 1200px; margin: 0 auto; text-align: center; }}
        .benefit-card {{ padding: 40px; background: #f8fafc; border-radius: 24px; transition: transform 0.3s ease; box-shadow: 0 10px 30px rgba(0,0,0,0.02);border: 1px solid rgba(0,0,0,0.04); }}
        .benefit-card:hover {{ transform: translateY(-10px); border-color: rgba(99,102,241,0.2); box-shadow: 0 10px 30px rgba(99,102,241,0.1); }}
        .benefit-icon {{ font-size: 3rem; margin-bottom: 20px; }}
        .benefit-card h3 {{ font-size: 1.5rem; margin-bottom: 15px; color: #0f172a; }}
        .benefit-card p {{ color: #64748b; font-size: 1.05rem; line-height:1.5; }}

        .deep-dive {{ padding: 100px 5%; background: #f8fafc; }}
        .z-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; max-width: 1200px; margin: 0 auto 100px; }}
        .z-row:last-child {{ margin-bottom: 0; }}
        .z-row:nth-child(even) .z-content {{ order: 2; }}
        .z-row:nth-child(even) .z-image {{ order: 1; }}
        .z-content h2 {{ font-size: 2.5rem; font-weight: 800; color: #0f172a; margin-bottom: 20px; letter-spacing: -0.02em; line-height:1.1; }}
        .z-content p {{ font-size: 1.15rem; color: #475569; margin-bottom: 30px; line-height: 1.6; }}
        .z-list {{ list-style: none; padding: 0; margin-bottom:30px; }}
        .z-list li {{ font-size: 1.05rem; color: #334155; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; font-weight:500; }}
        .z-list li:before {{ content: '✓'; color: white; border-radius:50%; background:#10b981; padding:2px 6px; font-size:0.8rem; font-weight: bold; }}
        .z-image img {{ width: 100%; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); height: 400px; object-fit: cover; border:1px solid rgba(0,0,0,0.05); }}

        .feature-cta {{ padding: 100px 5%; text-align: center; background: white; }}
        .cta-box {{ max-width: 900px; margin: 0 auto; padding: 60px; background: linear-gradient(135deg, #0f172a, #1e293b); border-radius: 32px; color: white; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); }}
        .cta-box h2 {{ font-size: 3rem; font-weight: 800; margin-bottom: 20px; letter-spacing: -0.03em; }}
        .cta-box p {{ font-size: 1.25rem; color: #cbd5e1; margin-bottom: 40px; }}
        .btn-white {{ display: inline-block; padding: 15px 40px; background: white; color: #0f172a; font-weight: 700; border-radius: 12px; text-decoration: none; font-size: 1.1rem; transition: transform 0.2s; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .btn-white:hover {{ transform: translateY(-3px); box-shadow: 0 15px 25px rgba(0,0,0,0.15); }}

        .faq-section {{ padding: 100px 5%; background: #f8fafc; border-top: 1px solid #f1f5f9; }}
        .faq-heading {{ text-align: center; margin-bottom: 60px; }}
        .faq-heading h2 {{ font-size:2.5rem; font-weight:800; margin-bottom:15px; letter-spacing:-0.03em; color:#0f172a; }}
        .accordion {{ max-width: 800px; margin: 0 auto; }}

        .testimonial-banner {{ background: var(--primary-gradient, linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)); padding: 80px 5%; color: white; text-align: center; }}
        .test-quote {{ font-size: 2rem; font-weight: 500; font-style: italic; max-width: 900px; margin: 0 auto 30px; line-height: 1.4; }}
        .test-author {{ font-size: 1.2rem; font-weight: 700; }}
        .test-brand {{ font-size: 1rem; color: rgba(255,255,255,0.8); text-transform:uppercase; letter-spacing:0.1em; margin-top:5px; }}

        @media (max-width: 768px) {{
            .z-row {{ grid-template-columns: 1fr; gap: 40px; }}
            .z-row:nth-child(even) .z-content, .z-row:nth-child(even) .z-image {{ order: unset; }}
            .benefits-grid {{ grid-template-columns: 1fr; }}
            .feature-hero h1 {{ font-size: 2.8rem; }}
        }}
    </style>
</head>
<body>
    <!--NAVBAR_PLACEHOLDER-->

    <header class="feature-hero reveal">
        <div class="feature-badges">
            <span class="feature-badge">{cat}</span>
        </div>
        <h1>Elevate Operations with <br><span class="text-gradient">Automated {title}</span></h1>
        <p class="feature-desc">Stop relying on manual spreadsheets. Let Altametrics' industry-leading {title} engine streamline your workflow, eliminate human error, and drive sustained profitability across your entire enterprise.</p>
        <a href="javascript:void(0)" class="btn-primary" style="font-size:1.1rem; padding:15px 35px;">Request a Demo</a>
        <div style="margin-top: 60px;">
            <img src="{image}?q=80&w=1200&auto=format&fit=crop" alt="{title} Dashboard" class="hero-img">
        </div>
    </header>

    <section class="benefits-section reveal">
        <div class="benefits-grid">
            <div class="benefit-card">
                <div class="benefit-icon">⏱️</div>
                <h3>Save 15+ Hours a Week</h3>
                <p>Automate tedious manual processes associated with your {cat}. Get your managers out of the back office and onto the floor.</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">📉</div>
                <h3>Reduce Operational Costs</h3>
                <p>Pinpoint exactly where margin is leaking and deploy intelligent corrective actions automatically in real-time.</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">🤝</div>
                <h3>Unified Data Ecosystem</h3>
                <p>Say goodbye to siloed tools. We natively pull your POS, vendor, and payroll data into one single source of truth.</p>
            </div>
        </div>
    </section>

    <section class="deep-dive reveal">
        <div class="z-row">
            <div class="z-content">
                <h2>Designed specifically for high-volume enterprise chains.</h2>
                <p>Generic small-business tools break at scale. Altametrics' {title} module natively handles complex regional hierarchies, multi-concept groups, and franchise matrixing without breaking a sweat.</p>
                <ul class="z-list">
                    <li>Cross-store benchmarking & rollup reporting</li>
                    <li>Enterprise-grade permission security controls</li>
                    <li>Seamless bi-directional POS integrations</li>
                </ul>
                <a href="#" class="btn-secondary">Learn more about Enterprise Structure</a>
            </div>
            <div class="z-image">
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop" alt="Enterprise scale">
            </div>
        </div>

        <div class="z-row">
            <div class="z-image">
                <img src="https://images.unsplash.com/photo-1623039405147-547794f92e9e?q=80&w=800&auto=format&fit=crop" alt="AI Engine">
            </div>
            <div class="z-content">
                <h2>Powered by Contextual, Predictive AI.</h2>
                <p>It's not just a digital ledger. The Altametrics {cat} leverages millions of historical data points, real-world supplier data, and machine learning models to surface insights *before* they impact your bottom line.</p>
                <ul class="z-list">
                    <li>Predictive trend analysis & anomaly detection</li>
                    <li>Automated suggested ordering & scheduling</li>
                    <li>Real-time exception alerting</li>
                </ul>
                <a href="#" class="btn-secondary">View AI Capabilities</a>
            </div>
        </div>
    </section>

    <section class="testimonial-banner reveal">
        <div class="test-quote">"Implementing Altametrics {title} was a massive turning point for our operations. We achieved complete visibility across 400 locations and dropped our operational variance by over 12% in the first quarter."</div>
        <div class="test-author">Operations Director</div>
        <div class="test-brand">National Fast Casual Chain</div>
    </section>

    <section class="faq-section reveal">
        <div class="faq-heading">
            <h2>Frequently Asked Questions</h2>
            <p style="color:#64748b; font-size:1.1rem; max-width:600px; margin:0 auto;">Everything you need to know about implementing Altametrics {title}.</p>
        </div>
        <div class="accordion">
            <details class="accordion-item" open>
                <summary class="accordion-header">Does this integrate with my existing tech stack? <div class="accordion-icon"></div></summary>
                <div class="accordion-content">
                    <p>Yes. Altametrics {title} offers native, out-of-the-box API integrations with all major POS systems (Aloha, Micros, Toast, Par), broadline distributors (Sysco, US Foods), and leading payroll providers (ADP, Paylocity).</p>
                </div>
            </details>
            <details class="accordion-item">
                <summary class="accordion-header">How long does implementation take? <div class="accordion-icon"></div></summary>
                <div class="accordion-content">
                    <p>Depending on database complexity and integration requirements, enterprise rollout can take anywhere from 30 to 90 days. Our dedicated CSM team provides comprehensive white-glove onboarding throughout the entire process.</p>
                </div>
            </details>
            <details class="accordion-item">
                <summary class="accordion-header">Is this an add-on or part of the core suite? <div class="accordion-icon"></div></summary>
                <div class="accordion-content">
                    <p>{title} is a core module within the modular {cat} package. You can choose to deploy just this suite to solve immediate pain points, or unlock the entire Altametrics ecosystem for a truly unified operating system.</p>
                </div>
            </details>
        </div>
    </section>

    <section class="feature-cta reveal">
        <div class="cta-box">
            <h2>Ready to transform your {cat} operations?</h2>
            <p>Join the 100,000+ restaurant professionals using Altametrics to scale profitability without the growing pains.</p>
            <a href="javascript:void(0)" class="btn-white">Book a Strategy Call</a>
        </div>
    </section>

    <!--FOOTER_PLACEHOLDER-->
    
    <script src="script.js"></script>
</body>
</html>
"""

def extract_globals():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print("Error reading index.html:", e)
        return "", ""
        
    # Extract nav
    nav_start = content.find('<nav class="navbar')
    nav_end = content.find('</nav>') + 6
    navbar = content[nav_start:nav_end]
    
    # Extract footer
    footer_start = content.find('<footer>')
    footer_end = content.find('</footer>') + 9
    footer = content[footer_start:footer_end]
    
    # REPLACE all anchor links with page links in the NAVBAR!
    # Because index.html currently has workforce-scheduling.html#ai-forecasting, we fix that here.
    # The output navbar will have correct links!
    for slug in PAGES.keys():
        old_pattern_1 = f'href="workforce-scheduling.html#{slug}"'
        old_pattern_2 = f'href="inventory.html#{slug}"'
        old_pattern_3 = f'href="checklist.html#{slug}"'
        old_pattern_4 = f'href="reporting.html#{slug}"'
        old_pattern_5 = f'href="accounting.html#{slug}"'
        
        new_link = f'href="{slug}.html"'
        navbar = navbar.replace(old_pattern_1, new_link)
        navbar = navbar.replace(old_pattern_2, new_link)
        navbar = navbar.replace(old_pattern_3, new_link)
        navbar = navbar.replace(old_pattern_4, new_link)
        navbar = navbar.replace(old_pattern_5, new_link)
        
    return navbar, footer

def main():
    navbar, footer = extract_globals()
    if not navbar or not footer:
        print("Failed to extract navbar or footer.")
        return

    # Generate the 20 pages
    for slug, data in PAGES.items():
        html_content = TEMPLATE.format(
            title=data["title"],
            cat=data["cat"],
            icon=data["icon"],
            image=data["image"]
        )
        
        # Inject global components
        html_content = html_content.replace('<!--NAVBAR_PLACEHOLDER-->', navbar)
        html_content = html_content.replace('<!--FOOTER_PLACEHOLDER-->', footer)
        
        with open(f"{slug}.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Generated {slug}.html")

if __name__ == "__main__":
    main()
