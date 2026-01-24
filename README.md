# Revaya AI - Client Intake & Intelligence System

A two-phase AI-powered system for automated discovery and proposal generation focused on operational automation.

## 🎯 Overview

This system automates the entire client intake process from initial lead to proposal delivery:

**Phase 1: Pre-Call Intelligence** (Automated)
- 10 AI agents with **real-time web research** (Google Search grounding) research company, contact, operations, digital footprint, personal brand, and pain points
- Generate discovery questions aligned with "Where is your time disappearing?" framework
- Email complete brief to Shannon
- Notify Slack (#revaya-leads) with personal brand summary
- Save to Google Drive
- Push lead to Airtable CRM

**Phase 2: Proposal Generation** (Manual trigger after discovery call)
- Input discovery answers from operational audit
- 4 AI agents generate complete proposal with ROI framing and timeline
- Email proposal for review
- Notify Slack and save to Drive

## 🏗️ Architecture

### Phase 1: Research Agents (Parallel Execution)
1. **CompanyIntelligenceAgent** - Company profile and operational bottlenecks
2. **ContactResearchAgent** - Contact background and decision-making authority
3. **OperationsAnalyzerAgent** - Current operational workflows and time drains
4. **CompetitiveContextAgent** - Competitive landscape and market position
5. **RequirementsGathererAgent** - Discovery questions focused on time reclamation
6. **ObjectionAnticipatorAgent** - Anticipated objections with transparent responses
7. **DigitalFootprintAnalyzer** - Online presence, content style, and communication patterns
8. **ProjectHistoryResearcher** - Career track record, key projects, and achievements
9. **NetworkIntelligenceAnalyzer** - Professional network, company news, and trajectory signals
10. **PersonalBrandAnalyzerAgent** - Deep personal brand intelligence for rapport building

### Phase 2: Proposal Agents (Sequential Execution)
1. **TechnicalScoperAgent** - Automation architecture and specialized agents
2. **PricingCalculatorAgent** - ROI-based pricing (time saved, not just features)
3. **TimelineEstimatorAgent** - Phased implementation roadmap
4. **ProposalWriterAgent** - Complete proposal with transparency focus

## 📋 Prerequisites

- Python 3.11+
- Google Cloud account (project: `revaya-ai-systems`)
- Google AI API key (with Gemini 2.5 Flash access)
- SendGrid API key (for email)
- Slack webhook URL (for notifications)
- Google Drive API credentials (optional)
- Airtable API key (for CRM integration)

### Google Search Grounding

Agents use **Gemini 2.5 Flash with Google Search grounding** for real-time web research. This enables:
- Live LinkedIn profile research (no scraping required)
- Current company information and news
- Real-time competitive intelligence
- Automatic source citations

**Cost:** ~$35 per 1,000 grounded queries (uses same `GOOGLE_API_KEY`)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/revaya-ai/revaya-intake-system.git
cd revaya-intake-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
GOOGLE_API_KEY=your_google_api_key
SENDGRID_API_KEY=your_sendgrid_key
FROM_EMAIL=system@revayaai.com
TO_EMAIL=shannon@revayaai.com
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
AIRTABLE_API_KEY=your_airtable_api_key
PORT=8000
```

### 4. Run Locally

```bash
python api.py
```

Visit:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## 🧪 Testing

### Test Phase 1 (Pre-Call Research)

```bash
curl -X POST http://localhost:8000/initial-lead \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@testcorp.com",
    "phone": "555-0123",
    "company_name": "Smith Real Estate Group",
    "website": "https://example.com",
    "interested_in": "AI Automation",
    "pain_points": "Missing 90% of after-hours calls, manual appointment booking taking 10 hrs/week",
    "company_size": "11-50",
    "industry": "Real Estate",
    "budget_range": "$2,000-5,000/month",
    "timeline": "Want to start within 30 days",
    "linkedin_url": "https://linkedin.com/in/johnsmith"
  }'
```

### Test Phase 2 (Proposal Generation)

```bash
curl -X POST http://localhost:8000/generate-proposal \
  -H "Content-Type: application/json" \
  -d '{
    "client_info": {
      "company_name": "Test Corp",
      "contact_name": "John Smith",
      "email": "john@testcorp.com",
      "industry": "E-commerce"
    },
    "discovery_answers": "Need order processing automation, inventory alerts, customer service agent. Currently spending 15 hrs/week on manual tasks. Budget $5-8K, 4-6 week timeline acceptable."
  }'
