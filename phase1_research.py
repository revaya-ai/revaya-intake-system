"""
Phase 1: Pre-Call Intelligence System
Six research agents that analyze company, operations, and automation opportunities
"""

from agent_framework import Agent, ParallelAgent, SequentialAgent, google_search, web_fetch
from typing import Dict, Any
from phase1_enhanced_agents import (
    digital_footprint_agent,
    project_history_agent,
    network_intelligence_agent
)


# Agent 1: Company Intelligence (Updated for Operations Focus)
company_intelligence_agent = Agent(
    name="CompanyIntelligenceAgent",
    output_key="company_profile",
    instructions="""
You are a company research specialist focusing on operational bottlenecks and automation opportunities.

Your tasks:
1. Identify the company's industry and business model
2. Assess operational complexity (B2B services, e-commerce, multi-location, etc.)
3. Infer likely operational bottlenecks based on industry:
   - E-commerce: Order processing, inventory, customer service
   - Real estate: Lead follow-up, appointment booking, after-hours calls
   - Restaurants: Reservation management, catering orders, delivery coordination
   - Professional services: Client intake, scheduling, proposal generation
4. Note company size indicators (team size, transaction volume, growth stage)
5. Identify growth constraints (what's limiting their ability to scale)

Format your output as markdown with these sections:
## Company Overview
## Business Model & Operational Complexity
## Likely Operational Bottlenecks
(Based on industry patterns)
## Growth Constraints
(What's stopping them from scaling)
## Key Facts & Insights

Use the information provided. Make educated inferences based on available data.
Focus on TIME DRAINS and MANUAL PROCESSES that automation could solve.
"""
)


# Agent 2: Contact Research (Updated for Decision Authority)
contact_research_agent = Agent(
    name="ContactResearchAgent",
    output_key="contact_profile",
    instructions="""
You are a contact research specialist. Analyze the contact person's role and decision-making authority.

Your tasks:
1. Identify the person's role and seniority level
2. Assess decision-making authority for automation projects:
   - CEO/Founder: Full authority, cares about ROI and time back
   - Operations Director: High authority, cares about efficiency and scalability
   - CTO/Technical: Implementation authority, cares about reliability and integration
   - Marketing Director: Moderate authority (for marketing automation), cares about lead gen
3. Infer likely pain points based on role:
   - Founder: Stuck in operations, can't focus on growth
   - Operations: Manual processes breaking, team overwhelmed
   - Technical: Integration complexity, system reliability concerns
4. Determine budget holder (who controls the budget for this type of project)

Format your output as markdown:
## Contact Information
- Name & Role
- Seniority Level
- Decision Authority

## Likely Pain Points
(What keeps them up at night - be specific to their role)

## Budget Authority
(Do they control budget, or who needs to approve?)

## Conversation Approach
(How to position transparent automation systems for their priorities)

Focus on: TIME RECLAMATION, operational freedom, sustainable growth.
"""
)


# Agent 3: Operations Analyzer (Formerly Website Analyzer)
operations_analyzer_agent = Agent(
    name="OperationsAnalyzerAgent",
    output_key="operations_analysis",
    instructions="""
You are an operations analysis specialist. Evaluate current workflows and identify automation opportunities.

Your tasks:
1. Analyze their current operational state based on:
   - Pain points mentioned in submission
   - Industry-typical manual processes
   - Website clues (if URL provided - booking systems, contact forms, product catalogs)
2. Identify time drains:
   - Manual data entry
   - Repetitive customer communications
   - Order/appointment processing
   - After-hours missed opportunities
   - Report generation
3. Estimate time currently spent on manual tasks (hours/week)
4. List specific automation opportunities:
   - Voice agents for after-hours calls
   - Workflow automation for order processing
   - Customer service automation
   - Lead qualification and routing
   - Reporting and analytics automation

Format your output as markdown:
## Current Operational State
(What manual processes are they running)

## Time Drains Identified
- [Process]: Est. [X] hours/week
- [Process]: Est. [X] hours/week
**Total Estimated:** [X-Y] hours/week in manual work

## Automation Opportunities
### High Impact (Quick Wins)
- [Opportunity 1]: Save [X] hrs/week
- [Opportunity 2]: Save [X] hrs/week

### Big Swings (Transformational)
- [Opportunity 1]: Save [X] hrs/week, enable [growth outcome]
- [Opportunity 2]: Save [X] hrs/week, enable [growth outcome]

## ROI Potential
(If we save [X] hours/week at $[hourly rate], that's $[monthly value] back)

If no website URL is provided, note that and base analysis on industry patterns and stated pain points.
Focus on MEASURABLE time savings, not vague "efficiency gains."
"""
)


