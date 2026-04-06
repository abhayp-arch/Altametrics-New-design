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

PAGES = {
    # ------------------ The remaining pages ------------------
    "loss-prevention": {
         "title": "Exception & Loss Prevention", "cat": "Reporting Suite",
         "hero_h1": "Detect Staff Theft <br><span class=\"text-gradient\">Before It Escapes the Building</span>",
         "hero_desc": "Altametrics automatically flags anomalous voids, extreme discounts, and suspicious employee activity that historically hides deep inside massive end-of-day POS printouts.",
         "hero_image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
         "b1_icon": "🛑", "b1_title": "Void Heatmaps", "b1_desc": "Identify exactly which servers are executing extreme amounts of voids compared to their store peers.",
         "b2_icon": "🧾", "b2_title": "Sweet-Hearting Alerts", "b2_desc": "Identify recurring unauthorized 100% comps being given to 'friends and family'.",
         "b3_icon": "🎥", "b3_title": "Video POS Sync", "b3_desc": "Connect standard POS receipt timestamps natively to back-of-house IP security camera playback.",
         "uc1_challenge": "A bartender is handing out free top-shelf drinks by voiding them after the drink is poured.",
         "uc1_solution": "The LP Engine flags the bartender's 'Void Percentage vs Shift Sales' as an anomaly, triggering an automatic DM alert.",
         "uc2_challenge": "Manager investigates a cash shortage on a drawer, but has to manually rewind hours of blurry CCTV footage.",
         "uc2_solution": "The system overlays POS ticket data onto the video feed itself. Clicking a flagged void jumps the security feed directly to that exact millisecond.",
         "dd1_h2": "Automated Exception Rules Engine", "dd1_p": "You don't have to hunt for the needle in the haystack. The haystack finds you. Configure rules like 'Alert if an employee performs 3 voids within 10 minutes' or 'Alert if a manager comps more than $100 in a single shift'. Violations are compiled into a morning risk digest.",
         "dd1_li1": "Zero-configuration AI anomaly flags", "dd1_li2": "Customizable strict rule thresholds", "dd1_li3": "Cross-store employee benchmarking", "dd1_img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
         "dd2_h2": "Cash Drawer Reconciliation Audits", "dd2_p": "Loss prevention isn't just about catching staff; it's about holding managers accountable. The dashboard highlights every single 'No Sale' till opening, tracking how often managers are popping safe drawers independent of POS transactions.",
         "dd2_li1": "Tracks unlinked 'No Sale' operations", "dd2_li2": "Audits manager-override codes", "dd2_li3": "Automated safe-balance warnings", "dd2_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
         "role1_desc": "Understand exactly which cashiers need retraining on the POS vs which ones are intentionally gaming the system.",
         "role2_desc": "Save millions of dollars annually in untracked shrinkage that would otherwise be permanently lost.",
         "quote": "Within our first 30 days of turning on the exception alerts, we identified systemic coupon fraud occurring across five stores. Catching that one exploit justified the entire software contract.",
         "author": "Director of Asset Protection", "brand": "Global Fast Food Franchise",
         "faq1_q": "Do we need specific cameras?", "faq1_a": "Our POS-video sync integrates with major enterprise VMS (Video Management Systems) like Envysion and March Networks.",
         "faq2_q": "Does this require constant monitoring?", "faq2_a": "No, the entire point is exception-based management. You only look at the data when the AI emails you a specific flagged incident.",
         "faq3_q": "Can it detect time-clock fraud?", "faq3_a": "Yes, 'Buddy Punching' alerts trigger if two employees clock in within incredibly tight windows of each other while manager override thresholds are simultaneously breached."
    },

    "ai-insights": {
         "title": "Predictive AI Insights", "cat": "Reporting Suite",
         "hero_h1": "Stop the Autopsy, <br><span class=\"text-gradient\">Start the Prediction</span>",
         "hero_desc": "Move from answering 'What happened?' to 'What is *going* to happen?' Altametrics uses vast machine learning capabilities to simulate operational outcomes and suggest prescriptive actions.",
         "hero_image": "https://images.unsplash.com/photo-1518770660439-4636190af475",
         "b1_icon": "🧠", "b1_title": "Prescriptive Prompts", "b1_desc": "Instead of a chart showing high labor, the AI prompts: 'Cut 2 servers in Store #14 immediately.'",
         "b2_icon": "🔮", "b2_title": "Revenue Modeling", "b2_desc": "Simulate what happens to overall Gross Profit if you raise the cost of your flagship burger by $0.50.",
         "b3_icon": "💬", "b3_title": "Natural Language Query", "b3_desc": "Ask the system questions in plain English: 'Which store sold the most coffee yesterday?'",
         "uc1_challenge": "A CFO spends hours modeling different commodity inflation scenarios in Excel.",
         "uc1_solution": "The AI instantly simulates a 10% hike in poultry costs across the entire menu matrix, advising on optimized menu price offsets.",
         "uc2_challenge": "A GM logs in and is overwhelmed by 30 different complex dashboards.",
         "uc2_solution": "The 'Smart Morning Brief' synthesizes all dashboards into three bullet points: \"Prep extra fries, watch overtime for John, check your chicken freezer.\"",
         "dd1_h2": "Turnover Prediction Engine", "dd1_p": "The cost of replacing a trained cook is massive. Our AI analyzes subtle indicators—missed clock-ins, reduced requested hours, stagnant wage growth—and flags employees at high risk of quitting, giving managers a chance to intervene.",
         "dd1_li1": "Flight-risk employee flagging", "dd1_li2": "Burnout detection based on scheduled OT", "dd1_li3": "Actionable retention suggestions", "dd1_img": "https://images.unsplash.com/photo-1554224154-26032ffc0d07",
         "dd2_h2": "Conversational Interface (Copilot)", "dd2_p": "You don't need to learn a complex filtering language. Just type into the search bar: \"Show me the labor variance for all Texas locations against last year.\" The AI translates the English intent into a complex SQL query, instantly generating a graph.",
         "dd2_li1": "Plain-English semantic searches", "dd2_li2": "Automated ad-hoc graph generation", "dd2_li3": "Cross-references disparate datasets effortlessly", "dd2_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
         "role1_desc": "Have a digital assistant essentially tell you what your operational priorities need to be the moment you step foot in the building.",
         "role2_desc": "Uncover multidimensional correlations (e.g., weather + sports events + specific coupon drops) that human analysts could never spot.",
         "quote": "The predictive insights tool is like having a Wharton data scientist sitting in the back office of every single one of our 150 stores.",
         "author": "Chief Information Officer", "brand": "National Family Dining Brand",
         "faq1_q": "Is the AI learning from my competitors?", "faq1_a": "No, your data is securely siloed. However, the machine learning architecture (the weights and model structures) benefits from generalized industry-scale training.",
         "faq2_q": "Can the AI execute actions automatically?", "faq2_a": "We maintain a 'human in the loop' philosophy. The AI prescribes the optimal action (like suggesting a vendor PO), but a recognized manager must ultimately approve the execution.",
         "faq3_q": "Do I need a data science team to use this?", "faq3_a": "Not at all. The interface is designed specifically for restaurant operators with zero technical background, abstracting the complex data modeling away entirely."
    },

    "general-ledger": {
         "title": "Unified General Ledger", "cat": "Accounting Suite",
         "hero_h1": "The Ultimate <br><span class=\"text-gradient\">Source of Financial Truth</span>",
         "hero_desc": "Bridge the gap between restaurant operations and corporate finance. Altametrics acts as the master unified ledger, recording every transaction, transfer, and void as a GAAP-compliant journal entry.",
         "hero_image": "https://images.unsplash.com/photo-1554224154-26032ffc0d07",
         "b1_icon": "📚", "b1_title": "Continuous Close", "b1_desc": "Stop waiting for month-end. View your estimated P&Ls at any hour of any day based on live operational accruals.",
         "b2_icon": "🔀", "b2_title": "Multi-Entity Rollups", "b2_desc": "Consolidate financials across complex franchise matrixes, multiple LLCs, and diverse restaurant concepts flawlessly.",
         "b3_icon": "⚖️", "b3_title": "Automated Depletion", "b3_desc": "When a physical item is sold, the corresponding COGS account is instantly debited without manual batch entries.",
         "uc1_challenge": "Accountants manually calculate and accrue for utilities and payroll during the frustrating gap between month-end and invoice receipt.",
         "uc1_solution": "The system automatically books reversing accruals based on standard historical costs or scheduled hours worked.",
         "uc2_challenge": "The operations team and the finance team argue over the 'real' food cost percentage because they use different software.",
         "uc2_solution": "Because Operations uses Altametrics for Inventory, and Finance pulls the GL out of Altametrics, the numbers match to the penny.",
         "dd1_h2": "Franchise Royalty Deductions", "dd1_p": "If you are managing franchisees or hold multiple corporate brands, cross-entity accounting is a massive headache. Altametrics automatically calculates royalty percentages, management fees, and advertising fund contributions natively directly off the incoming POS revenue stream, posting the intercompany journal entries immediately.",
         "dd1_li1": "Customized tier-based percentage rules", "dd1_li2": "Automated intercompany billing", "dd1_li3": "Instant compliance reporting", "dd1_img": "https://images.unsplash.com/photo-1601597111158-2fceff292cdc",
         "dd2_h2": "Seamless Financial Software Export", "dd2_p": "We don't trap your data. Whether you run a simple QuickBooks setup for three stores, or an Oracle NetSuite environment for 3,000, our API and custom flat-file engines push perfectly formatted GL codes exactly the way your enterprise accounting system requires them.",
         "dd2_li1": "Native NetSuite, Sage, & MS Dynamics integrations", "dd2_li2": "Customizable GL code mapping tables", "dd2_li3": "Automated daily syncs", "dd2_img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
         "role1_desc": "Focus on driving top-line sales, confident that the software is handling the tedious accounting mapping behind the scenes.",
         "role2_desc": "Close out your financial periods on Day 3 instead of Day 15, pleasing investors and reducing back-office burnout.",
         "quote": "Moving to a unified platform meant our Ops and Finance teams were finally speaking the same language. It cut our month-end close cycle by over a week.",
         "author": "Corporate Controller", "brand": "Leading Dessert Franchise",
         "faq1_q": "Does Altametrics replace my accounting software?", "faq1_a": "No, it acts as an 'Integration and Operations Hub'. Altametrics handles the complex, messy restaurant-specific data (recipes, schedules, invoices) and pushes clean, summarized journal entries into your dedicated accounting software.",
         "faq2_q": "Can I map different POS systems to the same GL?", "faq2_a": "Yes! If you acquired a new brand using Micros, but your core brand uses Toast, Altametrics normalizes both data streams into the exact same standardized GL Chart of Accounts for corporate.",
         "faq3_q": "How does it handle sales tax complexities?", "faq3_a": "The system parses item-level tax details directly from the POS, routing the correct state, local, and beverage tax liabilities into separate highly-auditable accounts automatically."
    },

    "inventory-sync": {
         "title": "Real-Time Inventory Sync", "cat": "Accounting Suite",
         "hero_h1": "Bridge the Gap Between <br><span class=\"text-gradient\">Kitchen and Accounting</span>",
         "hero_desc": "Financial accuracy depends fundamentally on inventory validity. Altametrics instantly syncs live warehouse and walk-in values with your corporate accounting balance sheets.",
         "hero_image": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1",
         "b1_icon": "🔄", "b1_title": "Perpetual Valuation", "b1_desc": "Instead of waiting for generic end-of-month counts, your inventory assets are recalculated continuously based on live sales and deliveries.",
         "b2_icon": "📊", "b2_title": "FIFO & LIFO Options", "b2_desc": "Automatically exhaust the valuation of older inventory costs before newer ones based on your corporate tax preference.",
         "b3_icon": "📋", "b3_title": "Variance GL Mapping", "b3_desc": "When 'Actual vs Theoretical' gaps occur, the financial loss is automatically mapped to specific shrinkage expense accounts.",
         "uc1_challenge": "Accountants have to calculate 'Beginning Inventory + Purchases - Ending Inventory = COGS' manually every month on a massive spreadsheet.",
         "uc1_solution": "The system performs this calculation perpetually in real-time. By the 3rd of the month, the massive journal entry is already posted.",
         "uc2_challenge": "A store counts their inventory on a Friday, but an invoice from Thursday hasn't been entered yet, destroying the math.",
         "uc2_solution": "The system enforces logic blocks, preventing managers from submitting inventory counts until all pending EDI invoices are reconciled.",
         "dd1_h2": "Store-to-Store Transfer Accounting", "dd1_p": "When a GM moves two cases of chicken to a sister store down the street, it's not just an operational task; it's a massive accounting headache. The sync engine automatically credits the sending store's balance sheet and debits the receiving store's inventory assets the moment the digital transfer is accepted.",
         "dd1_li1": "Zero manual intercompany journal entry", "dd1_li2": "Accounts for complex tax zones", "dd1_li3": "Enforces GM accountability protocols", "dd1_img": "https://images.unsplash.com/photo-1586880244406-556ebe35f282",
         "dd2_h2": "Depreciating Prep-Batches", "dd2_p": "If you buy flour ($10) and yeast ($5), your raw asset value is $15. If a prep cook combines them into pizza dough, they are now a new Work-In-Progress (WIP) asset. The software tracks the financial transformation of these raw goods into sub-recipes, maintaining perfect valuation accuracy on the balance sheet at every stage of the cooking process.",
         "dd2_li1": "Raw to WIP financial tracking", "dd2_li2": "Eliminates double counting", "dd2_li3": "Validates complex commissary operations", "dd2_img": "https://images.unsplash.com/photo-1507048331197-7d4ac70811cf",
         "role1_desc": "Conduct counts using an intuitive mobile app, knowing the math is already handled for you.",
         "role2_desc": "Never question the validity of your COGS percentage again. The financials perfectly reflect the physical reality of the walk-in.",
         "quote": "Untangling our inter-store transfers used to consume our accounting department for 4 days at month-end. Now, the system just posts the offsets automatically. It’s flawless.",
         "author": "VP of Finance", "brand": "Regional Burger Chain",
         "faq1_q": "Does this require barcode scanning?", "faq1_a": "No, while barcode scanning is supported for receiving, store general inventory counts can easily be conducted using our custom sheet-to-shelf digital interface on any tablet.",
         "faq2_q": "How are wildly changing commodity prices handled?", "faq2_a": "The system defaults to a Weighted Average Cost algorithm for valuing existing inventory, meaning radical price spikes smooth out accurately as new invoice data is ingested.",
         "faq3_q": "Can it sync with our commissary kitchen?", "faq3_a": "Yes, commissary/warehouse modules allow corporate to act as the massive 'vendor' to the individual stores, tracking holistic inventory assets across the entire closed supply loop."
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
    print(f"Generated {len(PAGES)} highly unique pages for Batch 3.")

if __name__ == "__main__":
    update_templates()
