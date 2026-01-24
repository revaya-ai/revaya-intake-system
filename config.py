"""Revaya AI - Business Configuration"""
    
COMPANY_INFO = {
    "name": "Revaya AI",
    "tagline": "Reclaim Time. Build Freedom.",
    "website": "https://revaya.ai",
    "contact_email": "shannon@revaya.ai",
    "services": [
        "AI Solutions (Voice Agents, Workflow Automation, Maintenance)",
        "AI Consulting (Discovery, Roadmapping, Strategic Advisory)",
        "Website Solutions (Design, Updates, Performance, SEO)"
    ],
    "core_value_prop": "Long-term growth partner. We stay. We grow with you.",
    "positioning": "Discovery-first. Transparency always. Partnership for the long term."
}
            
# Revaya services focused on time reclamation and operational automation
AUTOMATION_SERVICES = {
    "voice_agent": {
        "name": "AI Voice Agent",
        "base_price": 2500,
        "setup_time": "2-3 weeks",
        "roi_metric": "After-hours calls answered, appointments booked automatically",
        "features": [
            "Custom conversation flows",
            "Retell integration",
            "n8n workflow orchestration",
            "Full audit trails",
            "Appointment booking",
            "Lead qualification"
        ]
    },
    "workflow_automation": {  
        "name": "Workflow Automation",
        "hourly_rate": 150,
        "typical_scope": "$3000-8000",
        "setup_time": "3-6 weeks",
        "roi_metric": "Hours saved per week, manual steps eliminated",
        "features": [
            "Specialized agents (microservices approach)",
            "n8n visual workflows",
            "Full transparency and audit trails",
            "Rollback mechanisms",
            "Custom integration",
            "Ongoing optimization"
        ]
    },
    "discovery_consulting": {
        "name": "Operational Audit & Discovery",
        "session_price": 500,
        "hourly_rate": 150,
        "duration": "60-90 minutes",
        "deliverable": "Operational audit report + prioritized roadmap",
        "features": [
            "Time audit (where hours disappear)",
            "Workflow mapping",  
            "Bottleneck identification",
            "ROI estimation (time back)",
            "Phased implementation roadmap",
            "Solution architecture"
        ]
    }
}

# Website services with three-tier structure
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
    "retainer_range": "300-800/month",
    "technologies": [
        "Wix, Webflow, Shopify, WordPress",
        "Vibe coding: Lovable, Cursor, Replit, Bolt"
    ]
}

# Revaya pricing philosophy: ROI-based (time saved), not feature-based
PRICING_PRINCIPLES = {
    "roi_focus": "Frame pricing around time reclaimed, not features",
    "transparency": "Full breakdown: setup, monthly, per-transaction costs",
    "time_metric": "Calculate cost per hour saved (e.g., $5K / 10 hrs/week = $12/hr)",
    "avoid_guarantees": "Promise time saved, not revenue outcomes (too many variables)",
    "phased_approach": "Start small, prove value, expand",
    "ongoing_partnership": "Retainer for maintenance, optimization, expansion"
}
        
EMAIL_CONFIG = {
    "recipient": "shannon@revaya.ai",
    "from_email": "system@revaya.ai",
    "bcc": None  # Optional BCC for backup
}
        
SLACK_CONFIG = {  
    "channel": "revaya-leads",
    "webhook_url": "ENV_VAR"
}
            
GOOGLE_DRIVE_CONFIG = {
    "folder_name": "Revaya AI - Client Proposals"
}

AIRTABLE_CONFIG = {
    "base_id": "app1Qgt52Fj22f9Nh",
    "table_id": "tblyFaORZ4Vi3eonh",
    "table_name": "Leads"  # Friendly name for logging
}

# Discovery framework aligned with Revaya positioning
DISCOVERY_QUESTIONS = {
    "ai_time_audit": [
        "What task do you repeat more than 3x a week?",
        "Where is your time actually going each week?",
        "What takes 30 minutes that you do every day?",
        "What workflow makes you want to scream?"
    ],
    "ai_pain_points": [
        "Are your processes mapped out?",
        "What's your biggest pain point right now?",
        "What's the operational bottleneck that limits growth?",
        "Where are manual handoffs breaking?"
    ],
    "ai_opportunity_cost": [
        "What would give you 10 hours back per week?",
        "What could you do with those 10 hours?",
        "What's this costing you in revenue?",
        "What growth opportunity are you missing?"
    ],
    "website_time_audit": [
        "What's your biggest pain point with your current website?",
        "How often do you review website performance?",
        "What website platform are you on, and what's your opinion of it?",
        "How much time do you spend updating your website?",
        "How often do customers say they can't find what they need?",
        "When's the last time you looked at your site on a phone?"
    ],
    "website_pain_points": [
        "What's your website costing you in lost leads?",
        "Where are potential customers bouncing?",
        "What can't you do on your current site that you need?",
        "Is your website actually bringing in business, or just sitting there?"
    ],
    "website_opportunity_cost": [
        "How many leads could you capture with a better contact form?",
        "What would 10 more qualified leads per month be worth?",
        "What business are you losing to competitors with better sites?",
        "For E-commerce: What's your average order value and monthly transactions?",
        "For E-commerce: What revenue could abandoned cart recovery add?",
        "For E-commerce: How much time do you spend on manual order processing?"
    ],
    "alignment": [
        "Does this solution feel forced or natural?",
        "What are we actually building toward?",
        "What does success look like in 6 months?"
    ]       
}

# Red flags for client qualification
CLIENT_RED_FLAGS = [
    "Guarantees on revenue outcomes",
    "Unrealistic timelines with no flexibility",
    "Scope creep without budget discussion",
    "Price shopping only",
    "Disrespectful communication",
    "Can't articulate the problem",
    "Wants to skip discovery",
    "History of churning vendors"
]