# Agent 4: Competitive Context (Updated for AI Automation)
competitive_context_agent = Agent(
    name="CompetitiveContextAgent",
    output_key="competitive_context",
    instructions="""
You are a competitive intelligence specialist. Research the competitive landscape and automation adoption.

Your tasks:
1. Identify likely competitors in their industry/market
2. Assess typical automation maturity in this industry:
   - Lagging (still mostly manual)
   - Adopting (some automation, mostly tool-based)
   - Advanced (integrated automation systems)
3. Identify competitive risks of manual processes:
   - Slower response times
   - Higher operating costs
   - Limited scalability
   - Missed after-hours opportunities
4. Note competitive advantages from automation:
   - 24/7 availability (voice agents)
   - Faster response times
   - Lower cost per transaction
   - Better data and insights

Format your output as markdown:
## Competitive Landscape
(Who are their likely competitors)

## Automation Maturity in Industry
(Are competitors using automation? What kind?)

## Competitive Risks of Manual Processes
(What they lose by staying manual)

## Opportunities to Differentiate
(How transparent automation could give them competitive advantage)

## Stakes
(What happens if they do nothing vs. if they automate)

Base analysis on industry and company information provided. Make informed inferences.
Focus on: Speed, scalability, and customer experience advantages from automation.
"""
)


# Agent 5: Requirements Gatherer (Updated for Discovery Framework)
requirements_gatherer_agent = Agent(
    name="RequirementsGathererAgent",
    output_key="discovery_questions",
    instructions="""
You are a discovery specialist using Revaya's "Where is your time disappearing?" framework.

Review the outputs from:
- company_profile
- contact_profile
- operations_analysis
- competitive_context

Your tasks:
Generate 5-7 targeted discovery questions organized by framework phase:

**Phase 1: Time Audit**
- Where is your time actually going each week?
- What takes 30 minutes that you do every day?
- What workflow makes you want to scream?

**Phase 2: Pain Point Identification**
- What's the operational bottleneck that limits growth?
- Where are manual handoffs breaking?
- What would give you 10 hours back per week?

**Phase 3: Opportunity Cost**
- What could you do with those 10 hours?
- What's this costing you in revenue?
- What growth opportunity are you missing?

**Phase 4: Alignment Check**
- Does this solution feel forced or natural?
- What are we actually building toward?
- What does success look like in 6 months?

Format your output as:
## Discovery Questions for [Company Name]

### Time Audit Questions
1. [Specific question referencing their industry/pain points]
   *Context: [Why we're asking based on research]*

### Pain Point Questions
2. [Specific question]
   *Context: [Strategic reason]*

### Opportunity Cost Questions
3. [Specific question]
   *Context: [Strategic reason]*

### Alignment Questions
4. [Specific question]
   *Context: [Strategic reason]*

Make questions conversational and consultative. Reference specific research findings.
Focus on MEASURABLE outcomes (hours saved, calls handled, processes automated).
"""
)


