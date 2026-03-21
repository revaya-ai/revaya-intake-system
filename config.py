"""Revaya AI - Business Configuration"""

COMPANY_INFO = {
    "name": "Revaya AI",
    "tagline": "Your business only works when you do. That's a systems problem.",
    "website": "https://revaya.ai",
    "contact_email": "shannon@revaya.ai",
    "services": [
        "Business AI OS — Audit, Setup, and Retainer",
        "Website Design and Development (active client engagements through Q2 2026)"
    ],
    "core_value_prop": "Specialized agents with full audit trails. Not monolithic black boxes. A system designed around your specific business.",
    "positioning": "I build Business AI Operating Systems for founder-led businesses. Discovery before implementation. Transparency always. Long-term architecture partnership."
}

# The five layers delivered in every AIOS engagement
AIOS_LAYERS = {
    "context": {
        "name": "Context Layer",
        "description": "Where does your business knowledge live? This layer captures decisions, workflows, client history, and institutional knowledge so your AI agents always have the right context.",
        "examples": ["Decision logs", "SOPs in AI-readable format", "Client and deal context", "Meeting summaries auto-captured"]
    },
    "data": {
        "name": "Data Layer",
        "description": "Connect the data sources that matter. CRM, email, calendar, Slack — pulled into one queryable layer.",
        "examples": ["CRM sync", "Meeting transcripts indexed", "Pipeline visibility", "Slack/email search"]
    },
    "intelligence": {
        "name": "Intelligence Layer",
        "description": "Agents that think. Specialized models for research, analysis, drafting, and decision support — each doing one job well.",
        "examples": ["Pre-call research briefs", "Proposal generation", "Content drafting", "Lead scoring"]
    },
    "automate": {
        "name": "Automate Layer",
        "description": "Recurring tasks that no longer require the founder. Triggered workflows, automated comms, scheduled reports.",
        "examples": ["Lead intake automation", "Follow-up sequences", "Weekly reporting", "Invoice and delivery triggers"]
    },
    "build": {
        "name": "Build Layer",
        "description": "Custom agents and tools built to the exact specifications of the business. This is where the AIOS becomes proprietary.",
        "examples": ["Custom intake agents", "Industry-specific research tools", "Internal command interfaces", "Client-facing automation"]
    }
}

# AIOS engagement tiers
AIOS_TIERS = {
    "audit": {
        "name": "AIOS Audit",
        "price": 3000,
        "deductible": True,
        "description": "A structured assessment of your business across the 5 AIOS layers. Deliverable: a prioritized architecture map and implementation roadmap. Deductible against Setup if you proceed.",
        "duration": "1–2 weeks",
        "deliverable": "AIOS Architecture Map + Prioritized Roadmap"
    },
    "setup": {
        "name": "AIOS Setup",
        "price_range": "$10,000 – $30,000",
        "price_min": 10000,
        "price_max": 30000,
        "description": "Full AIOS build across the 5 layers, scoped to the complexity of the engagement. Founder-first — the founder's AIOS is stable before any team scaling.",
        "duration": "4–8 weeks",
        "deliverable": "Deployed AIOS across scoped layers, training, documentation"
    },
    "retainer": {
        "maintenance": {
            "name": "Maintenance Retainer",
            "price_range": "$500 – $1,000/month",
            "description": "System health, updates, and issue resolution. No new builds."
        },
        "growth": {
            "name": "Growth Retainer",
            "price_range": "$2,000 – $5,000/month",
            "description": "Ongoing architecture work. New agents, new layers, expanding what's working. Includes build credits."
        },
        "partnership": {
            "name": "Partnership Retainer",
            "price_range": "$5,000 – $10,000/month",
            "description": "Deep ongoing engagement. Available after first Growth client at 90+ days in."
        }
    }
}

# ICP qualification criteria
ICP_CRITERIA = {
    "icp1_strong_fit": {
        "name": "ICP 1 — Drowning Operator",
        "signals": [
            "Founder-led business, 1–15 people",
            "Revenue $200K – $20M",
            "Knowledge-intensive work (agencies, consultancies, SaaS, professional practices, founder-led product brands)",
            "Founder is the primary bottleneck — decisions and knowledge are centralized in one person",
            "Has tried tools/automation before but without a system design",
            "AI-aware but not yet AI-operational"
        ],
        "hard_pass": [
            "Physical-operations-only businesses with no knowledge/judgment component",
            "Pure arbitrage or reseller model — no expertise embedded in the work",
            "Enterprise (100+ employees) — wrong fit for this model",
            "Under $200K revenue — not enough complexity to justify the engagement"
        ]
    },
    "icp2_pilot": {
        "name": "ICP 2 — Solo Founder / Entrepreneur",
        "signals": [
            "1–3 people, often solo with freelance support",
            "Pilot engagement path at $8K–$12K",
            "Motivated to learn and implement"
        ]
    }
}

