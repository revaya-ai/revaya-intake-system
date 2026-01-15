"""Revaya AI - Business Configuration"""

COMPANY_INFO = {
    "name": "Revaya AI",
    "website": "https://www.revayaai.com",
    "contact_email": "shannon@revayaai.com",
    "services": ["AI Automation", "Voice Agents", "Strategic Websites", "Operational Consulting"],
    "core_value_prop": "Reclaim 10+ hours per week through transparent automation",
    "positioning": "Transparent, auditable AI systems—not black boxes"
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
    "strategic_website": {
        "name": "Strategic Website",
        "base_price": 5000,
        "setup_time": "4-6 weeks",
        "roi_metric": "Visitor-to-client conversion rate",
        "features": [
            "Next.js + React",
            "SEO optimized",
            "Mobile-first responsive",
            "Brand-aligned design",
            "Performance optimized",
            "You own the code"
        ],
        "partner_note": "Partnership with Winnicki Digital for design + SEO"
    },
    "discovery_consulting": {
        "name": "Operational Audit & Discovery",
        "session_price": 500,
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
    "recipient": "shannon@revayaai.com",
    "from_email": "system@revayaai.com",
    "bcc": None  # Optional BCC for backup
}

SLACK_CONFIG = {
    "channel": "revaya-leads",
    "webhook_url": "ENV_VAR"
}

GOOGLE_DRIVE_CONFIG = {
    "folder_name": "Revaya AI - Client Proposals"
}

# Discovery framework aligned with Revaya positioning
DISCOVERY_QUESTIONS = {
    "time_audit": [
        "Where is your time actually going each week?",
        "What takes 30 minutes that you do every day?",
        "What workflow makes you want to scream?"
    ],
    "pain_points": [
        "What's the operational bottleneck that limits growth?",
        "Where are manual handoffs breaking?",
        "What would give you 10 hours back per week?"
    ],
    "opportunity_cost": [
        "What could you do with those 10 hours?",
        "What's this costing you in revenue?",
        "What growth opportunity are you missing?"
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