```

### Test Integrations

```bash
curl -X POST http://localhost:8000/test-integrations
```

## 🐳 Docker

### Build

```bash
docker build -t revaya-intake .
```

### Run

```bash
docker run -p 8000:8080 \
  -e GOOGLE_API_KEY=your_key \
  -e SENDGRID_API_KEY=your_key \
  -e SLACK_WEBHOOK_URL=your_webhook \
  revaya-intake
```

## ☁️ Google Cloud Run Deployment

### Option 1: Simple Deployment

```bash
# Set environment variables
export GOOGLE_API_KEY=your_key
export SENDGRID_API_KEY=your_key
export SLACK_WEBHOOK_URL=your_webhook
export FROM_EMAIL=system@revayaai.com
export TO_EMAIL=shannon@revayaai.com

# Deploy
./deploy.sh
```

### Option 2: Secure Deployment (Recommended)

Uses Google Cloud Secret Manager for credentials:

```bash
# Create .env file with your credentials
cp .env.example .env
# Edit .env with actual values

# Deploy with secrets
./deploy-with-secrets.sh
```

### Manual Deployment

```bash
# Build
gcloud builds submit --tag gcr.io/revaya-ai-systems/revaya-intake

# Deploy
gcloud run deploy revaya-intake \
  --image gcr.io/revaya-ai-systems/revaya-intake \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=xxx,SENDGRID_API_KEY=xxx,SLACK_WEBHOOK_URL=xxx
```

## 📁 Project Structure

```
revaya-intake-system/
├── api.py                      # FastAPI application
├── config.py                   # Business configuration
├── phase1_research.py          # Phase 1: 6 core research agents
├── phase1_enhanced_agents.py   # Phase 1: 4 enhanced research agents (digital, history, network, personal brand)
├── phase2_proposal.py          # Phase 2: 4 proposal agents
├── agent_framework.py          # Agent framework with Google Search grounding
├── utils.py                    # Email, Slack, Drive, Airtable utilities
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration
├── deploy.sh                   # Cloud Run deployment
├── deploy-with-secrets.sh      # Secure deployment
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## 🔌 API Endpoints

### GET /
Health check

### GET /health
Detailed health check with configuration status

### POST /initial-lead
Phase 1: Generate pre-call intelligence brief