# Website services — kept for active Q2 2026 web client engagements
WEBSITE_SERVICES = {
    "single_page": {
        "name": "Single Page Website",
        "price": 900,
        "timeline": "1 week",
        "best_for": "Landing pages, coming soon pages, simple online presence",
        "includes": [
            "1 page",
            "Mobile responsive",
            "Image gallery",
            "Lead capture form",
            "Embedded video",
            "Social share",
            "Website training"
        ],
        "add_ons": {
            "additional_page": 300,
            "training_hourly": 70
        }
    },
    "small_website": {
        "name": "Small Website",
        "price": 2499,
        "timeline": "2 weeks",
        "best_for": "Service businesses, consultants, coaches, small ecommerce shops",
        "includes": [
            "Up to 5 pages",
            "Mobile responsive",
            "Image gallery",
            "Lead capture form",
            "E-commerce (lite)",
            "Ticketing system",
            "Embedded video",
            "Social share",
            "Google Search Console",
            "Google Business Profile",
            "Website training"
        ],
        "add_ons": {
            "additional_page": 300,
            "blog": 500,
            "training_hourly": 70
        }
    },
    "large_website": {
        "name": "Large Website",
        "price": 5199,
        "timeline": "4-6 weeks",
        "best_for": "Established businesses needing comprehensive online presence",
        "includes": [
            "Up to 15 pages",
            "Mobile responsive",
            "Image gallery",
            "Lead capture form",
            "Full e-commerce",
            "Ticketing system",
            "Embedded video",
            "Social share",
            "Google Search Console",
            "Google Business Profile",
            "Website training"
        ],
        "add_ons": {
            "additional_page": 200,
            "blog": 400,
            "training_hourly": 50
        }
    },
    "hourly_rate": 75,
    "maintenance_retainer": "300–800/month",
    "technologies": [
        "Next.js (custom, SEO-optimized)",
        "Wix, Webflow, Shopify, WordPress",
        "Vibe coding: Lovable, Cursor, Replit, Bolt"
    ]
}

# AIOS ROI framing — used by proposal and pricing agents
PRICING_PRINCIPLES = {
    "primary_metric": "Founder hours recovered per week",
    "secondary_metrics": ["Task automation %", "Revenue per headcount"],
    "roi_framing": "Frame pricing as cost per hour of founder time recovered. Example: $15K setup / 10 hrs/week recovered = $28/hr over one year — far less than hiring.",
    "avoid_guarantees": "Promise system architecture and time savings potential, not revenue outcomes.",
    "augment_first": "Augment before you automate. Founder AIOS stable for 30+ days before team scaling.",
    "phased_approach": "Start with the highest-leverage layer. Prove value before expanding.",
    "retainer_value": "Retainer is not support — it is ongoing architecture. The system evolves as the business grows."
}

EMAIL_CONFIG = {
    "recipient": "shannon@revaya.ai",
    "from_email": "system@revaya.ai",
    "bcc": None
}

SLACK_CONFIG = {
    "channel": "revaya-leads",
    "webhook_url": "ENV_VAR"
}

GOOGLE_DRIVE_CONFIG = {
    "folder_name": "Revaya AI - Client Proposals"
}

# AIOS-aligned discovery questions organized by layer
DISCOVERY_QUESTIONS = {
    "context_layer": [
        "Where does your business knowledge live today? If you went off-grid for a week, what decisions would stall?",
        "What happens when someone on your team asks a question only you can answer?",
        "How do you capture what you learn from client work? Does it go anywhere useful?"
    ],
    "data_layer": [
        "What data do you collect that no one actually looks at?",
        "Where do things fall through the cracks — deals, follow-ups, action items from meetings?",
        "If I asked you right now what your pipeline looks like, how long would it take to get that answer?"
    ],
    "intelligence_layer": [
        "What decisions do you make repeatedly that feel like they follow a pattern?",
        "Where are you doing research or analysis manually that you wish you could delegate?",
        "What would need to be true for you to trust an AI agent to draft something on your behalf?"
    ],
    "automate_layer": [
        "What tasks do you do every week that you wish you didn't have to touch?",
        "What are you the bottleneck on that blocks other people from moving forward?",
        "What would give you 10 hours back per week?"
    ],
    "build_layer": [
        "What tools are you duct-taping together right now?",
        "What custom thing would you build if you had an engineering team for a week?",
        "What does your ideal operating week look like versus what it looks like today?"
    ],
    "qualification": [
        "What's your current monthly revenue range?",
        "How many people are on your team — employees plus regular contractors?",
        "How many hours per week do you spend on work only you can do?",
        "What percentage of your recurring tasks do you think could be handled without you?",
        "What's your revenue per team member right now, roughly?"
    ],
    "alignment": [
        "What does a win look like in 90 days?",
        "What does this need to be to feel worth it?",
        "What are we actually building toward?"
    ]
}

# Red flags for client qualification
CLIENT_RED_FLAGS = [
    "Wants to skip discovery",
    "Can't articulate what problem they're solving",
    "Price shopping without understanding the engagement",
    "Wants a tool, not a system",
    "History of churning vendors or blaming them",
    "Unrealistic timelines with no flexibility",
    "Disrespectful communication",
    "Guarantees on revenue outcomes demanded upfront"
]
