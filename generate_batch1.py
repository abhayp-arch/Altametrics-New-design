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
            <p>See exactly how our {title} shifts your workforce from reactive firefighting to proactive management.</p>
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

# BATCH 1 CONTENT: Workforce & Inventory (8 pages)
PAGES = {
    # ------------------ WORKFORCE ------------------
    "ai-forecasting": {
        "title": "AI Demand Forecasting", "cat": "Workforce Suite",
        "hero_h1": "Predict Sales with <br><span class=\"text-gradient\">Pinpoint AI Accuracy</span>",
        "hero_desc": "Stop relying on gut-feel schedules. Generate highly accurate, location-specific demand forecasts up to 4 weeks in advance using historical trends, localized weather data, and custom operational anomalies.",
        "hero_image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        
        "b1_icon": "🧠", "b1_title": "Machine Learning Models", "b1_desc": "Our algorithms learn your unique seasonal trends and traffic patterns, getting smarter and more accurate with every transaction.",
        "b2_icon": "🌦️", "b2_title": "Weather Integration", "b2_desc": "Automatically overlay hyper-local weather conditions to dynamically adjust expected traffic and required staffing levels.",
        "b3_icon": "📉", "b3_title": "Slash Labor Variance", "b3_desc": "Eliminate both costly over-staffing and revenue-damaging under-staffing by matching labor directly to verified demand.",
        
        "uc1_challenge": "Relying on last year's sales data misses entirely new trends and current economic shifts.",
        "uc1_solution": "We use a weighted exponential smoothing model that prioritizes recent 4-week trends while still accounting for year-over-year baselines.",
        "uc2_challenge": "Local events or road closures completely invalidate standard automated forecasts.",
        "uc2_solution": "Managers can easily input custom 'Events' (e.g., local concert) to artificially boost or limit the generated AI forecast.",
        
        "dd1_h2": "15-Minute Increment Profiling", "dd1_p": "Daily forecasts aren't enough for the restaurant industry. Demand spikes happen in 15-minute rushes. Our engine breaks down your daily forecast into 15-minute intervals, ensuring you schedule the exact right number of stations during the lunch rush without paying for idle time at 3 PM.",
        "dd1_li1": "Item-level forecasting (predicting specific prep needed)", "dd1_li2": "Integration with historic POS receipt data", "dd1_li3": "Dynamic labor standard matching", "dd1_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        
        "dd2_h2": "Automated Schedule Generation", "dd2_p": "Once the forecast is locked, let the engine build the schedule. Altametrics uses your predefined labor matrices, employee availability, and state labor compliance rules to spit out a 90% complete, fully-optimized schedule in seconds.",
        "dd2_li1": "Respects employee time-off requests", "dd2_li2": "Balances skills matrix for specific stations", "dd2_li3": "Highlights projected vs actual labor costs instantly", "dd2_img": "https://images.unsplash.com/photo-1552664730-d307ca884978",
        
        "role1_desc": "Spend 5 minutes reviewing and adjusting algorithmic schedules instead of 4 hours building them from scratch every Thursday.",
        "role2_desc": "Get a portfolio-wide view of forecast accuracy vs actuals across regions to identify poorly predicting locations before they eat into margins.",
        
        "quote": "Our labor cost percentage dropped by 2.4% within three months of switching to Altametrics AI Forecasting. It literally paid for the entire platform in Q1.",
        "author": "VP of Operations", "brand": "Global QSR Chain",
        
        "faq1_q": "How much historical data does the AI need?", "faq1_a": "The model functions best with at least 13 months of historical POS data to establish year-over-year seasonality, but it can begin providing valuable exponential smoothing forecasts with just 4-6 weeks of baseline data.",
        "faq2_q": "Can managers override the AI forecast?", "faq2_a": "Yes. While the AI generates the baseline, authorized managers can manually adjust the forecast up or down by a percentage or dollar amount to account for local knowledge the AI wouldn't possess.",
        "faq3_q": "Does it forecast items sold or just revenue?", "faq3_a": "Both. Depending on your configuration, Altametrics tracks projected revenue, guest counts, and specific menu item mix (highly useful for kitchen prep planning)."
    },
    
    "compliance": {
        "title": "Labor Law Compliance", "cat": "Workforce Suite",
        "hero_h1": "Bulletproof Your <br><span class=\"text-gradient\">Labor Compliance</span>",
        "hero_desc": "Navigate the complex web of Fair Workweek laws, predictive scheduling regulations, and complex overtime rules without the legal anxiety. We automate the rulebook.",
        "hero_image": "https://images.unsplash.com/photo-1573164713988-8665fc963095",
        
        "b1_icon": "⚖️", "b1_title": "Built-In State Rules", "b1_desc": "Automatically apply hyper-specific labor rules for jurisdictions like California, New York, and Oregon natively into the scheduling engine.",
        "b2_icon": "🛑", "b2_title": "Pre-Shift Blockers", "b2_desc": "Prevent managers from finalizing schedules that incur meal break penalties, clopening violations, or unauthorized overtime.",
        "b3_icon": "📑", "b3_title": "Audit-Ready Logs", "b3_desc": "Maintain permanent digital records of employee shift acceptances, waiver signatures, and schedule change consent.",
        
        "uc1_challenge": "Managers accidentally schedule employees back-to-back late night then early morning (Clopenings), incurring premium pay penalties.",
        "uc1_solution": "The scheduler strictly enforces required rest periods, physically blocking the manager from saving the shift without overriding with recorded employee consent.",
        "uc2_challenge": "Handling predictive scheduling penalty pay when cutting employees early due to slow traffic.",
        "uc2_solution": "The time clock interface automatically calculates and logs Good Faith Estimate penalty premiums if a shift is altered inside the legal window.",
        
        "dd1_h2": "Fair Workweek Automation", "dd1_p": "For multi-state chains, Fair Workweek regulations are a massive liability. Altametrics simplifies this by automating Good Faith Estimates, tracking voluntary standby lists, and requiring electronic employee sign-off for last-minute shift changes right inside the employee mobile app.",
        "dd1_li1": "Digital shift-offer broadcasting", "dd1_li2": "Consent logging mechanism", "dd1_li3": "Automated penalty tracking", "dd1_img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
        
        "dd2_h2": "Minor & Teen Labor Controls", "dd2_p": "Ensure you never violate strict minor labor laws. The system tracks employee ages dynamically, enforcing strict cut-off times during school nights, limiting maximum weekly hours, and requiring mandated breaks exactly according to state-by-state education codes.",
        "dd2_li1": "School-calendar syncing integration", "dd2_li2": "Hard-stops on POS timeclocks", "dd2_li3": "Automated aging-up triggers", "dd2_img": "https://images.unsplash.com/photo-1623039405147-547794f92e9e",
        
        "role1_desc": "Build schedules confidently knowing the system won't let you accidentally break the law or incur unapproved overtime.",
        "role2_desc": "Rest easy with centralized, tamper-proof compliance dashboards indicating audit-readiness across the entire restaurant group.",
        
        "quote": "Operating in California and Seattle was a compliance nightmare until we rolled out Altametrics. Our premium penalty payouts decreased by 85%.",
        "author": "Chief Human Resources Officer", "brand": "West Coast Dining Group",
        
        "faq1_q": "How often are the labor laws updated in your system?", "faq1_a": "Our dedicated compliance team continuously monitors federal, state, and local ordinances, pushing logic updates to the platform quarterly or ahead of major municipal legal changes.",
        "faq2_q": "Does this replace my HRIS system?", "faq2_a": "No, Altametrics integrates with your HRIS (like Workday or ADP) to pull in employee roles, pay rates, and ages, using that data to enforce operational time and attendance compliance on the floor.",
        "faq3_q": "Can employees waive their breaks?", "faq3_a": "Yes, where legally permitted, the platform facilitates digital employee break waivers that are logged securely to protect the employer during labor audits."
    },
    
    "mobile-app": {
        "title": "Employee Mobile App", "cat": "Workforce Suite",
        "hero_h1": "Empower Teams with a <br><span class=\"text-gradient\">Unified Mobile Hub</span>",
        "hero_desc": "Give your hourly workforce the ultimate self-service tool. Handle shift swaps, time-off requests, messaging, and digital onboarding from an app they actually want to use.",
        "hero_image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c",
        
        "b1_icon": "📱", "b1_title": "Native iOS & Android", "b1_desc": "A fast, intuitive, natively built mobile experience available on all major app stores with biometric login support.",
        "b2_icon": "🔄", "b2_title": "Seamless Shift Swapping", "b2_desc": "Employees can drop, offer, and pick up shifts directly. Managers just tap 'Approve'.",
        "b3_icon": "💬", "b3_title": "Secure Team Comms", "b3_desc": "Eliminate chaotic group chats. Keep work communications professional, auditable, and off personal WhatsApp threads.",
        
        "uc1_challenge": "A line cook calls out sick at 6 AM, forcing the GM to spend two hours calling off-duty staff.",
        "uc1_solution": "The GM broadcasts an 'Open Shift' alert via push notification to all eligible cooks. An employee claims it in 30 seconds.",
        "uc2_challenge": "Employees constantly texting managers asking 'When do I work next?'",
        "uc2_solution": "Schedules automatically sync to the app calendar and their personal iPhone calendars with shift reminders.",
        
        "dd1_h2": "Centralized Team Communication", "dd1_p": "Communicate announcements, health policies, and shift updates instantly. Create role-based channels (e.g., 'Bartenders Only') to ensure messages are relevant. Read-receipts guarantee managers know exactly who has seen critical operational updates.",
        "dd1_li1": "Broadcast push notifications", "dd1_li2": "1-on-1 direct manager messaging", "dd1_li3": "Company-wide document sharing", "dd1_img": "https://images.unsplash.com/photo-1552664730-d307ca884978",
        
        "dd2_h2": "Self-Service Availability & PTO", "dd2_p": "Shift the administrative burden onto the staff. Employees submit recurring availability, block out specific school/vacation days, and request PTO directly in the app. The scheduling engine automatically factors this in, preventing managers from scheduling unavailable staff.",
        "dd2_li1": "Real-time PTO balance viewing", "dd2_li2": "Manager push-notification approvals", "dd2_li3": "Availability blackout periods", "dd2_img": "https://images.unsplash.com/photo-1581244277943-fe4a9c777189",
        
        "role1_desc": "View your upcoming shifts, swap with coworkers securely, and request time off without having to hunt down the GM in the office.",
        "role2_desc": "Drastically reduce administrative phone calls and text messages, keeping personal boundaries intact while ensuring the store is staffed.",
        
        "quote": "Our employee retention increased simply because the staff loved the transparency of the app. Shift swaps that used to take days of texting are now handled in five minutes.",
        "author": "Director of Technology", "brand": "National Coffee Chain",
        
        "faq1_q": "Do employees have to pay for the app?", "faq1_a": "No, the Altametrics eRestaurant Team app is completely free to download for employees as part of your corporate software license.",
        "faq2_q": "Can managers clock people in from the app?", "faq2_a": "Yes! With geo-fencing enabled, managers can allow approved staff to clock in remotely, or use the app as a secure manager portal to override missing punches from the floor.",
        "faq3_q": "Is the messaging feature compliant with labor laws?", "faq3_a": "Yes, to prevent 'off-the-clock' work claims, corporate can configure the app to restrict hourly employees from sending or receiving work messages when they are not physically clocked in."
    },
    
    "payroll": {
        "title": "Payroll & Tips", "cat": "Workforce Suite",
        "hero_h1": "Streamline Your <br><span class=\"text-gradient\">Tip & Payroll Exports</span>",
        "hero_desc": "Eliminate spreadsheet math. Automate complex weekly tip pooling, TRAC compliance, and direct-to-payroll data exports seamlessly without manual data entry.",
        "hero_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        
        "b1_icon": "💰", "b1_title": "Complex Tip Pooling", "b1_desc": "Handle any distribution model: points-based, percentage of sales, zone-based, or customized hierarchical tip sharing.",
        "b2_icon": "🔗", "b2_title": "Direct Payroll Sync", "b2_desc": "Generate formatted flat-files that natively upload or API-sync directly to ADP, Paycor, Paylocity, and Gusto.",
        "b3_icon": "✅", "b3_title": "Daily Tip Automation", "b3_desc": "Calculate shiftly tip-outs for digital paycards to meet the modern demand for instant employee access to earnings.",
        
        "uc1_challenge": "A restaurant assigns 2% of food sales to bussers, 4% of alcohol to bartenders, and splits the rest among servers based on hours worked.",
        "uc1_solution": "Altametrics pulls category sales from the POS, applies the custom math matrix automatically, and allocates exact dollar amounts to each clocked-in employee.",
        "uc2_challenge": "Entering 140 employee hours into ADP manually every Monday morning taking 6 hours of admin time.",
        "uc2_solution": "Click 'Export to Payroll'—Altametrics packages standard, OT, penalty, and tip hours into an exact ADP-formatted CSV.",
        
        "dd1_h2": "IRS TRAC Compliance", "dd1_p": "Ensure you never run afoul of the IRS. The system automatically tracks declared cash tips vs credit tips, enforcing minimum threshold declarations (like 8%) to guarantee compliance with the Tip Reporting Alternative Commitment (TRAC).",
        "dd1_li1": "Automated shortfall detection", "dd1_li2": "Manager tip-declaration overrides", "dd1_li3": "Audit-proof historical reporting", "dd1_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        
        "dd2_h2": "Multi-Role Pay Rates", "dd2_p": "In a restaurant, an employee might work as a host on Tuesday at $15/hr and a server on Friday at $8/hr. The timeclock and payroll exporter automatically separate these distinct labor codes, calculating correct blended overtime rates per federal FLSA guidelines.",
        "dd2_li1": "Weighted average overtime calculation", "dd2_li2": "Automatic role-based rate fetching", "dd2_li3": "Cross-store borrowed employee pay tracking", "dd2_img": "https://images.unsplash.com/photo-1554224154-26032ffc0d07",
        
        "role1_desc": "Spend your Monday mornings managing your restaurant, not hunched over an Excel sheet trying to calculate who worked the patio section.",
        "role2_desc": "Process portfolio-wide payroll reliably with standardized tip rules that eliminate individual store manager calculation errors.",
        
        "quote": "Calculating our massive multi-tier tip pool used to take 4 hours every Sunday night. Altametrics does it accurately in about 3 seconds.",
        "author": "Controller", "brand": "High-Volume Steakhouse Group",
        
        "faq1_q": "Does Altametrics process the actual paychecks?", "faq1_a": "No, Altametrics acts as the Time & Attendance 'Source of Truth'. We calculate the exact hours, compliance pay, and tips, and push that perfect data to your dedicated payroll provider to cut the checks.",
        "faq2_q": "Can you handle different tip pools for AM and PM shifts?", "faq2_a": "Absolutely. Our rules engine is robust enough to separate breakfast, lunch, and dinner day-parts, ensuring tips generated during a lunch rush aren't distributed to evening staff.",
        "faq3_q": "What payroll software do you integrate with?", "faq3_a": "We have standardized integrations for over 40 major HRIS/Payroll systems including ADP, Paychex, Paylocity, SAP, Workday, and more."
    },
    
    # ------------------ INVENTORY ------------------
    "waste-reduction": {
        "title": "Waste Reduction & Tracking", "cat": "Inventory Suite",
        "hero_h1": "Trace Every Ounce, <br><span class=\"text-gradient\">Eliminate Food Waste</span>",
        "hero_desc": "Stop throwing profits in the trash. Digitally log yields, spoilage, and operational mistakes to pinpoint exactly where you are losing product margin.",
        "hero_image": "https://images.unsplash.com/photo-1556910103-1c02745aae4d",
        
        "b1_icon": "🗑️", "b1_title": "Digital Waste Logs", "b1_desc": "Log dropped items, expired product, and prep spoilage on a tablet instantly without paper logs.",
        "b2_icon": "🔍", "b2_title": "Root Cause Tracking", "b2_desc": "Categorize waste by reason (burnt, dropped, expired) to identify training gaps vs supplier issues.",
        "b3_icon": "📊", "b3_title": "Actual vs Theoretical", "b3_desc": "Compare what your POS says you sold against what you actually consumed to measure hidden variance.",
        
        "uc1_challenge": "Managers find a 5% variance in cheese inventory but have no idea if it was over-portioned on pizzas or thrown away spoiled.",
        "uc1_solution": "Mandatory digital waste tracking separates 'Known Waste' from 'Unknown Variance', allowing operators to fix specific portioning issues.",
        "uc2_challenge": "Paper waste logs are illegible, falsified, or lost before accounting can review them.",
        "uc2_solution": "Cloud-based tracking instantly hits the General Ledger the moment a manager logs a spoilt case of tomatoes on the kitchen tablet.",
        
        "dd1_h2": "Yield & Trim Tracking", "dd1_p": "For concepts doing from-scratch prep, understanding yield is critical. If your butcher receives a 10lb primal cut and trims away 3lbs of fat, Altametrics tracks the yield percentage. If your yield suddenly drops to 60%, the system alerts you to poor kitchen knife skills or sub-par vendor product.",
        "dd1_li1": "Customizable yield recipes", "dd1_li2": "Vendor quality flagging", "dd1_li3": "Batch prep variance alerts", "dd1_img": "https://images.unsplash.com/photo-1507048331197-7d4ac70811cf",
        
        "dd2_h2": "Automated Reversal & Impact Analysis", "dd2_p": "When a manager logs a burnt steak as waste, the system does more than just record it. It instantly depletes the actual inventory stock on hand and updates real-time Daily Food Cost models so the GM knows they are $40 behind margin targets for the shift.",
        "dd2_li1": "Real-time inventory depletion", "dd2_li2": "Financial GL impact journal entries", "dd2_li3": "Shiftly margin-loss reporting", "dd2_img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc",
        
        "role1_desc": "A fast, 3-tap interface on the kitchen tablet to declare waste during a busy rush without holding up the line.",
        "role2_desc": "Analyze portfolio-wide waste trends to determine if a specific LTO product is spoiling too universally across the brand.",
        
        "quote": "By moving to digital waste logs and tracking Actual vs Theoretical, we identified a massive over-portioning issue in our fry stations that saved us $2M annually across our fleet.",
        "author": "Director of Culinary Operations", "brand": "Casual Dining Franchise",
        
        "faq1_q": "Does tracking waste actually save money?", "faq1_a": "Yes. While it doesn't retrieve the lost product, categorizing waste shifts the focus from 'mysterious loss' to actionable training. You can't fix what you can't measure.",
        "faq2_q": "Can it integrate with kitchen displays?", "faq2_a": "Yes, many modern KDS integrations allow operators to flag an item as 'remake/dropped' directly on the screen, instantly feeding Altametrics the waste data.",
        "faq3_q": "How does it handle liquids like bar spills?", "faq3_a": "The system interfaces perfectly with bar metrics. Bartenders can log spillage by the ounce or milliliter, which accurately depletes the liquor bottle inventory."
    },
    
    "purchasing": {
        "title": "Automated Purchasing", "cat": "Inventory Suite",
        "hero_h1": "Centralize Your <br><span class=\"text-gradient\">Vendor Supply Chain</span>",
        "hero_desc": "Take control of your exact food costs. Automate suggested ordering, centralize vendor catalogs, and enforce strict corporate purchasing contracts across every location.",
        "hero_image": "https://images.unsplash.com/photo-1586880244406-556ebe35f282",
        
        "b1_icon": "🛒", "b1_title": "Suggested Orders", "b1_desc": "AI calculates exactly what you need to order based on on-hand stock, par levels, and projected weekend sales.",
        "b2_icon": "📑", "b2_title": "EDI Vendor Integrations", "b2_desc": "Push electronic purchase orders directly to Sysco, US Foods, Gordon Food Service and receive electronic invoices back.",
        "b3_icon": "🔒", "b3_title": "Maverick Spend Control", "b3_desc": "Lock down order guides so managers can only purchase approved products from approved vendors at contracted prices.",
        
        "uc1_challenge": "Managers spend 4 hours a week manually browsing vendor websites and over-ordering 'just in case'.",
        "uc1_solution": "The 'Suggested Order' button compiles a perfect PO in seconds. The manager reviews, clicks approve, and it sends instantly.",
        "uc2_challenge": "A vendor sneaks a 5% price increase onto an invoice, and store managers don't notice it during receiving.",
        "uc2_solution": "Invoice Price Variance alerts flag accounting immediately if an invoice line-item exceeds the corporately contracted price.",
        
        "dd1_h2": "Electronic Data Interchange (EDI)", "dd1_p": "Stop maintaining paper invoices. We pipe directly into all major broadline distributor back-ends. The moment an order is placed, an EDI PO is sent. When the truck arrives, the electronic invoice is automatically waiting in the system for the manager to verify against the physical goods.",
        "dd1_li1": "Zero-touch invoice ingestion", "dd1_li2": "Catch-weight updating", "dd1_li3": "Automated routing to Accounts Payable", "dd1_img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
        
        "dd2_h2": "Cross-Store Inventory Transfers", "dd2_p": "For operators with multiple locations in a tight geographic radius, Altametrics facilitates digital warehouse transfers. Instead of buying an expensive emergency case of cups from a broadliner, Store A can digitally request and transfer cups from Store B, keeping inventory valuations perfectly balanced.",
        "dd2_li1": "Digital request & approval workflows", "dd2_li2": "Automatic GL offsetting entries", "dd2_li3": "Commissary kitchen support", "dd2_img": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1",
        
        "role1_desc": "Never miss an order cutoff. Review AI-suggested quantities on a tablet while walking the walk-in cooler.",
        "role2_desc": "Negotiate better vendor rebates by proving exact volume compliance and eliminating off-contract maverick spending at the store level.",
        
        "quote": "Our supply chain was fragmented. Altametrics centralized our catalog, locked down maverick spend, and reduced our overall food cost by 3% simply by enforcing vendor contracts.",
        "author": "VP of Supply Chain", "brand": "National Taco Concept",
        
        "faq1_q": "Does this work with local/specialty vendors?", "faq1_a": "Yes. While major broadliners use EDI, managers can still generate standard digital POs in the system that are emailed directly to local bakeries or produce vendors.",
        "faq2_q": "Can it account for fluctuating par levels?", "faq2_a": "Absolutely. The system uses dynamic par levels tied to the AI demand forecast, ensuring you order more buns for a busy holiday weekend than a slow Tuesday.",
        "faq3_q": "How does receiving work on the tablet?", "faq3_a": "Managers view the digital PO on their tablet when the truck arrives. They can 'short' items if the vendor missed something, updating the invoice liability in real-time."
    },
    
    "recipe-costing": {
        "title": "Dynamic Recipe Costing", "cat": "Inventory Suite",
        "hero_h1": "Engineer a  <br><span class=\"text-gradient\">More Profitable Menu</span>",
        "hero_desc": "Instantly see how fluctuating supply chain costs impact your bottom line. Altametrics connects real-time vendor invoice prices to your exact recipe builds.",
        "hero_image": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1",
        
        "b1_icon": "🍲", "b1_title": "Sub-Recipe Mapping", "b1_desc": "Build batch recipes (e.g., pizza dough) that act as single ingredients inside master plate recipes.",
        "b2_icon": "📈", "b2_title": "Live Margin Tracking", "b2_desc": "If the price of beef jumps 10% on today's invoice, your burger plate cost updates instantly across all reports.",
        "b3_icon": "🧾", "b3_title": "Menu Engineering", "b3_desc": "Map sales mix velocity against plate margins to identify your 'Stars', 'Plowhorses', and 'Dogs'.",
        
        "uc1_challenge": "Corporate chefs rely on Excel spreadsheets that use outdated 6-month-old meat prices to cost out the menu.",
        "uc1_solution": "Altametrics dynamically ties the recipe ingredient cost directly to the most recent EDI invoice cost, keeping margins hyper-accurate.",
        "uc2_challenge": "Trying to determine if raising the price of a chicken sandwich will offset the rising cost of cooking oil.",
        "uc2_solution": "Use the 'What-If' modeling dashboard to simulate menu price increases and project the exact impact on gross profit.",
        
        "dd1_h2": "Allergen & Nutritional Tracking", "dd1_p": "Recipes aren't just for accounting. Attach mandatory nutritional values, caloric counts, and allergen tags (Gluten, Dairy, Nuts) to ingredients. When recipes are assembled, the system calculates the master plate nutritional profile to ensure legal compliance on your menu boards.",
        "dd1_li1": "USDA database integrations", "dd1_li2": "Automated macro-nutrient totals", "dd1_li3": "Crucial food safety filtering", "dd1_img": "https://images.unsplash.com/photo-1514933651103-005eec06c04b",
        
        "dd2_h2": "Actual vs Theoretical (AvT) Analysis", "dd2_p": "Perfect recipe costing is the engine behind AvT. By knowing exactly that a burger uses 1 bun, 4oz of beef, and 1oz of cheese, Altametrics compares those theoretical ideals against the POS sales mix. The variance gap reveals exact portioning issues and staff theft.",
        "dd2_li1": "Pinpoint over-portioning habits", "dd2_li2": "Identify high-theft items", "dd2_li3": "Calculate hidden margin loss daily", "dd2_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        
        "role1_desc": "Print out beautifully formatted, highly accurate prep-recipe cards with photos to ensure back-of-house consistency.",
        "role2_desc": "Execute highly strategic menu price increases based on hard, real-time commodity data rather than gut feelings.",
        
        "quote": "We realized we were losing 40 cents on every salmon dish we sold because our manual Excel costing hadn't updated to reflect massive supply chain inflation. Implementing live costing saved our Q3 margins.",
        "author": "Executive Chef", "brand": "Upscale Dining Portfolio",
        
        "faq1_q": "How long does it take to input all our recipes?", "faq1_a": "Our onboarding team handles the heavy lifting via bulk spreadsheet imports. We can usually parse and upload your entire cookbook during the first 30 days.",
        "faq2_q": "What happens when an item has different yields based on prep?", "faq2_a": "The system features advanced yield modeling. You buy a 10lb whole fish, but specify a 60% yield for the fillets, ensuring the cost-per-ounce is weighted correctly for the edible portion.",
        "faq3_q": "Can recipes vary by location?", "faq3_a": "Yes. While you can maintain an enterprise master recipe, you can allow regional substitutions (e.g., using regional sourdough bread in SF vs LA) that accurately reflect localized COGS."
    },
    
    "prep-planning": {
        "title": "Smart Prep Planning", "cat": "Inventory Suite",
        "hero_h1": "Never Run Out, <br><span class=\"text-gradient\">Never Over-Prep</span>",
        "hero_desc": "Connect your daily demand forecasts directly to the prep table. Generate dynamic kitchen workflows to ensure the exact right amount of food is ready for the rush.",
        "hero_image": "https://images.unsplash.com/photo-1507048331197-7d4ac70811cf",
        
        "b1_icon": "🔪", "b1_title": "Demand-Driven Quantities", "b1_desc": "If the AI predicts 400 burgers will sell tomorrow, the system tells the prep cook exactly how many tomatoes to slice today.",
        "b2_icon": "⏱️", "b2_title": "Shelf-Life Tracking", "b2_desc": "Factor in expiration times. Don't prep a 3-day supply of guacamole if it turns brown in 24 hours.",
        "b3_icon": "📋", "b3_title": "Digital Kitchen Worklists", "b3_desc": "Replace whiteboards with digital tablets guiding prep cooks step-by-step through their shift priorities.",
        
        "uc1_challenge": "Kitchen staff preps the exact same amount of food every Tuesday, regardless of a massive local holiday parade.",
        "uc1_solution": "The dynamic prep sheet scales up tomato slicing and dough tossing automatically based on the AI's elevated traffic forecast.",
        "uc2_challenge": "Running out of signature sauce at 6 PM on a Friday because the AM prep cook got distracted.",
        "uc2_solution": "Digital task tracking requires the AM cook to 'check off' the sauce prep, alerting management if it falls behind schedule.",
        
        "dd1_h2": "Just-In-Time Prep Scheduling", "dd1_p": "Food quality is everything. Altametrics allows you to schedule intraday prep. Instead of slicing all lettuce at 8 AM and letting it wilt by dinner, the system schedules a morning prep block and an afternoon refresh block based on calculated velocity.",
        "dd1_li1": "Intra-day freshness optimization", "dd1_li2": "Reduces total spoilage waste", "dd1_li3": "Balances kitchen workloads", "dd1_img": "https://images.unsplash.com/photo-1556910103-1c02745aae4d",
        
        "dd2_h2": "Ingredient Roll-up Logic", "dd2_p": "If your menu has 12 different items that use diced onions, the system automatically looks at the forecasted sales for all 12 items, calculates the sub-recipe onion requirements for each, and rolls them up into one unified 'Diced Onion' task for the prep cook.",
        "dd2_li1": "Cross-menu aggregation", "dd2_li2": "Saves hours of manager math", "dd2_li3": "Accounts for existing on-hand stock", "dd2_img": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1",
        
        "role1_desc": "Empower your BOH staff to come in, look at the tablet, and know exactly what to cut, cook, and cool without manager intervention.",
        "role2_desc": "Verify that recipe quality and freshness standards are being maintained across hundreds of franchised locations.",
        
        "quote": "Over-prepping was costing us thousands in wasted food, and under-prepping was causing 86'd items and angry guests. Smart Prep brought our line into perfect equilibrium.",
        "author": "Kitchen Manager", "brand": "High-Volume Brewery",
        
        "faq1_q": "Does prep planning run on tablets?", "faq1_a": "Yes! The entire Prep UI is designed for rugged kitchen tablets, featuring large touch targets and dark-modes suitable for the line.",
        "faq2_q": "Does it connect to label printers?", "faq2_a": "Yes, once a prep task is completed on the tablet, the system can automatically print a Food Safety 'Use By' label via networked Bluetooth printers.",
        "faq3_q": "What happens if we already have prepped food left over?", "faq3_a": "The manager inputs the 'Current On-Hand' prepped levels in the morning. The system subtracts that from the total required, ensuring you only prep the Delta."
    }
}

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
    
    return navbar, footer

def update_templates():
    navbar, footer = extract_globals()
    for slug, data in PAGES.items():
        base = TEMPLATE
        
        # Inject Navbar and Footer
        base = base.replace('<!--NAVBAR_PLACEHOLDER-->', navbar)
        base = base.replace('<!--FOOTER_PLACEHOLDER-->', footer)
        
        # We replace specific keys
        for key, value in data.items():
            base = base.replace(f"{{{key}}}", value)
            
        # Fix the python escaping issue and convert back to regular CSS brackets
        base = base.replace('{{', '{').replace('}}', '}')
            
        with open(f"{slug}.html", 'w', encoding='utf-8') as f:
            f.write(base)
            
    print(f"Generated {len(PAGES)} highly unique pages for Batch 1.")

if __name__ == "__main__":
    update_templates()
