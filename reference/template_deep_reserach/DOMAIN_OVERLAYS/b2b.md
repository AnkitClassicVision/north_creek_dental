# B2B (Business-to-Business) Domain Overlay

## Overview
This overlay applies to businesses selling products or services to other businesses. It emphasizes buying committees, longer sales cycles, account-based approaches, and B2B-specific research requirements.

## Activation Criteria
Apply this overlay when:
- Primary customers are businesses, not individual consumers
- Sales involve multiple decision-makers
- Sales cycles are typically weeks to months (not impulse purchases)
- Industry: SaaS, Professional Services, Manufacturing, Wholesale, Business Services, Enterprise Solutions

---

## Mandatory Data Points

### Buying Process Data
- [ ] Typical buying committee composition
- [ ] Decision-maker roles and titles
- [ ] Influencer roles (technical, financial, end-user)
- [ ] Approval thresholds by deal size
- [ ] Typical sales cycle length
- [ ] RFP/procurement process (if formal)
- [ ] Budget cycle timing

### Account Intelligence
- [ ] Target company size (employees, revenue)
- [ ] Target industries/verticals
- [ ] Technology stack considerations
- [ ] Compliance/security requirements
- [ ] Integration requirements
- [ ] Existing vendor relationships

### Unit Economics (B2B-Specific)
- [ ] Average contract value (ACV)
- [ ] Customer acquisition cost (CAC) by segment
- [ ] Lifetime value (LTV) with retention assumptions
- [ ] Sales cycle length impact on cash flow
- [ ] Expansion revenue potential
- [ ] Churn/retention rates by segment

---

## Source Requirements

### Primary Sources (Required for C1 Claims)
| Source Type | Priority | Examples |
|-------------|----------|----------|
| Industry analyst reports | **High** | Gartner, Forrester, IDC |
| Professional associations | **High** | Trade associations, certification bodies |
| LinkedIn Sales Navigator | **Medium** | Org charts, title data |
| Company filings/reports | **High** | 10-K, annual reports (for public companies) |
| Industry publications | **Medium** | Trade journals, vertical publications |
| Conference/event data | **Medium** | Speaking topics, sponsor data |

### B2B Data Sources
- **LinkedIn:** Org structure, titles, connections
- **ZoomInfo/Apollo:** Contact and company data
- **Crunchbase:** Funding, growth signals
- **G2/Capterra:** B2B software reviews
- **Glassdoor:** Company culture, hiring trends
- **BuiltWith/Wappalyzer:** Technology stack

### Source Quality Grades (B2B-Specific)
| Grade | Criteria |
|-------|----------|
| **A** | Gartner Magic Quadrant, Forrester Wave, company filings, peer-reviewed research |
| **B** | Industry association reports, analyst briefings, G2 Crowd data |
| **C** | Trade publication surveys, conference presentations, vendor case studies |
| **D** | Blog posts, social media, single-source claims |
| **E** | Vendor marketing materials (unless verified), anonymous claims |

### Fallback Sources (Paywall-Free Alternatives)
When premium analyst reports are unavailable, use these free alternatives:

| Source Type | Free Alternative | URL |
|-------------|------------------|-----|
| **Company filings** | SEC EDGAR | sec.gov/edgar |
| **Funding data** | Crunchbase (free tier) | crunchbase.com |
| **Company insights** | LinkedIn (free tier) | linkedin.com/company |
| **Technology stacks** | BuiltWith (free tier) | builtwith.com |
| **Small business data** | SBA Resources | sba.gov |
| **Industry data** | Trade association sites | [varies by industry] |
| **Job market signals** | Indeed/LinkedIn Jobs | indeed.com, linkedin.com/jobs |
| **Review data** | G2/Capterra (free tier) | g2.com, capterra.com |
| **Government contracts** | SAM.gov | sam.gov |

### When in Doubt (B2B Claims Guidance)
**B2B marketing often involves regulated claims and contractual implications.** When uncertain:

1. **ROI claims:** Must have methodology and substantiation; avoid specific percentages without source
2. **Market position claims:** "Leader" or "Top" requires third-party validation (analyst report)
3. **Customer logos:** ALWAYS verify permission before using; check contract terms
4. **Case study metrics:** Verify with customer before publishing; get written approval
5. **Competitive comparisons:** Must be factual, verifiable, and fair; avoid disparagement
6. **Security/compliance claims:** SOC2, ISO, etc. must be current and accurate; verify dates
7. **Integration claims:** Verify partnership status before claiming integration capabilities
8. **Default action:** When unsure about B2B claims, verify against source documentation and get customer/partner approval where applicable

---

## Buying Committee Analysis