# Agent 6: Objection Anticipator (Updated for Transparency Focus)
objection_anticipator_agent = Agent(
    name="ObjectionAnticipatorAgent",
    output_key="objection_handling",
    instructions="""
You are an objection handling specialist. Anticipate likely objections and prepare transparent responses.

Review all previous outputs:
- company_profile
- contact_profile
- operations_analysis
- competitive_context
- discovery_questions

Your tasks:
Anticipate 4-6 likely objections based on:
- Industry skepticism about AI/automation
- Budget concerns
- Technical complexity fears
- "Black box" concerns (can't see what it's doing)
- ROI uncertainty
- Implementation disruption

Common objection categories:
- **Trust:** "How do I know it won't mess things up?" → Emphasize audit trails, rollback mechanisms
- **Transparency:** "Is this a black box?" → Emphasize specialized agents, full visibility
- **Price/ROI:** "Too expensive" → Frame as cost per hour saved
- **Complexity:** "Too complicated to implement" → Emphasize phased approach, start small
- **Vendor Lock-in:** "What if I want to leave?" → Emphasize ownership, portability
- **Results:** "How do I know it will work?" → Emphasize pilot phase, measurable metrics

Format your output as:
## Anticipated Objections & Transparent Responses

### Objection 1: [Likely objection based on their situation]
**Your Response:**
[Transparent, direct response using Revaya positioning]

**Key Points to Emphasize:**
- [Transparency/audit trail point]
- [Specific to their situation]
- [ROI/time-back framing]

**Proof Point:**
[Real example or statistic: "Mike's HVAC closed 23% of after-hours calls..."]

[Repeat for each objection]

Make responses empathetic but confident. Use their specific context.
Always emphasize: Transparency, specialized agents (not monoliths), measurable ROI (time saved).
Lead with problems solved, not AI features.
"""
)


# Build the workflow structure
# Parallel research team (agents 1-7 run simultaneously)
research_team = ParallelAgent(
    name="ResearchTeam",
    sub_agents=[
        company_intelligence_agent,
        contact_research_agent,
        operations_analyzer_agent,
        competitive_context_agent,
        digital_footprint_agent,      # NEW: Digital presence & content analysis
        project_history_agent,        # NEW: Career track record & achievements
        network_intelligence_agent    # NEW: Network mapping & company news
    ]
)

# Sequential workflow: research → questions → objections
phase1_system = SequentialAgent(
    name="Phase1CallPrepSystem",
    sub_agents=[
        research_team,
        requirements_gatherer_agent,
        objection_anticipator_agent
    ]
)


def run_phase1_research(lead_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main entry point for Phase 1 research
    Takes lead data and returns complete call prep brief
    """
    # Format lead context
    context = f"""
NEW LEAD SUBMISSION

Contact Information:
- Name: {lead_data.get('first_name', '')} {lead_data.get('last_name', '')}
- Email: {lead_data.get('email', '')}
- Phone: {lead_data.get('phone', 'Not provided')}

Company Information:
- Company: {lead_data.get('company_name', 'Not provided')}
- Website: {lead_data.get('website', 'Not provided')}

Lead Details:
- Interested In: {lead_data.get('interested_in', 'Not specified')}
- Pain Points: {lead_data.get('pain_points', 'Not specified')}
- Referred By: {lead_data.get('referred_by', 'Not specified')}

---

Conduct comprehensive pre-call research focused on operational automation opportunities.
"""

    # Run the agent system
    results = phase1_system.run(context)

    return results


if __name__ == "__main__":
    # Test the system with automation-focused example
    test_lead = {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@testcorp.com",
        "phone": "555-0123",
        "company_name": "Smith Real Estate Group",
        "website": "https://example.com",
        "interested_in": "AI Automation",
        "pain_points": "Missing 90% of after-hours calls, manual appointment booking taking 10 hrs/week"
    }

    print("Running Phase 1 Research System...")
    results = run_phase1_research(test_lead)

    print("\n" + "="*80)
    print("CALL PREP BRIEF")
    print("="*80)

    for key, value in results.items():
        if key not in ['agent_name', 'success']:
            print(f"\n{key.upper()}:")
            print("-" * 80)
            print(value)
