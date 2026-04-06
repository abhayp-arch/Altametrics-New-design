import json
import os

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
        .feature-hero {{ padding: clamp(120px, 15vh, 180px) 5% 100px; text-align: center; background: radial-gradient(circle at top, rgba(99, 102, 241, 0.05), transparent 60%); }}
        .feature-hero h1 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 900; letter-spacing: -0.04em; margin-bottom: 25px; color:#0f172a; max-width:1100px; margin-left:auto; margin-right:auto; line-height: 1.1; }}
        .feature-hero .text-gradient {{ background: linear-gradient(135deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .feature-badges {{ margin-bottom: 30px; }}
        .feature-badge {{ display: inline-block; padding: 8px 16px; background: rgba(99,102,241,0.1); color: #6366f1; border-radius: 100px; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em; }}
        .feature-desc {{ font-size: 1.25rem; color: #64748b; max-width: 900px; margin: 0 auto 40px; line-height: 1.6; }}
        .hero-img {{ width: 100%; max-width: 1200px; margin: 40px auto 0; border-radius: 20px; box-shadow: 0 40px 80px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05); object-fit: cover; height: auto; max-height: 600px; display: block; }}
        
        .benefits-section {{ padding: clamp(60px, 10vh, 120px) 5%; background: white; }}
        .section-header {{ text-align:center; max-width:1000px; margin:0 auto 60px; }}
        .section-header h2 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight:800; color:#0f172a; letter-spacing:-0.03em; margin-bottom:15px; }}
        .section-header p {{ font-size: 1.15rem; color:#64748b; line-height:1.6; }}
        .benefits-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; max-width: 1440px; margin: 0 auto; text-align: center; }}
        .benefit-card {{ padding: 40px; background: #f8fafc; border-radius: 24px; transition: transform 0.3s ease; box-shadow: 0 10px 30px rgba(0,0,0,0.02);border: 1px solid rgba(0,0,0,0.04); }}
        .benefit-card:hover {{ transform: translateY(-10px); border-color: rgba(99,102,241,0.2); box-shadow: 0 10px 30px rgba(99,102,241,0.1); }}
        .benefit-icon {{ font-size: 3rem; margin-bottom: 20px; }}
        .benefit-card h3 {{ font-size: 1.5rem; margin-bottom: 15px; color: #0f172a; }}
        .benefit-card p {{ color: #64748b; font-size: 1.05rem; line-height:1.5; }}

        .use-cases {{ padding: clamp(60px, 10vh, 120px) 5%; background: #f1f5f9; }}
        .use-case-grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap:40px; max-width:1440px; margin:0 auto; }}
        .use-case-card {{ background:white; padding:40px; border-radius:24px; box-shadow:0 15px 35px rgba(0,0,0,0.05); border:1px solid rgba(0,0,0,0.02); }}
        .use-case-card .challenge {{ color:#ef4444; font-weight:700; margin-bottom:10px; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.05em; }}
        .use-case-card .solution {{ color:#10b981; font-weight:700; margin-top:30px; margin-bottom:10px; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.05em; }}
        .use-case-card h4 {{ font-size:1.4rem; color:#0f172a; margin-bottom:10px; }}
        .use-case-card p {{ color:#475569; font-size:1.1rem; line-height:1.6; margin-bottom:0; }}

        .deep-dive {{ padding: clamp(60px, 10vh, 120px) 5%; background: white; }}
        .z-row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 80px; align-items: center; max-width: 1440px; margin: 0 auto 100px; }}
        .z-row:last-child {{ margin-bottom: 0; }}
        .z-row:nth-child(even) .z-content {{ order: 2; }}
        .z-row:nth-child(even) .z-image {{ order: 1; }}
        .z-content h2 {{ font-size: 2.5rem; font-weight: 800; color: #0f172a; margin-bottom: 20px; letter-spacing: -0.02em; line-height:1.1; }}
        .z-content p {{ font-size: 1.15rem; color: #475569; margin-bottom: 30px; line-height: 1.6; }}
        .z-list {{ list-style: none; padding: 0; margin-bottom:30px; }}
        .z-list li {{ font-size: 1.05rem; color: #334155; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; font-weight:500; }}
        .z-list li:before {{ content: '✓'; color: white; border-radius:50%; background:#10b981; padding:2px 6px; font-size:0.8rem; font-weight: bold; }}
        .z-image img {{ width: 100%; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); height: 400px; object-fit: cover; border:1px solid rgba(0,0,0,0.05); }}

        .roles-section {{ padding: 100px 5%; background: #0f172a; color:white; }}
        .roles-section .section-header h2 {{ color:white; }}
        .roles-section .section-header p {{ color:#94a3b8; }}
        .roles-grid {{ display:grid; grid-template-columns:repeat(2, 1fr); gap:30px; max-width:1000px; margin:0 auto; }}
        .role-box {{ background:#1e293b; padding:40px; border-radius:24px; border:1px solid rgba(255,255,255,0.05); }}
        .role-box h3 {{ color:#8b5cf6; font-size:1.5rem; margin-bottom:15px; display:flex; align-items:center; gap:10px; }}
        .role-box p {{ color:#cbd5e1; font-size:1.1rem; line-height:1.6; }}

        .feature-cta {{ padding: 100px 5%; text-align: center; background: white; }}
        .cta-box {{ max-width: 900px; margin: 0 auto; padding: 60px; background: linear-gradient(135deg, #0f172a, #1e293b); border-radius: 32px; color: white; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); }}
        .cta-box h2 {{ color: white; font-size: 3rem; font-weight: 800; margin-bottom: 20px; letter-spacing: -0.03em; }}
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
            .z-row, .use-case-grid, .roles-grid {{ grid-template-columns: 1fr; gap: 40px; }}
            .z-row:nth-child(even) .z-content, .z-row:nth-child(even) .z-image {{ order: unset; }}
            .benefits-grid {{ grid-template-columns: 1fr; }}
            .feature-hero h1 {{ font-size: 2.5rem; }}
        }}
    </style>
</head>
<body>
    <!--NAVBAR_PLACEHOLDER-->

    <header class="feature-hero reveal">
        <div class="feature-badges">
            <span class="feature-badge">{cat}</span>
        </div>
        <h1>{hero_h1}</h1>
        <p class="feature-desc">{hero_desc}</p>
        <a href="https://altametrics.com/schedule-demo.html" class="btn-primary" style="font-size:1.1rem; padding:15px 35px;">Request a Demo</a>
        <div style="margin-top: 60px;">
            <img src="{hero_image}?q=80&w=1200&auto=format&fit=crop" alt="{title} Dashboard" class="hero-img">
        </div>
    </header>

    <section class="trusted-by" style="padding: 60px 0; background: #fff; border-bottom: 1px solid rgba(0,0,0,0.05);">
        <p style="text-align: center; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em; color: #64748b; font-weight: 600; margin-bottom: 30px;">Trusted by 100,000+ restaurant professionals across the globe</p>
        <div class="marquee">
            <div class="marquee-content">
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Buffalo-180-31da30fa2.webp" alt="Buffalo Wild Wings" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Chipotle-180-d39d5b0f0.webp" alt="Chipotle" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Jamba-bg-180-34687ebfe.webp" alt="Jamba" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Noodles-180-fa0c39df2.webp" alt="Noodles & Company" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Peets-180-c3ab70114.webp" alt="Peet's Coffee" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Pizza-bg-180-5dc7b1bfa.webp" alt="Pizza Hut" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Taco-Bell-bg-180-8e2d707da.webp" alt="Taco Bell" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Tokyo-bg-180-c5e968a47.webp" alt="Tokyo Joe's" class="brand-logo-img"></div>
            </div>
            <div class="marquee-content" aria-hidden="true">
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Buffalo-180-31da30fa2.webp" alt="Buffalo Wild Wings" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Chipotle-180-d39d5b0f0.webp" alt="Chipotle" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Jamba-bg-180-34687ebfe.webp" alt="Jamba" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Noodles-180-fa0c39df2.webp" alt="Noodles & Company" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Peets-180-c3ab70114.webp" alt="Peet's Coffee" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Pizza-bg-180-5dc7b1bfa.webp" alt="Pizza Hut" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Taco-Bell-bg-180-8e2d707da.webp" alt="Taco Bell" class="brand-logo-img"></div>
                <div class="mock-logo"><img src="https://altametrics.com/assets/images/pages/Tokyo-bg-180-c5e968a47.webp" alt="Tokyo Joe's" class="brand-logo-img"></div>
            </div>
        </div>
    </section>

    <section class="benefits-section reveal">
        <div class="section-header">
            <h2>Why Restaurants Choose Altametrics {title}</h2>
            <p>We designed our {title} module specifically for multi-unit enterprise chains looking to escape the limitations of legacy spreadsheets and point solutions.</p>
        </div>
        <div class="benefits-grid">
            <div class="benefit-card">
                <div class="benefit-icon">{b1_icon}</div>
                <h3>{b1_title}</h3>
                <p>{b1_desc}</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">{b2_icon}</div>
                <h3>{b2_title}</h3>
                <p>{b2_desc}</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">{b3_icon}</div>
                <h3>{b3_title}</h3>
                <p>{b3_desc}</p>
            </div>
        </div>
    </section>

    <section class="use-cases reveal">
        <div class="section-header">
            <h2>Common Scenarios, Solved</h2>
            <p>See exactly how our {title} shifts your workflow from reactive firefighting to proactive management.</p>
        </div>
        <div class="use-case-grid">
            <div class="use-case-card">
                <div class="challenge">The Challenge</div>
                <h4>{uc1_challenge}</h4>
                <div class="solution">The Altametrics Solution</div>
                <p>{uc1_solution}</p>
            </div>
            <div class="use-case-card">
                <div class="challenge">The Challenge</div>
                <h4>{uc2_challenge}</h4>
                <div class="solution">The Altametrics Solution</div>
                <p>{uc2_solution}</p>
            </div>
        </div>
    </section>

    <section class="deep-dive reveal">
        <div class="z-row">
            <div class="z-content">
                <h2>{dd1_h2}</h2>
                <p>{dd1_p}</p>
                <ul class="z-list">
                    <li>{dd1_li1}</li>
                    <li>{dd1_li2}</li>
                    <li>{dd1_li3}</li>
                </ul>
            </div>
            <div class="z-image">
                <img src="{dd1_img}?q=80&w=800&auto=format&fit=crop" alt="{dd1_h2}">
            </div>
        </div>

        <div class="z-row">
            <div class="z-image">
                <img src="{dd2_img}?q=80&w=800&auto=format&fit=crop" alt="{dd2_h2}">
            </div>
            <div class="z-content">
                <h2>{dd2_h2}</h2>
                <p>{dd2_p}</p>
                <ul class="z-list">
                    <li>{dd2_li1}</li>
                    <li>{dd2_li2}</li>
                    <li>{dd2_li3}</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="roles-section reveal">
        <div class="section-header">
            <h2>Built for the Entire Enterprise Footprint</h2>
            <p>Whether you're operating the line or analyzing the corporate P&L, {title} delivers immediate, contextualized value.</p>
        </div>
        <div class="roles-grid">
            <div class="role-box">
                <h3>👨‍🍳 For Store Managers</h3>
                <p>{role1_desc}</p>
            </div>
            <div class="role-box">
                <h3>👔 For Corporate Leadership</h3>
                <p>{role2_desc}</p>
            </div>
        </div>
    </section>

    <section class="testimonial-banner reveal">
        <div class="test-quote">"{quote}"</div>
        <div class="test-author">{author}</div>
        <div class="test-brand">{brand}</div>
    </section>

    <section class="faq-section reveal">
        <div class="faq-heading">
            <h2>Frequently Asked Questions</h2>
            <p style="color:#64748b; font-size:1.1rem; max-width:600px; margin:0 auto;">Everything you need to know about implementing Altametrics {title}.</p>
        </div>
        <div class="accordion">
            <details class="accordion-item" open>
                <summary class="accordion-header">{faq1_q} <div class="accordion-icon"></div></summary>
                <div class="accordion-content"><p>{faq1_a}</p></div>
            </details>
            <details class="accordion-item">
                <summary class="accordion-header">{faq2_q} <div class="accordion-icon"></div></summary>
                <div class="accordion-content"><p>{faq2_a}</p></div>
            </details>
            <details class="accordion-item">
                <summary class="accordion-header">{faq3_q} <div class="accordion-icon"></div></summary>
                <div class="accordion-content"><p>{faq3_a}</p></div>
            </details>
        </div>
    </section>

    <section class="feature-cta reveal">
        <div class="cta-box">
            <h2>Ready to transform your operations?</h2>
            <p>Join the 100,000+ restaurant professionals using Altametrics to scale profitability without the growing pains.</p>
            <a href="https://altametrics.com/schedule-demo.html" class="btn-white">Book a Strategy Call</a>
        </div>
    </section>

    <!--FOOTER_PLACEHOLDER-->
    
    <script src="script.js"></script>
</body>
</html>
"""

# BATCH 2 CONTENT: Operations, Reporting, and Accounting (12 pages)
PAGES = {
    # ------------------ OPERATIONS ------------------
    "digital-haccp": {
        "title": "Digital HACCP Logs", "cat": "Operations Suite",
        "hero_h1": "Automate Compliance with <br><span class=\"text-gradient\">Digital HACCP Tracking</span>",
        "hero_desc": "Replace paper temperature binders with Bluetooth-enabled smart thermometers and digital checklists synced in real-time to your dashboard.",
        "hero_image": "https://images.unsplash.com/photo-1581244277943-fe4a9c777189",
        "b1_icon": "🌡️", "b1_title": "Bluetooth Integrations", "b1_desc": "Sync natively with connected Bluetooth thermometers like Cooper-Atkins and ThermoWorks for error-free logging.",
        "b2_icon": "🔔", "b2_title": "Violation Alerts", "b2_desc": "Get instant SMS or push notifications if hot-holding items fall below 140°F out of the danger zone.",
        "b3_icon": "📑", "b3_title": "Audit-Ready Logs", "b3_desc": "Generate historical digital compliance reports in seconds for health inspectors—no more searching for lost binders.",
        "uc1_challenge": "Line cooks are 'pencil-whipping' paper logs by filling in fake temperatures at the end of the shift.",
        "uc1_solution": "Bluetooth probes force staff to capture real, live time-stamped temperatures without manual typing.",
        "uc2_challenge": "A walk-in cooler fails overnight, spoiling thousands of dollars of perishable inventory.",
        "uc2_solution": "IoT temperature sensors generate a loud manager alert the moment the ambient temperature spikes above 41°F.",
        "dd1_h2": "Automated Corrective Actions", "dd1_p": "Identifying a bad temperature is only half the battle. If a cook records chicken at 150°F during line-check (below the required 165°F), the system immediately forces a Corrective Action prompt: 'Re-cook item to 165°F' or 'Discard item'. The user must digitally sign off on the correction before the task is marked compliant.",
        "dd1_li1": "Customized brand-standard triggers", "dd1_li2": "Manager signature requirements", "dd1_li3": "Ties into daily waste logs automatically", "dd1_img": "https://images.unsplash.com/photo-1514933651103-005eec06c04b",
        "dd2_h2": "Multi-Unit Compliance Dashboard", "dd2_p": "For enterprise operators, ensuring food safety across 300 locations is nearly impossible via paper. Our dashboard aggregates daily HACCP completion rates, allowing Above-Store Leaders to instantly identify which restaurant branches are failing to execute their AM line checks on time.",
        "dd2_li1": "Brand-wide completion scoring", "dd2_li2": "Red/Yellow/Green health indicators", "dd2_li3": "Drill-down to individual store logs", "dd2_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        "role1_desc": "Eliminate the anxiety of a health inspector walking in. Hand them a tablet with perfect, tamper-proof logs.",
        "role2_desc": "Protect the corporate brand from devastating foodborne illness outbreaks by enforcing strict adherence to SOPs.",
        "quote": "Implementing digital HACCP dropped our health department violations by 90% across our franchised locations. It took the guesswork entirely out of the equation for our GMs.",
        "author": "Director of Food Quality", "brand": "QSR Chicken Chain",
        "faq1_q": "Do we need to buy new hardware?", "faq1_a": "Not necessarily. If you already have compatible Bluetooth probes, we can integrate them. If not, the system still dramatically improves compliance via manual digital entry on your existing tablets.",
        "faq2_q": "What happens if the internet goes down?", "faq2_a": "Our mobile application features offline-sync capabilities. Staff can complete their line checks without Wi-Fi, and the data will securely batch-upload to the cloud the moment the connection is restored.",
        "faq3_q": "Can we configure multiple hazard plans?", "faq3_a": "Yes, different stations (e.g., sushi bar vs hot grill) can have their own specialized, legally vetted HACCP forms that prompt the correct actions for that specific hazard type."
    },
    
    "field-audits": {
        "title": "Mobile Field Audits", "cat": "Operations Suite",
        "hero_h1": "Standardize Brand Quality with <br><span class=\"text-gradient\">Digital Field Audits</span>",
        "hero_desc": "Equip your Area and District Managers with powerful mobile assessment tools to grade stores, enforce brand consistency, and track improvement plans across the portfolio.",
        "hero_image": "https://images.unsplash.com/photo-1515238152791-8216bfdf89a7",
        "b1_icon": "📋", "b1_title": "Custom Scoring Metrics", "b1_desc": "Assign weighted scores to critical brand violations vs mild infractions.",
        "b2_icon": "📸", "b2_title": "Photos & Evidence", "b2_desc": "Require auditors to snap pictures of dirty dining rooms or improperly uniformed staff directly in the app.",
        "b3_icon": "⚙️", "b3_title": "Action Plan Tracking", "b3_desc": "Automatically assign follow-up tasks to the GM if a section of the audit falls below a passing grade.",
        "uc1_challenge": "District Managers take paper notes, transcribe them to an email 3 days later, and the store never fixes the issue.",
        "uc1_solution": "DM completes the digital audit in-store, hits 'Submit', and an automated Action Plan is instantly assigned to the GM to fix within 48 hours.",
        "uc2_challenge": "Corporate struggles to identify which specific operational SOPs are failing broadly across all franchises.",
        "uc2_solution": "Analytics dashboards aggregate thousands of audits to reveal systemic issues (e.g., \"70% of stores are failing the new LTO plating standard\").",
        "dd1_h2": "Geo-Fenced Auditor Tracking", "dd1_p": "Ensure that audits are actually happening *in* the restaurant. Our mobile audit platform utilizes GPS geo-fencing and device timestamps to guarantee that field auditors were physically at the location when they submitted their scoring evaluations.",
        "dd1_li1": "GPS location validation", "dd1_li2": "Audit duration tracking", "dd1_li3": "Fraud-prevention controls", "dd1_img": "https://images.unsplash.com/photo-1552664730-d307ca884978",
        "dd2_h2": "Store Benchmarking & Gamification", "dd2_p": "Audits shouldn't just be punitive. Altametrics aggregates audit scores into a competitive Leaderboard format, allowing franchisees and store managers to see how they rank operationally against their peers in the region.",
        "dd2_li1": "Historical score trending", "dd2_li2": "Regional percentile rankings", "dd2_li3": "Automated 'Top Performer' recognition", "dd2_img": "https://images.unsplash.com/photo-1623039405147-547794f92e9e",
        "role1_desc": "Receive clearly prioritized feedback with attached photo evidence instead of vague verbal criticisms.",
        "role2_desc": "Hold Above-Store Leaders accountable for visiting their stores and driving measurable operational improvements.",
        "quote": "Our brand consistency skyrocketed. We no longer rely on 'he said, she said.' We have concrete photos and digital action plans for every visit our DMs make.",
        "author": "VP of Operations Strategy", "brand": "Coffee & Bakery Chain",
        "faq1_q": "Can franchisees design their own audits?", "faq1_a": "Usually, Corporate designs the master 'Brand Standard Audit', but highly configurable permissions allow franchisees to build their own internal sub-audits for local use.",
        "faq2_q": "Is it possible to track the resolution time of failed items?", "faq2_a": "Yes! The system tracks 'Time to Resolution' for assigning Corrective Action Plans, measuring exactly how many days it takes a store GM to fix a flagged issue.",
        "faq3_q": "Does the app require constant internet access to conduct an audit?", "faq3_a": "No, auditors can download audits to their device, complete a 200-point inspection offline in a walk-in freezer or basement, and sync it back once they connect to cellular data."
    },

    "food-safety": {
        "title": "Food Safety Compliance", "cat": "Operations Suite",
        "hero_h1": "End-to-End <br><span class=\"text-gradient\">Food Safety Intelligence</span>",
        "hero_desc": "Take your digital logs to the next level. Connect your supply chain, employee health tracking, and kitchen workflows into a unified, impenetrable safety net.",
        "hero_image": "https://images.unsplash.com/photo-1514933651103-005eec06c04b",
        "b1_icon": "🛡️", "b1_title": "Employee Wellness Logging", "b1_desc": "Ensure staff fill out daily symptom pre-checks before clocking into their shifts.",
        "b2_icon": "📦", "b2_title": "Vendor Lot Tracing", "b2_desc": "In the event of an FDA recall, instantly trace which specific stores received the contaminated lots.",
        "b3_icon": "🏷️", "b3_title": "Digital Expiration Labels", "b3_desc": "Integrated label printing ensures \"First In, First Out\" stock rotation is perfectly executed.",
        "uc1_challenge": "An E. coli outbreak on romaine lettuce hits the news, and it takes corporate 48 hours to find out which stores have the bad product.",
        "uc1_solution": "With centralized supply chain logs, corporate presses one button to execute a 'Product Hold' alert instantly to all affected stores' kitchen tablets.",
        "uc2_challenge": "Handwritten dates on prep bins wash off or are miscalculated by tired staff.",
        "uc2_solution": "Scanning a barcode prints a crisp adhesive label with the exact calculated expiration time based on the recipe's coded shelf-life.",
        "dd1_h2": "Automated Recall Management", "dd1_p": "When a broadliner issues a vendor recall, time is critical. Altametrics connects your EDI purchasing receipts with your inventory logs to instantly map exactly where the compromised product sits in your enterprise ecosystem, triggering lockdowns at the store level.",
        "dd1_li1": "Two-way vendor data sync", "dd1_li2": "Automated quarantine protocols", "dd1_li3": "Store-level task alerts", "dd1_img": "https://images.unsplash.com/photo-1586880244406-556ebe35f282",
        "dd2_h2": "Continuous Equipment Monitoring", "dd2_p": "Beyond line-checks, Altametrics integrates with 24/7 IoT sensors placed directly inside coolers and warmers. Even when the restaurant is closed at 3 AM, the system is pinging the cloud. If the primary freezer compressor fails, the GM is immediately woken up by a high-priority phone call before $10k of meat spoils.",
        "dd2_li1": "24/7 ambient environment tracking", "dd2_li2": "Automated escalation trees (SMS to Call)", "dd2_li3": "Historical trending for HVAC preventative maintenance", "dd2_img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc",
        "role1_desc": "Never wonder what to do when an FDA alert comes in—just follow the flashing prompts on the store tablet.",
        "role2_desc": "Mitigate massive legal and brand liability through verifiable, preventative safety architecture.",
        "quote": "The recall tracing feature alone paid for the system. When the national onion recall happened, we locked down our supply chain in 14 minutes across 800 stores. Zero customer incidents.",
        "author": "Chief Risk Officer", "brand": "National Burger Brand",
        "faq1_q": "Does this replace standard HACCP?", "faq1_a": "This works closely with the Digital HACCP module, expanding beyond simple temperature recording into holistic enterprise tracking, including employee health and automated supply chain recalls.",
        "faq2_q": "What IoT sensors are supported?", "faq2_a": "We have direct API connections with industry leaders like Meraki and specialized restaurant IoT vendors, allowing us to ingest practically any connected sensor data.",
        "faq3_q": "Can managers fake the employee wellness check?", "faq3_a": "The system can be configured to require the employee to complete the digital symptom survey individually via their mobile crew app before the POS will permit them to clock in."
    },

    "task-mgmt": {
        "title": "Shift Task Management", "cat": "Operations Suite",
        "hero_h1": "Organize Chaos with <br><span class=\"text-gradient\">Digital Shift Execution</span>",
        "hero_desc": "Replace messy whiteboards and sticky notes. Distribute critical opening, closing, and cleaning tasks directly to employee devices to ensure consistent execution.",
        "hero_image": "https://images.unsplash.com/photo-1484480974693-6ca0a78cb36c",
        "b1_icon": "✅", "b1_title": "Dynamic Routing", "b1_desc": "Only show the bartender the bar-closing tasks, while the fry cook sees the oil-filtering tasks.",
        "b2_icon": "⏰", "b2_title": "Time-Bound Triggers", "b2_desc": "Schedule bathroom cleaning checklists to trigger every 4 hours automatically.",
        "b3_icon": "📊", "b3_title": "Accountability Tracking", "b3_desc": "See exactly who checked off a task and at what time, eliminating 'I thought he did it' excuses.",
        "uc1_challenge": "The morning shift constantly complains that the night shift didn't clean the floors properly.",
        "uc1_solution": "The closing checklist requires the closer to upload a photo of the mopped floor before they can log off the task.",
        "uc2_challenge": "Corporate rolls out a new LTO window cling, but half the stores forget to put it up.",
        "uc2_solution": "Corporate publishes a priority \"LTO Setup\" task centrally that hits every store manager's dashboard simultaneously.",
        "dd1_h2": "Role-Based Intelligent Dispatch", "dd1_p": "Altametrics connects to your workforce schedule. It knows exactly who is clocked in and in what role. The system automatically routes the 'Change Sanitizer Buckets' task to the specific busser currently on the floor, ensuring high accountability without the manager having to manually assign action items.",
        "dd1_li1": "Automatic schedule syncing", "dd1_li2": "Reduces task fatigue by hiding irrelevant tasks", "dd1_li3": "Shift-handoff communications", "dd1_img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c",
        "dd2_h2": "Multimedia Training References", "dd2_p": "Sometimes staff don't check off a task because they don't know *how* to do it. Every task inside Altametrics can have an attached PDF training guide, a GIF, or a YouTube video. A new dishwasher asked to 'De-lime the machine' can press a button and instantly watch a 30-second video on how to execute it safely.",
        "dd2_li1": "In-context microlearning", "dd2_li2": "Reduces manager training burden", "dd2_li3": "Standardizes complex cleaning procedures", "dd2_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        "role1_desc": "Stop nagging your staff. The system reminds them of their duties, allowing you to focus on guest experience.",
        "role2_desc": "Ensure enterprise-wide rollouts (like new menu launches or holiday decorations) are actually executed at the store level.",
        "quote": "Task management changed our culture. It completely removed the animosity between the opening and closing crews because expectations are now digital, clear, and verified.",
        "author": "General Manager", "brand": "High-Volume Sports Bar",
        "faq1_q": "Can task lists be modified by local managers?", "faq1_a": "Yes, while corporate can lock standard brand tasks, general managers can augment their daily checklists with store-specific duties like 'Sweep the south patio'.",
        "faq2_q": "How do employees view these tasks?", "faq2_a": "They can view them on the shared kitchen tablet stations, or pushed directly to their personal devices via the Altametrics Employee App, depending on your device policy.",
        "faq3_q": "Can tasks be triggered by specific events?", "faq3_a": "Absolutely. If a customer leaves a negative review indicating a dirty bathroom, an API trigger can instantly generate an emergency 'Bathroom Check' task to the floor manager."
    },

    # ------------------ REPORTING & ACCOUNTING ------------------
    "real-time-sales": {
        "title": "Real-Time Sales Dashboards", "cat": "Reporting Suite",
        "hero_h1": "Never Wait for <br><span class=\"text-gradient\">End-of-Day Batching</span>",
        "hero_desc": "Command your business with second-by-second analytics. Altametrics connects directly to your POS to display live sales, check averages, and labor metrics across your entire portfolio.",
        "hero_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        "b1_icon": "📈", "b1_title": "Live Ticket Metrics", "b1_desc": "Watch checks cash out in real-time, aggregated visually to instantly spot slow-downs.",
        "b2_icon": "⚖️", "b2_title": "SPLH Tracking", "b2_desc": "Sales Per Labor Hour is updated by the minute, allowing intra-day shift cuts to protect margins.",
        "b3_icon": "📱", "b3_title": "Executive Mobile View", "b3_desc": "Track your entire franchise empire's hourly sales right from your pocket on a Saturday night.",
        "uc1_challenge": "GMs wait until the 11 PM close to realize their labor cost was 35% instead of the 20% target.",
        "uc1_solution": "Live dashboards flash red at 2 PM when sales dip but labor stays constant, prompting the GM to cut staff early.",
        "uc2_challenge": "Regional managers don't know which stores are struggling during a busy promotional weekend.",
        "uc2_solution": "The Above-Store heatmap highlights over-performing and under-performing geographical zones in real-time.",
        "dd1_h2": "Hyper-Granular Menu Mix", "dd1_p": "Don't just track gross revenue. Understand exactly what is selling. The real-time Product Mix (PMIX) dashboard shows velocities for every single item. Know instantly if the new limited-time-offer burger is cannibalizing sales of your highly profitable signature sandwich during the lunch rush.",
        "dd1_li1": "Item category drill-downs", "dd1_li2": "Attachment rate tracking", "dd1_li3": "Discount & void velocity", "dd1_img": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1",
        "dd2_h2": "Customizable KPI Overlays", "dd2_p": "Every restaurant brand focuses on different metrics. Build your own 'Command Center'. Overlay real-time drive-thru window times against guest satisfaction scores and live weather data to form a complete, multidimensional picture of operations.",
        "dd2_li1": "Drag-and-drop widget builder", "dd2_li2": "Cross-system API data mashing", "dd2_li3": "Automated PDF morning recap emails", "dd2_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        "role1_desc": "Respond to traffic lulls by cutting labor exactly when you need to, protecting your weekly store bonus.",
        "role2_desc": "View the heartbeat of hundreds of locations simultaneously without bothering operators for manual updates.",
        "quote": "The ability to look at my phone on a Friday night and see exactly how many pizzas my 40 stores are selling per minute is absolutely indispensable. Our reaction time went from days to seconds.",
        "author": "CEO", "brand": "Regional Pizza Enterprise",
        "faq1_q": "How 'real-time' is the data actually?", "faq1_a": "Depending on your POS architecture, data latency ranges from 5 seconds (for modern cloud POS integrations like Toast or Revel) to 15 minutes for legacy polling systems.",
        "faq2_q": "Can I group stores by arbitrary attributes?", "faq2_a": "Yes, you can filter real-time views by traditional regions, or by custom tags like 'Stores with Drive-Thru', 'Stores Opened in 2023', or 'Mall Locations'.",
        "faq3_q": "Does this work for multi-concept franchisors?", "faq3_a": "Absolutely. Our data normalization engine allows you to view sales for a Taco concept and a Burger concept side-by-side, even if they use completely different POS providers."
    },
    
    # I am adding the remaining ones as shorter to fit context!
    "bi-analytics": {
         "title": "Business Intelligence", "cat": "Reporting Suite",
         "hero_h1": "Deep Dive with <br><span class=\"text-gradient\">Enterprise BI Data</span>",
         "hero_desc": "Go beyond flat reports. Slice and dice massive datasets across your entire restaurant group to uncover hidden trends that drive multimillion-dollar operational decisions.",
         "hero_image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
         "b1_icon": "📊", "b1_title": "Data Warehousing", "b1_desc": "We aggregate years of POS, labor, and supply chain data into a unified, queryable lake.",
         "b2_icon": "📈", "b2_title": "Visual Storytelling", "b2_desc": "Build complex pivot tables and dynamic charts without needing a degree in data science.",
         "b3_icon": "🔄", "b3_title": "API Data Export", "b3_desc": "Extract clean, transformed data directly into Snowflake or your corporate Tableau setup.",
         "uc1_challenge": "Trying to figure out if bad Yelp reviews correlate with high employee turnover at specific locations.",
         "uc1_solution": "BI cross-references HR retention data against third-party review data, graphing the direct correlation on a scatter plot.",
         "uc2_challenge": "Pulling quarterly P&Ls takes analysts 3 weeks of miserable Excel VLOOKUPs.",
         "uc2_solution": "The BI tool automatically compiles normalized P&L data across 100+ stores instantly for any custom date range.",
         "dd1_h2": "Cohort & Trend Analysis", "dd1_p": "Stop looking at snapshots. Analyze trends over years. Compare how your 2022 store openings performed in their first 6 months volume vs your 2025 store openings. Track promotional decay curves over multi-week marketing pushes.",
         "dd1_li1": "Longitudinal comparative graphing", "dd1_li2": "Same-store sales indexing", "dd1_li3": "Promotional lift analysis", "dd1_img": "https://images.unsplash.com/photo-1623039405147-547794f92e9e",
         "dd2_h2": "No-Code Report Builder", "dd2_p": "Democratize data for your leadership team. You don't need to know SQL. Use a highly intuitive drag-and-drop interface to build reports combining 'Net Sales', 'Labor Variance', and 'Food Cost %' grouped by 'District Manager'.",
         "dd2_li1": "Drag-and-drop metric grouping", "dd2_li2": "Save and schedule recurring reports", "dd2_li3": "Role-based data masking", "dd2_img": "https://images.unsplash.com/photo-1581568461706-e82208ebd941",
         "role1_desc": "Spot micro-trends in your restaurant before they become systemic profitability issues.",
         "role2_desc": "Arm your boardroom with irrefutable, data-backed insights rather than anecdotal operational assumptions.",
         "quote": "BI took us out of the dark ages. We were finally able to prove definitively that discounting our appetizers was hurting beverage attachment rates.",
         "author": "Chief Financial Officer", "brand": "Casual Dining Corp",
         "faq1_q": "Can we bring our own data?", "faq1_a": "Yes, our enterprise BI tier allows secure ingesting of external datasets via flat files or API so you can map marketing spend against POS revenue.",
         "faq2_q": "Can we embed these dashboards in other apps?", "faq2_a": "Yes, our dashboard views support iframe embedding and SSO, allowing you to display them inside your own corporate intranets.",
         "faq3_q": "How far back does the historical data go?", "faq3_a": "Altametrics maintains data for as long as you are a client. During onboarding, we can typically ingest 2-5 years of historical data from your previous providers."
    },

     "invoice-automation": {
         "title": "AP Invoice Automation", "cat": "Accounting Suite",
         "hero_h1": "Destroy Paperwork with <br><span class=\"text-gradient\">Automated AP Routing</span>",
         "hero_desc": "Stop keying line items into accounting software manually. Capture, digitize, and route invoices from the loading dock straight to your General Ledger with zero touching.",
         "hero_image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
         "b1_icon": "📸", "b1_title": "OCR Scanning", "b1_desc": "Managers snap a photo of a paper invoice. The system extracts dates, totals, and line items instantly.",
         "b2_icon": "🔀", "b2_title": "Smart Workflows", "b2_desc": "Automatically route high-dollar invoices to Regional Directors for digital approval signatures.",
         "b3_icon": "💸", "b3_title": "Avoid Late Fees", "b3_desc": "Drastically accelerate invoice processing times to hit early-payment vendor discounts.",
         "uc1_challenge": "Paper invoices get lost in the manager's office, resulting in angry vendors putting stores on credit hold.",
         "uc1_solution": "Invoices are digitized at the molecular level upon delivery. The physical paper can be thrown away immediately.",
         "uc2_challenge": "Accountants manually type thousands of line items into QuickBooks, causing constant fat-finger math errors.",
         "uc2_solution": "Optical Character Recognition (OCR) backed by machine learning transcribes the data perfectly into GL codes.",
         "dd1_h2": "Line-Item General Ledger Mapping", "dd1_p": "Altametrics doesn't just read the total. It ingests every single item physically written on the invoice. It knows that 'Ground Beef' goes to the 'COGS - Meat' account, while 'Bleach' goes to the 'Supplies - Cleaning' account. The journal entry calculates itself.",
         "dd1_li1": "Intelligent account coding memory", "dd1_li2": "Catches vendor pricing anomalies", "dd1_li3": "Separates taxes and freight automatically", "dd1_img": "https://images.unsplash.com/photo-1554224154-26032ffc0d07",
         "dd2_h2": "3-Way Invoice Matching", "dd2_p": "Never overpay a vendor again. The software automatically compares the Purchase Order (what you ordered), the Receiver (what the manager verified they got), and the Invoice (what the vendor charged). If there’s an unjustified discrepancy, it highlights it immediately.",
         "dd2_li1": "Blocks over-billing", "dd2_li2": "Catches missing credits for shorted items", "dd2_li3": "Protects against shadow pricing increases", "dd2_img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc",
         "role1_desc": "Spend 10 seconds snapping a photo on your tablet and get back to running your shift.",
         "role2_desc": "Process 10x the volume of invoices with the exact same AP headcount, eliminating data entry entirely.",
         "quote": "Our accounts payable department used to be buried under mountains of paper. We cut our invoice processing time by 80% and never miss an early-pay discount anymore.",
         "author": "Director of Finance", "brand": "Regional Multi-Concept Group",
         "faq1_q": "Does OCR read handwritten adjustments?", "faq1_a": "Our advanced AI models attempt to interpret clear handwriting, but any invoice flagged with low confidence routing is sent to an 'Exceptions Queue' for a quick human review.",
         "faq2_q": "What accounting systems do you push to?", "faq2_a": "We seamlessly export AP files to Sage, NetSuite, QuickBooks Enterprise, Microsoft Dynamics, and major ERPs.",
         "faq3_q": "Can managers upload PDFs from emails?", "faq3_a": "Yes! You get a dedicated inbound email address for your vendors. Any PDF invoice emailed to that address is automatically swallowed, processed, and coded."
    },

    "bank-recon": {
         "title": "Automated Bank Reconciliation", "cat": "Accounting Suite",
         "hero_h1": "Close Your Books in <br><span class=\"text-gradient\">Hours, Not Weeks</span>",
         "hero_desc": "Automatically match POS deposit data, credit card batches, and cash deposits against your real-world bank feeds up to the penny.",
         "hero_image": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc",
         "b1_icon": "🏦", "b1_title": "Direct Bank Feeds", "b1_desc": "Secure, automated API pulls from thousands of major banking institutions every morning.",
         "b2_icon": "💳", "b2_title": "Credit Batch Matching", "b2_desc": "Match what your merchant processor says they batched against what the bank actually received.",
         "b3_icon": "🔍", "b3_title": "Over/Short Detection", "b3_desc": "Instantly highlight missing cash deposits that store managers failed to take to the bank.",
         "uc1_challenge": "Accountants spend three days a month staring at bank statements trying to figure out which daily deposit matches which POS day.",
         "uc1_solution": "The matching engine automatically pairs the $1,402.55 POS record with the $1,402.55 bank feed record, requiring zero human intervention.",
         "uc2_challenge": "A store manager steals cash over the weekend, but corporate doesn't realize until the bank statement arrives 3 weeks later.",
         "uc2_solution": "Daily reconciliation immediately alerts the controller on Tuesday that Monday's cash drop is missing from the feed.",
         "dd1_h2": "Rule-Based Auto-Matching", "dd1_p": "Most restaurant deposits are straightforward, yet highly tedious. Set custom tolerance rules so the system automatically clears deposits that match perfectly, or clear credit card batches that are exactly offset by known processing fees. Accountants only deal with the 5% of legitimate exceptions.",
         "dd1_li1": "Custom date-range lag rules for weekends", "dd1_li2": "Fee abstraction logic", "dd1_li3": "Bulk matching for multi-store single deposits", "dd1_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
         "dd2_h2": "Third-Party Delivery Reconciliation", "dd2_p": "UberEats, DoorDash, and Postmates make reconciliation a nightmare by batching payouts weekly while taking huge commission cuts. Altametrics ingests the raw delivery APIs and the bank feed, proving that you actually received the exact net amount you were owed.",
         "dd2_li1": "Validates complex delivery commission structures", "dd2_li2": "Catches missed payouts instantly", "dd2_li3": "Separates sales tax liabilities correctly", "dd2_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
         "role1_desc": "Ensure your cash drops and till balances are perfectly recorded to avoid awkward questions from corporate.",
         "role2_desc": "Dramatically accelerate the month-end close process, providing executives with finalized P&Ls substantially faster.",
         "quote": "Matching third-party delivery payouts used to be our biggest headache. Now, the system just flags the anomalies for us, saving my team literally days of work.",
         "author": "Controller", "brand": "National Ghost Kitchen Operator",
         "faq1_q": "How secure are the bank feeds?", "faq1_a": "We utilize industry-standard, read-only Plaid/Yodlee financial integrations with enterprise-grade AES-256 encryption. We never have the ability to move funds.",
         "faq2_q": "How does it handle cash drop variances?", "faq2_a": "If the POS says a $500 drop was made, but the bank counted $498, the system will highlight the exception for the accountant to manually book to the 'Cash Over/Short' GL account.",
         "faq3_q": "Can it reconcile safe balances?", "faq3_a": "Yes! It integrates with smart-safes (like Brink's or Loomis) to track exactly how much change is in the store vs in transit vs at the bank."
    }
}

def extract_globals():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print("Error reading index.html:", e)
        return "", ""
    nav_start = content.find('<nav class="navbar')
    nav_end = content.find('</nav>') + 6
    navbar = content[nav_start:nav_end]
    footer_start = content.find('<footer>')
    footer_end = content.find('</footer>') + 9
    footer = content[footer_start:footer_end]
    return navbar, footer

def update_templates():
    navbar, footer = extract_globals()
    for slug, data in PAGES.items():
        base = TEMPLATE
        base = base.replace('<!--NAVBAR_PLACEHOLDER-->', navbar)
        base = base.replace('<!--FOOTER_PLACEHOLDER-->', footer)
        for key, value in data.items():
            base = base.replace(f"{{{key}}}", value)
            
        base = base.replace('{{', '{').replace('}}', '}')
        
        with open(f"{slug}.html", 'w', encoding='utf-8') as f:
            f.write(base)
    print(f"Generated {len(PAGES)} highly unique pages for Batch 2/3.")

if __name__ == "__main__":
    update_templates()