### Required Committee Documentation
```yaml
buying_committee:
  economic_buyer:
    typical_title: "[C-level, VP, Director]"
    primary_concerns: ["ROI", "Risk", "Strategic fit"]
    information_needs: ["Business case", "References", "TCO"]
    engagement_timing: "[Early/Mid/Late in process]"

  technical_buyer:
    typical_title: "[IT Director, Architect, Technical Lead]"
    primary_concerns: ["Integration", "Security", "Scalability"]
    information_needs: ["Technical specs", "API docs", "Security audit"]
    engagement_timing: "[Usually mid-process]"

  user_buyer:
    typical_title: "[Manager, Team Lead, End User]"
    primary_concerns: ["Ease of use", "Training", "Day-to-day value"]
    information_needs: ["Demo", "Trial", "User testimonials"]
    engagement_timing: "[Throughout process]"

  coach/champion:
    typical_title: "[Internal advocate]"
    primary_concerns: ["Making the project succeed internally"]
    information_needs: ["Internal selling tools", "Executive summary"]
    engagement_timing: "[Early and throughout]"

  procurement:
    typical_title: "[Procurement, Legal, Finance]"
    primary_concerns: ["Terms", "Compliance", "Pricing"]
    information_needs: ["Contracts", "Certifications", "Pricing sheets"]
    engagement_timing: "[Late stage]"

  committee_size_by_deal:
    small_deal: "[1-2 decision-makers]"
    mid_deal: "[3-5 decision-makers]"
    enterprise_deal: "[6+ stakeholders]"
```

---

## Persona Additions

### Required B2B Persona Fields
```yaml
persona_b2b_fields:
  role_in_buying:
    options: ["Economic buyer", "Technical buyer", "User buyer", "Coach/champion", "Blocker/skeptic"]

  seniority_level:
    options: ["C-suite", "VP", "Director", "Manager", "Individual contributor"]

  functional_area:
    options: ["IT", "Finance", "Operations", "Marketing", "Sales", "HR", "Executive"]

  kpis_measured_on:
    description: "What metrics is this person evaluated on?"
    examples: ["Revenue growth", "Cost reduction", "Team productivity", "Risk mitigation"]

  career_motivations:
    options: ["Promotion/visibility", "Making their team successful", "Innovation reputation", "Stability/risk avoidance"]

  information_consumption:
    options: ["Industry publications", "Peer networks", "Analyst reports", "Social (LinkedIn)", "Events/conferences", "Vendor content"]

  vendor_relationship_preference:
    options: ["Self-service/minimal contact", "Consultative partnership", "Hands-off after purchase"]

  risk_tolerance:
    options: ["Early adopter", "Fast follower", "Mainstream", "Laggard/conservative"]

  company_size:
    options: ["SMB (<100)", "Mid-market (100-1000)", "Enterprise (1000+)"]

  budget_authority:
    threshold: "[Dollar amount they can approve without escalation]"
```

---

## Sales Cycle Mapping

### B2B Funnel Stages
```
AWARENESS (Target Account Identification)
├── Account selection criteria
├── Intent signals
├── Metrics: Target account list, Intent score

DISCOVERY (Initial Engagement)
├── Triggers: Content download, event attendance, inbound inquiry
├── First meeting goals
├── Metrics: MQLs, First meetings booked

QUALIFICATION (Fit Assessment)
├── BANT/MEDDIC/GPCT criteria
├── Discovery questions
├── Metrics: SALs, Qualified opportunities

EVALUATION (Solution Mapping)
├── Demo/proof of concept
├── Technical validation
├── Stakeholder mapping
├── Metrics: POC success rate, Stakeholder engagement

PROPOSAL (Business Case)
├── ROI/business case
├── Reference calls
├── Procurement engagement
├── Metrics: Proposal acceptance rate

NEGOTIATION (Terms & Pricing)
├── Contract negotiation
├── Security/legal review
├── Final approvals
├── Metrics: Discount rate, Time to close

CLOSE (Contract Signed)
├── Signature
├── Handoff to implementation
├── Metrics: Win rate, ACV

EXPAND (Post-Sale Growth)
├── Implementation success
├── Adoption metrics
├── Expansion opportunities
├── Metrics: Time to value, NPS, Expansion revenue
```

---

## Account-Based Marketing (ABM) Considerations

### ABM Tier Structure
```yaml
abm_tiers:
  tier_1_strategic:
    account_count: "10-50"
    approach: "One-to-one, fully customized"
    resources: "Dedicated team, custom content, executive engagement"
    metrics: "Account engagement score, Pipeline from accounts, Win rate"

  tier_2_scale:
    account_count: "50-500"
    approach: "One-to-few, industry/segment customization"
    resources: "Segment-specific campaigns, targeted ads"
    metrics: "Account engagement, MQLs from target accounts"

  tier_3_programmatic:
    account_count: "500+"
    approach: "One-to-many, technology-enabled"
    resources: "Automated personalization, broad targeting"
    metrics: "Account reach, Engagement rates"
```