**Request:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "email": "john@example.com",
  "phone": "555-0123",
  "company_name": "Test Corp",
  "website": "https://example.com",
  "interested_in": "AI Automation",
  "pain_points": "Missing after-hours calls, manual appointment booking taking 10 hrs/week",
  "referred_by": "Google Search",
  "company_size": "11-50",
  "industry": "Real Estate",
  "pain_cost_monthly": "$5,000-10,000 in missed opportunities",
  "workflow_description": "Leads come in via website, manually entered into CRM",
  "repetitive_tasks": "Data entry, appointment confirmations, follow-up emails",
  "current_tools": "Salesforce, Google Calendar, Gmail",
  "decision_makers": "CEO and Operations Director",
  "past_vendors": "Tried Zapier but too limited",
  "timeline": "Want to start within 30 days",
  "budget_range": "$2,000-5,000/month",
  "success_90_days": "Reduce manual work by 50%, never miss an after-hours call",
  "what_prompted_call": "Lost a big deal because we didn't respond fast enough",
  "tech_comfort_level": 3,
  "tried_ai_before": "Used ChatGPT for writing but nothing operational",
  "lead_source": "LinkedIn Ad",
  "linkedin_url": "https://linkedin.com/in/johnsmith"
}
```

**Note:** Only `first_name`, `last_name`, `email`, and `interested_in` are required. All other fields are optional.

**Response:**
```json
{
  "success": true,
  "brief": "...",
  "email_sent": true,
  "slack_notified": true,
  "drive_link": "https://..."
}
```

### POST /generate-proposal
Phase 2: Generate complete proposal

**Request:**
```json
{
  "client_info": {
    "company_name": "Test Corp",
    "email": "john@testcorp.com"
  },
  "discovery_answers": "Need inventory automation, 15 hrs/week manual work..."
}
```

**Response:**
```json
{
  "success": true,
  "proposal": "...",
  "technical_scope": "...",
  "pricing_breakdown": "...",
  "timeline_estimate": "...",
  "email_sent": true,
  "drive_link": "https://..."
}
```

## 🔧 Configuration

### Business Configuration (config.py)

Edit `config.py` to customize:
- Automation services and pricing (ROI-based, not feature-based)
- Company information
- Email recipients
- Slack channels

### Agent Customization

Each agent can be customized by editing:
- `phase1_research.py` - Research agent instructions
- `phase2_proposal.py` - Proposal agent instructions

## 📊 Monitoring

### View Logs (Cloud Run)

```bash
gcloud run logs read --service=revaya-intake --limit=100
```

### View Logs (Local)

Logs are printed to console with emoji indicators:
- 📥 New lead received
- 🔍 Running agents
- 📧 Sending email
- 💬 Slack notification
- 💾 Saving to Drive
- 📊 Pushing to Airtable
- ✅ Success
- ❌ Error

## 🔒 Security

- API keys stored in environment variables
- Google Secret Manager integration for Cloud Run
- No credentials in code
- `.gitignore` prevents credential commits
- CORS configured for production

## 🐛 Troubleshooting

### Email not sending
- Verify `SENDGRID_API_KEY` is set
- Check `FROM_EMAIL` is verified in SendGrid
- View logs for specific error

### Slack not notifying
- Verify `SLACK_WEBHOOK_URL` is correct
- Test webhook with curl
- Check Slack app permissions

### Airtable not syncing
- Verify `AIRTABLE_API_KEY` is set (create at airtable.com/create/tokens)
- Ensure your token has access to the correct base
- Required scopes: `data.records:read`, `data.records:write`
- Core fields (required in your table):
  - First Name (Single line text)
  - Last Name (Single line text)
  - Email (Email)
  - Company Name (Single line text)
  - Website (URL)
  - Source (Single line text)
  - Status (Single select with "open" option)
- Optional fields (add to capture more data):
  - Phone, LinkedIn, Interested In, Pain Points
  - Industry, Company Size, Budget Range, Timeline
  - Referred By, Brief Link, LinkedIn Headline

### Google Drive not saving
- Ensure `credentials.json` exists
- System falls back to local storage if Drive unavailable
- Check output/ folder for local saves

### Agents not responding
- Verify `GOOGLE_API_KEY` is valid
- Check Google AI API quota
- Review logs for specific errors

## 📝 Development

### Run Tests

```bash
# Test Phase 1 agents
python phase1_research.py

# Test Phase 2 agents
python phase2_proposal.py

# Test utilities
python utils.py

# Test API
python api.py
# Then use test scripts
```

### Add New Agents

1. Create agent in appropriate phase file
2. Add to workflow (ParallelAgent or SequentialAgent)
3. Update instructions and output_key
4. Test independently before integration

## 📄 License

Proprietary - Revaya AI

## 👥 Contact

Shannon Winnicki - shannon@revaya.ai
Website: https://www.revaya.ai

## 🚀 Deployment Checklist

- [ ] Set all environment variables
- [ ] Test locally with `python api.py`
- [ ] Test endpoints with curl or Postman
- [ ] Verify email delivery
- [ ] Verify Slack notifications
- [ ] Test Google Drive integration
- [ ] Test Airtable CRM integration
- [ ] Build Docker image
- [ ] Deploy to Cloud Run
- [ ] Test production endpoints
- [ ] Monitor logs for errors
- [ ] Set up monitoring/alerts

## 📈 Future Enhancements

- [ ] Add webhook for automatic form submission
- [x] ~~Implement CRM integration~~ - Airtable integration complete
- [x] ~~Add real-time web research~~ - Google Search grounding enabled (Gemini 2.5 Flash)
- [ ] Add proposal versioning
- [ ] Create dashboard for tracking leads
- [ ] Add analytics and reporting
- [ ] Implement A/B testing for proposals
- [ ] Add ROI calculator for discovery calls
- [ ] Create mobile app interface