---

## Marketing Constraints

### B2B-Specific Compliance
- **Data privacy:** GDPR/CCPA implications for account data
- **Industry regulations:** Varies by target vertical (healthcare, finance, government)
- **Procurement requirements:** May need to meet specific certifications (SOC2, ISO, FedRAMP)

### Channel Restrictions
- **LinkedIn:** Sponsored content policies, InMail limits
- **Email:** CAN-SPAM, GDPR consent requirements
- **Events:** Industry association sponsorship rules
- **Analyst relations:** Disclosure requirements

### Proof Point Requirements
Case studies and references should include:
- Company name (or anonymized with industry/size)
- Specific, quantified results
- Timeframe to achieve results
- Permission for public use

---

## Competitive Intelligence

### B2B-Specific Sources
- **G2/Capterra/TrustRadius:** Product reviews, comparisons
- **Gartner Peer Insights:** Enterprise reviews
- **Analyst reports:** Magic Quadrant, Forrester Wave positioning
- **LinkedIn:** Competitor hiring, employee movements
- **Job postings:** Product roadmap signals, expansion plans
- **Conference presence:** Thought leadership positioning
- **Patent filings:** Technology differentiation

### Competitive Analysis Requirements
- [ ] Feature/capability comparison (detailed matrix)
- [ ] Pricing model comparison (where available)
- [ ] Target market comparison
- [ ] Go-to-market motion comparison
- [ ] Analyst positioning comparison
- [ ] Review platform comparison
- [ ] Customer case study analysis
- [ ] Technology/integration comparison
- [ ] Team/leadership comparison
- [ ] Funding/financial position comparison

---

## Pricing & Packaging Research

### B2B Pricing Models
Document competitor and market standard for:
- Per-seat vs. per-usage pricing
- Tiered packaging structure
- Enterprise/custom pricing approach
- Implementation/onboarding fees
- Annual vs. monthly commitment discounts
- Expansion/upsell triggers

### Value-Based Pricing Inputs
Research should support:
- ROI calculation framework
- Value metrics (what outcomes to measure)
- Willingness-to-pay signals
- Competitive price positioning

---

## Red Flags (Automatic Review Triggers)

If research uncovers any of these, flag for user attention:

1. **Market Signals:**
   - Major competitor funding/acquisition
   - New entrant with disruptive model
   - Analyst report repositioning
   - Technology shift affecting category

2. **Account Intelligence:**
   - Target company layoffs/restructuring
   - Budget freeze signals
   - Key champion departure
   - Competitive deal loss patterns

3. **Product/Market Fit:**
   - Negative review trends
   - Churn signals in market
   - Feature gap vs. competitors
   - Compliance/certification gaps

---

## Skill Integration

### perplexity Usage for B2B
- Research buying committee structures by industry
- Find industry benchmark data (sales cycles, win rates)
- Verify competitor funding and growth
- Research target account intelligence

### hubspot Usage for B2B
- CRM data on existing accounts
- Contact and company enrichment
- Deal stage analysis
- Pipeline forecasting inputs

### codex Usage for B2B
- Audit competitive analysis completeness
- Verify pricing research accuracy
- Check case study claims
- Review sales cycle assumptions

---

## Checklist: B2B Research Complete

```yaml
b2b_completion_checklist:
  buying_process:
    - [ ] Buying committee roles documented
    - [ ] Decision criteria by role identified
    - [ ] Sales cycle stages mapped
    - [ ] Budget cycle timing understood
    - [ ] RFP/procurement process documented

  personas:
    - [ ] Persona per buying committee role
    - [ ] KPIs/success metrics per role
    - [ ] Information needs mapped
    - [ ] Career motivations documented

  unit_economics:
    - [ ] ACV ranges defined
    - [ ] CAC by segment estimated
    - [ ] LTV with retention assumptions
    - [ ] Sales cycle impact on economics

  competitive:
    - [ ] Feature comparison matrix
    - [ ] Pricing model comparison
    - [ ] G2/analyst positioning
    - [ ] Win/loss intelligence

  marketing:
    - [ ] ABM tier structure recommended
    - [ ] Channel strategy by buyer stage
    - [ ] Content needs by persona
    - [ ] Event/conference strategy

  enablement:
    - [ ] Sales deck requirements
    - [ ] ROI calculator inputs
    - [ ] Objection handling framework
    - [ ] Reference/case study needs
```

---

*End of B2B Domain Overlay*
