# Website Content Mapping Master Template
## [Business Name] Growth System Website

**Version**: Template 1.0  
**Purpose**: Universal template for transforming market research into website content  
**Target Website**: `/website/[business_folder]/`  
**Research Source**: `/RESEARCH/` directories

---

## Template Usage Instructions

This template can be applied to any business type following this structure:
- Replace `[Business Name]` with actual business name
- Replace `[Industry/Service]` with specific industry (e.g., "Dry Eye Treatment", "Dental Care", "Physical Therapy")
- Replace `[Location]` with geographic area (e.g., "Austin", "Atlanta Metro", "Chicago North Side")
- Follow the calculation methodologies to derive your specific numbers

---

## Table of Contents

1. [Document Setup & Configuration](#1-document-setup--configuration)
2. [Data Source Organization](#2-data-source-organization)
3. [Universal Formatting Standards](#3-universal-formatting-standards)
4. [Calculation Methodologies](#4-calculation-methodologies)
5. [Page Content Templates](#5-page-content-templates)
   - [5.1 Homepage/Overview](#51-homepageoverview)
   - [5.2 Executive Summary](#52-executive-summary)
   - [5.3 Target Personas](#53-target-personas)
   - [5.4 Competitive Analysis](#54-competitive-analysis)
   - [5.5 Marketing Strategy](#55-marketing-strategy)
   - [5.6 Customer Funnels](#56-customer-funnels)
   - [5.7 Strategic Partnerships](#57-strategic-partnerships)
6. [Quality Control Framework](#6-quality-control-framework)
7. [Maintenance Protocol](#7-maintenance-protocol)

---

## 1. Document Setup & Configuration

### Project Variables to Define

```yaml
Business_Info:
  name: "[Your Business Name]"
  website_url: "[URL]"
  address: "[Street Address, City, State ZIP]"
  service_radius: "[X miles or Y minutes]"
  industry: "[Industry/Service Type]"
  
Research_Structure:
  primary_folder: "/RESEARCH/[BusinessName]_[Service]/"
  secondary_folder: "/RESEARCH/[industry]_[location]/"
  competitive_folder: "/RESEARCH/[industry]_competitive_analysis/"
  growth_folder: "/RESEARCH/[industry]_growth_system_[location]/"

Persona_Images:
  source_folder: "/RESEARCH/images/"
  naming_convention: "[persona_slug]_headshot.png"
  # Images are generated during research phase using nanobanana skill
  # Example: busy_professional_brian_headshot.png
  usage: "Map each persona to their corresponding headshot image on the website"
  
Website_Structure:
  root: "/website/[business_folder]/"
  pages:
    - index.html (Overview/Homepage)
    - executive-summary.html
    - personas.html
    - competitive.html
    - marketing.html
    - funnels.html
    - partnerships.html
```

### Required Working Documents

Create these tracking spreadsheets before starting:

1. **Metrics Master Sheet**
   - Tab 1: Raw Data (direct from research)
   - Tab 2: Calculations (show all work)
   - Tab 3: Final Values (for website)
   - Tab 4: Source References

2. **Persona Calculator**
   - Tab 1: Demographics
   - Tab 2: Financial Metrics (LTV, CAC)
   - Tab 3: Market Sizing
   - Tab 4: Journey Mapping

3. **Competitive Matrix**
   - Tab 1: Competitor List
   - Tab 2: Service Comparison
   - Tab 3: Pricing Analysis
   - Tab 4: Gap Identification

---

## 2. Data Source Organization

### Research File Naming Convention

Based on the structure from question.md, your research should follow this pattern:

```
/RESEARCH/
├── images/                            # Persona headshot images (generated via nanobanana)
│   ├── [persona1_slug]_headshot.png   # Photorealistic headshots for website
│   ├── [persona2_slug]_headshot.png
│   └── ...
├── [BusinessName]_[Service]/
│   ├── 00_File_Index.md
│   ├── 01_market_analysis/
│   │   ├── [location]_local_analysis.md
│   │   └── competitive_analysis.md
│   ├── 02_personas/
│   │   ├── detailed_personas.md
│   │   └── persona_economics.md
│   ├── 03_funnel/
│   │   ├── cac_ltv_analysis.md
│   │   └── conversion_metrics.md
│   └── 04_financial_models/
│       ├── scenario_models.md
│       └── revenue_projections.md
```

### Data Hierarchy (Use in Priority Order)

1. **Consolidated Reports** (if available)
2. **Primary Research** `/[BusinessName]_[Service]/`
3. **Growth System Analysis** `/[industry]_growth_system_[location]/`
4. **Competitive Intelligence** `/[industry]_competitive_analysis/`
5. **Supporting Analysis** `/[industry]_[location]/`

### Conflict Resolution Protocol

When data sources conflict:
1. Check timestamp (use most recent)
2. Verify calculation methodology
3. Consider source credibility
4. Document choice and rationale
5. Apply consistently across all pages

---

## 3. Universal Formatting Standards

### Number Formatting Rules

| Data Type | Format Pattern | Example | When to Use |
|-----------|---------------|---------|-------------|
| Large Currency | `$X.XM` or `$XXM` | `$15.2M` | TAM, market size |
| Exact Currency | `$X,XXX` | `$4,738` | LTV, treatment values |
| Rounded Currency | `$X,XX0` | `$3,890` | Simplified display |
| Ratios | `XX:1` or `X.Xx` | `31:1` or `4.3x` | LTV:CAC, ROI |
| Percentages | `XX%` or `XX.X%` | `54%` or `54.2%` | Margins, rates |
| Population | `XXX,XXX` | `187,500` | Customer counts |
| Time Periods | `X.X [unit]` | `2.2 months` | Payback, retention |

### Simplification Guidelines

**Complex → Simple Examples:**
- 28.67:1 → 31:1 (round up for impact)
- 187,462 → 187,500 (round to nearest 500/1000)
- $4,089.37 → $4,100 (round to nearest 50/100)
- 22.4% → 22% (whole number for casual display)

### Localization Requirements

Transform generic content to location-specific:
- Generic: "Allergy treatment" → Local: "[Location] [Specific Allergen] Protocol"
- Standard: "Business hours" → Specific: "Evening/Weekend availability"
- Universal: "Professionals" → Targeted: "[Location] [Industry] corridor workers"

---

## 4. Calculation Methodologies

### A. Total Addressable Market (TAM)

**Formula:**
```
TAM = Population × Condition_Prevalence × Service_Relevance × Annual_Value

Where:
- Population = Census data for service radius
- Condition_Prevalence = Industry research (% affected)
- Service_Relevance = % who would seek treatment
- Annual_Value = Average yearly spend per customer
```

**Example Calculation:**
```
Population (5-mile): 157,225
× Prevalence: 23% = 36,162
× Service Relevance: 25% = 9,040
× Annual Value: $1,680 = $15,187,200
Round to: $15.2M
```

### B. Serviceable Available Market (SAM)

**Formula:**
```
SAM = TAM × Accessibility_Factor × Affordability_Factor

Where:
- Accessibility = % within reasonable distance/time
- Affordability = % who can afford service
```

### C. Serviceable Obtainable Market (SOM)

**Formula:**
```
SOM = SAM × Realistic_Capture_Rate × Time_Period

Where:
- Capture Rate = Your expected market share
- Time Period = Usually Year 1, 3, or 5
```

### D. Lifetime Value (LTV)

**Standard Formula:**
```
LTV = Initial_Transaction + (Repeat_Value × Retention_Rate × Years)

Or more complex:
LTV = Σ(Year_n_Revenue × Retention_Rate^n × Discount_Rate)
```

**Blended LTV Calculation:**
```
Blended_LTV = Σ(Persona_LTV × Persona_Mix_%)

Example:
= (Persona_A $3,850 × 30%)
+ (Persona_B $1,700 × 35%) 
+ (Persona_C $2,100 × 15%)
+ (Persona_D $10,385 × 5%)
+ (Persona_E $4,550 × 15%)
= $3,890
```

### E. Customer Acquisition Cost (CAC)

**Channel-Specific CAC:**
```
CAC = Marketing_Spend / New_Customers_Acquired
```

**Blended CAC:**
```
Blended_CAC = Total_Marketing_Spend / Total_New_Customers

Or weighted:
= Σ(Channel_CAC × Channel_Mix_%)
```

### F. LTV:CAC Ratio

**Formula:**
```
Ratio = LTV / CAC

Benchmarks:
- <1:1 = Losing money
- 1:1 to 3:1 = Breaking even to modest profit
- 3:1 to 5:1 = Healthy
- >5:1 = Excellent (may be under-investing)
```

### G. Payback Period

**Formula:**
```
Payback_Period = CAC / (Average_Revenue_Per_Customer / 12)

Example:
= $143 / ($1,680 / 12)
= $143 / $140
= 1.02 months
```

### H. Conversion Funnel Metrics

**Stage Conversion Formula:**
```
Stage_N_Volume = Stage_N-1_Volume × Conversion_Rate

Example Funnel:
Impressions: 45,000
× CTR 3.2% = Visitors: 1,440
× Engagement 37.5% = Leads: 540
× Qualification 33.3% = Appointments: 180
× Show Rate 70% = New Patients: 126
```

---

## 5. Page Content Templates

## 5.1 Homepage/Overview

### Hero Section Template

#### Four Key Metrics Selection Criteria

**Metric 1: Market Size/TAM**
- **Look for:** Total addressable market calculations
- **Files to check:** 
  - `/market_analysis/[location]_local_analysis.md`
  - `/financial_models/market_sizing.md`
- **Extract:** Largest defensible number
- **Format:** `$XX.XM` with descriptor

**Metric 2: Target Population**
- **Look for:** 
  - Total affected population
  - Key demographic counts
  - Unique local factors (e.g., allergens, industries)
- **Files to check:** 
  - `/market_analysis/` demographics sections
  - Environmental or industry reports
- **Calculation:** Population × Prevalence × Local_Factor
- **Format:** Round to memorable number (nearest 500/1000/5000)

**Metric 3: ROI/Value Metric**
- **Look for:** LTV:CAC ratio, ROI, margins
- **Files to check:** 
  - `/funnel/cac_ltv_analysis.md`
  - `/financial_models/unit_economics.md`
- **Format:** Ratio (XX:1) or percentage

**Metric 4: Operational Excellence**
- **Options:** 
  - Operating margin
  - Payback period
  - Growth rate
  - Retention rate
- **Format:** Most impressive metric for the business

### Quick Stats Dashboard

**Standard Four Cards:**

1. **Market Opportunity**
   ```
   Title: Market Size
   Value: $[SOM] (not TAM - use realistic obtainable)
   Details: "[Time period] revenue potential within [radius]"
   Growth: +XX% YoY (if available)
   ```

2. **Target Segments**
   ```
   Title: Target Segments
   Value: [Number] (typically 3-5)
   List: Top 3 by size or value
   - [Segment 1] ([Count])
   - [Segment 2] ([Count])  
   - [Segment 3] ([Count])
   ```

3. **Unit Economics**
   ```
   Title: Unit Economics
   Value: $[Average LTV]
   Details: "Average customer lifetime value"
   Breakdown: 
   - CAC: $[XXX] avg
   - Payback: [X.X] months
   ```

4. **Growth Projection**
   ```
   Title: Growth Projection
   Value: $[Year 3 Target]
   Timeline:
   - Y1: $[Amount]
   - Y2: $[Amount]
   - Y3: $[Amount]
   ```

### Service/Product Categories

**Structure for Each Category:**
```
Category Name: [Core Offering Area]
Icon: [Relevant emoji or icon class]
Description: [1-2 sentences of benefit-focused copy]
Features: [3 specific offerings]
- [Specific service/feature 1]
- [Specific service/feature 2]  
- [Specific service/feature 3]
```

---

## 5.2 Executive Summary

### Market Opportunity Score

**Component Scoring Framework:**

Each component scored 1-10 based on:

1. **Market Demand (25% weight)**
   ```
   Base: 5.0
   + Size bonus: up to +2.0
   + Growth bonus: up to +1.5
   + Urgency bonus: up to +1.5
   ```

2. **Financial Returns (35% weight)**
   ```
   Base: 5.0
   + LTV:CAC bonus: up to +3.0
   + Margins bonus: up to +1.0
   + Payback bonus: up to +1.0
   ```

3. **Competitive Position (25% weight)**
   ```
   Base: 5.0
   + Differentiation: up to +2.5
   + Market gaps: up to +2.5
   ```

4. **Implementation Risk (15% weight)**
   ```
   Base: 5.0
   + Low capital needs: up to +2.0
   + Proven model: up to +2.0
   + Clear path: up to +1.0
   ```

**Overall Score = Weighted Average**

### Strategic Findings Template

For each finding (typically 3-4):

```
Finding Title: [Compelling Statement]

Highlight Box:
"[Single most important data point or insight]"

Supporting Evidence (4 bullets):
• [Specific metric with context]
• [Comparison to benchmark]
• [Growth or trend data]
• [Unique advantage]
```

### Implementation Roadmap Phases

**Phase 1: Foundation (Months 1-3)**
- 5-7 highest ROI actions
- Quick wins for credibility
- Essential infrastructure
- Target: [Specific metrics]

**Phase 2: Growth (Months 4-12)**
- Scale successful tactics
- Add new channels/segments
- Build partnerships
- Target: [Specific metrics]

**Phase 3: Leadership (Years 2-3)**
- Innovation and differentiation
- Market expansion
- Premium offerings
- Target: [Specific metrics]

---

## 5.3 Target Personas

### Persona Card Structure

**For Each Persona Extract:**

1. **Identity Elements**
   ```
   Name: [Alliterative First Name] [Archetype]
   Image_Path: /RESEARCH/images/[persona_slug]_headshot.png
   # Example: /RESEARCH/images/busy_professional_brian_headshot.png
   # These photorealistic headshots are generated during research using nanobanana skill
   Tagline: [Direct quote capturing their core frustration]
   Subtitle: [Professional/demographic descriptor]
   ```

### Persona Image Mapping

**IMPORTANT: Use the photorealistic headshot images generated during the research phase.**

The persona images are stored in `/RESEARCH/images/` and should be mapped to each persona on the website:

```yaml
persona_image_mapping:
  source_directory: "/RESEARCH/images/"

  mapping_process:
    1. Identify persona slug from persona name (lowercase, underscores)
    2. Locate corresponding image: [persona_slug]_headshot.png
    3. Copy/link image to website assets folder
    4. Reference in persona card HTML/component

  example_mapping:
    persona_name: "Busy Professional Brian"
    persona_slug: "busy_professional_brian"
    image_source: "/RESEARCH/images/busy_professional_brian_headshot.png"
    website_path: "/website/[business_folder]/assets/images/personas/busy_professional_brian_headshot.png"
    html_reference: '<img src="./assets/images/personas/busy_professional_brian_headshot.png" alt="Busy Professional Brian">'

  website_integration:
    - Copy all persona images from /RESEARCH/images/ to website assets
    - Use consistent path structure: /assets/images/personas/
    - Ensure alt text matches persona name for accessibility
    - Optimize images for web if needed (resize, compress)
```

2. **Financial Metrics**
   ```
   LTV: $[Amount] (show calculation)
   CAC: $[Amount] (by primary channel)
   LTV:CAC: [Ratio]:1
   Market Size: [Count] individuals
   ```

3. **Profile Components**
   - **Demographics:** Age, income, location, family
   - **Psychographics:** Values, fears, aspirations
   - **Jobs to Be Done:** 3 functional, 2 emotional
   - **Pain Points:** Top 3 specific frustrations
   - **Best Channels:** Where to reach them
   - **Key Message:** One powerful statement

### Persona Prioritization

**Scoring Formula:**
```
Priority = (LTV × √Market_Size) / CAC

Sort personas by score, assign tiers:
- Tier 1: Top 20% of scores
- Tier 2: Next 30%
- Tier 3: Bottom 50%
```

---

## 5.4 Competitive Analysis

### Market Gap Identification

**For Each Gap:**
```
Gap Name: [Clear descriptor]
Quantification: [Number/percentage]
Evidence: [Specific proof no one serves this]
Opportunity Size: $[Revenue potential]
```

**Standard Gaps to Look For:**
1. **Convenience Gaps:** Hours, location, booking
2. **Specialization Gaps:** Specific conditions/demographics
3. **Technology Gaps:** Equipment, techniques
4. **Pricing Gaps:** Unserved price points
5. **Experience Gaps:** Service, comfort, speed

### Competitor Profiling

**For Each Major Competitor:**
```
Name: [Business name]
Tier: [Premium/Standard/Budget]
Threat Level: [High/Medium/Low]

Key Metrics:
- Wait Time: [Duration]
- Price Range: $[Low]-$[High]
- Distance: [Miles from you]
- Strengths: [Top 2-3]

How We Win:
• [Specific advantage 1]
• [Specific advantage 2]
• [Specific advantage 3]
```

### Competitive Matrix

Create comparison table:
```
| Capability | Us | Comp 1 | Comp 2 | Comp 3 |
|------------|-----|---------|---------|---------|
| [Feature 1] | ✓ | ✗ | ✗ | Partial |
| [Feature 2] | ✓ | ✓ | ✗ | ✗ |
| [Price <$X] | ✓ | ✗ | ✓ | ✗ |
```

---

## 5.5 Marketing Strategy

### Channel Allocation Framework

**Budget Distribution Template:**
```
Total Budget: $[Annual amount]

Channel Breakdown:
1. [Primary Channel]: XX% = $[Amount]
   - Expected Customers: [Count]
   - CAC: $[Amount]
   - ROI: [X.X]x

[Repeat for each channel]
```

**Standard Channel Mix:**
- Digital (40-60%): Search, display, social
- Referral (20-30%): Partners, patients
- Traditional (10-20%): Print, radio, events
- Emerging (10-20%): New platforms, tests

### Persona Messaging Matrix

**For Each Persona × Channel:**
```
[Persona Name]
Core Message: "[Main value prop for them]"

Channel-Specific:
- Search Ad: "[Headline] | [Description]"
- Social Post: "[Hook + emoji strategy]"
- Email Subject: "[Compelling subject line]"
- Landing Page H1: "[Clear value statement]"
```

### Launch Timeline Template

**30-60-90 Day Plan:**

**Days 1-30: Foundation**
- Week 1: [Critical setup tasks]
- Week 2: [Initial campaigns]
- Week 3: [Testing and learning]
- Week 4: [Optimization]
Target: [Metrics]

**Days 31-60: Momentum**
- [Scale what works]
- [Add new channels]
- [Build partnerships]
Target: [Metrics]

**Days 61-90: Scale**
- [Full deployment]
- [Advanced tactics]
- [Measure and adjust]
Target: [Metrics]

---

## 5.6 Customer Funnels

### Funnel Stage Definitions

**Standard 6-Stage Model:**

1. **Awareness**
   - Definition: First exposure to brand
   - Metrics: Impressions, reach
   - Conversion benchmark: 2-5% to Interest

2. **Interest** 
   - Definition: Engaged with content
   - Metrics: Clicks, visits
   - Conversion benchmark: 20-40% to Evaluation

3. **Evaluation**
   - Definition: Actively comparing options
   - Metrics: Time on site, pages viewed
   - Conversion benchmark: 25-35% to Conversion

4. **Conversion**
   - Definition: Takes desired action
   - Metrics: Form fills, bookings
   - Conversion benchmark: 50-70% to Purchase

5. **Purchase/Treatment**
   - Definition: Becomes customer
   - Metrics: Revenue, tickets
   - Conversion benchmark: 70-85% to Retention

6. **Retention/Advocacy**
   - Definition: Repeat and refer
   - Metrics: LTV, NPS, referrals
   - Benchmark: 60-80% retention

### Funnel Calculation Template

```
Stage 1 Volume: [Starting number]
× Conversion Rate = Stage 2 Volume: [Result]
× Conversion Rate = Stage 3 Volume: [Result]
[Continue for all stages]

Validation: Final number should match expected customers/month
```

---

## 5.7 Strategic Partnerships

### Partnership Categories

**Standard Categories:**

1. **Healthcare/Professional Referrals**
   - Target: Related practices
   - Structure: Referral fees or reciprocal
   - Expected yield: [X patients/month]

2. **Corporate/B2B**
   - Target: Large employers
   - Structure: Employee benefits
   - Expected yield: [X patients/month]

3. **Educational Institutions**
   - Target: Schools, universities
   - Structure: Student discounts
   - Expected yield: [X patients/month]

4. **Community Organizations**
   - Target: Local groups
   - Structure: Member benefits
   - Expected yield: [X patients/month]

### Partnership ROI Calculation

```
Partnership Value = (Referrals × LTV) - (Partnership Costs)
Partnership ROI = Value / Costs

Where Costs include:
- Setup time and materials
- Ongoing relationship management
- Referral fees or discounts
- Marketing support
```

---

## 6. Quality Control Framework

### Pre-Launch Checklist

#### Persona Images
- [ ] All persona headshot images generated via nanobanana and saved to /RESEARCH/images/
- [ ] Images copied to website assets folder (/assets/images/personas/)
- [ ] Each persona card displays correct corresponding image
- [ ] Image alt text matches persona name
- [ ] Images optimized for web (appropriate size and compression)

#### Data Validation
- [ ] All calculations documented with source
- [ ] Numbers consistent across all pages
- [ ] Market data within 6 months old
- [ ] Competitive info current
- [ ] Financial projections conservative

#### Content Quality
- [ ] Benefit-focused language
- [ ] Local market specifics included
- [ ] No unsubstantiated claims
- [ ] Professional tone throughout
- [ ] CTAs clear and compelling

#### Technical Validation
- [ ] All formulas compute correctly
- [ ] Ratios and percentages accurate
- [ ] Rounding consistent
- [ ] Charts data properly formatted
- [ ] No broken references

#### Performance Validation (CRITICAL)

**Core Web Vitals Targets:**
- [ ] LCP (Largest Contentful Paint) < 2.5 seconds
- [ ] FID (First Input Delay) < 100ms
- [ ] CLS (Cumulative Layout Shift) < 0.1

**Resource Budgets:**
- [ ] Total page weight < 1.5MB
- [ ] JavaScript bundle < 200KB
- [ ] CSS bundle < 50KB
- [ ] Each persona image < 50KB
- [ ] Total images < 500KB

**Critical Rendering Path:**
- [ ] Critical CSS inlined in `<head>`
- [ ] Non-critical CSS uses preload/onload pattern
- [ ] All scripts use `defer` attribute
- [ ] Font preconnect hints present (`fonts.googleapis.com`, `fonts.gstatic.com`)
- [ ] `font-display: swap` in use

**Image Optimization:**
- [ ] ALL images have `width` and `height` attributes
- [ ] Hero images use `loading="eager"` and `fetchpriority="high"`
- [ ] Below-fold images use `loading="lazy"` and `decoding="async"`
- [ ] WebP format used with JPEG/PNG fallback via `<picture>` element

**Animation Performance:**
- [ ] Aurora blobs use `transform3d` (NOT top/left/width/height)
- [ ] Aurora has `will-change: transform` applied
- [ ] Glass cards apply `will-change` ONLY on `:hover`
- [ ] Only `transform` and `opacity` are animated
- [ ] `@media (prefers-reduced-motion: reduce)` rules present

**Glassmorphism Limits:**
- [ ] `backdrop-filter: blur()` used on MAX 5 elements per page
- [ ] `@supports` fallback for unsupported browsers
- [ ] `isolation: isolate` on all glass cards

**Lazy Loading:**
- [ ] Scroll reveal uses IntersectionObserver API
- [ ] Spotlight cursor effect lazy loads on first interaction
- [ ] SVG sprite used for repeated Lucide icons

### Accuracy Verification

**For Every Number Displayed:**
1. Trace to source document
2. Verify calculation method
3. Check rounding/formatting
4. Confirm context accurate
5. Document in tracking sheet

---

## 7. Maintenance Protocol

### Update Frequency

**Monthly Updates:**
- Competitive changes
- Campaign performance
- Conversion metrics

**Quarterly Updates:**
- Market size revisions
- Persona adjustments
- Financial projections
- Partnership status

**Annual Overhaul:**
- Complete market re-research
- Strategy pivot assessment
- Technology changes
- Full competitive scan

### Change Documentation

**Required for Every Update:**
```
Change Log Entry:
Date: [YYYY-MM-DD]
Page/Section: [Specific location]
Old Value: [Previous content]
New Value: [Updated content]
Source: [Research file or data source]
Reason: [Why changed]
Impact: [Other affected sections]
Approved by: [Name]
```

### Version Control

**Naming Convention:**
- Major: X.0 (annual overhaul)
- Minor: X.Y (quarterly updates)
- Patch: X.Y.Z (corrections)

**Archive Requirements:**
- Keep 3 previous versions
- Document all calculations
- Maintain source references
- Track decision rationales

---

## Appendix: Research Extraction Guide

### What to Look For in Research Files

#### In Market Analysis Files:
- Population demographics
- Income distributions
- Growth trends
- Local unique factors (weather, industry, culture)
- Prevalence/incidence rates
- Competitor listings
- Pricing surveys

#### In Persona Files:
- Demographic details
- Psychographic profiles
- Financial capacity
- Pain points and fears
- Channel preferences
- Journey stages
- Jobs to be done

#### In Financial Models:
- Revenue projections
- Cost structures
- Unit economics
- Scenario planning
- Sensitivity analysis
- Break-even calculations

#### In Competitive Analysis:
- Competitor profiles
- Service comparisons
- Pricing matrices
- SWOT analysis
- Market gaps
- Differentiation opportunities

#### In Funnel/CAC/LTV Analysis:
- Conversion rates by stage
- Channel performance
- Customer acquisition costs
- Lifetime values
- Retention curves
- Cohort analyses

### Data Extraction Template

For systematic extraction, use this format:

```
File: [Path/filename]
Section: [Heading or line numbers]
Raw Data: [Exact extract]
Context: [What this represents]
Calculation: [If derived, show work]
Final Value: [What goes on website]
Notes: [Any caveats or assumptions]
```

---

## Final Implementation Notes

### Success Criteria

A properly implemented mapping should:
1. Transform 100% of research into actionable website content
2. Maintain data consistency across all pages
3. Include local market differentiation
4. Provide clear calculation documentation
5. Enable easy updates and maintenance

### Common Pitfalls to Avoid

1. **Using TAM when SOM is more realistic**
2. **Showing unrounded, overly precise numbers**
3. **Generic messaging without local relevance**
4. **Inconsistent metrics across pages**
5. **Missing source documentation**
6. **Optimistic projections without basis**
7. **Ignoring competitive responses**
8. **Complex jargon over clear benefits**

### Quality Markers

Your final website should have:
- **Clarity:** Grandmother test - would she understand?
- **Credibility:** Every claim backed by data
- **Compelling:** Clear value proposition
- **Consistency:** Same story throughout
- **Current:** Fresh, relevant data
- **Calculable:** Math adds up
- **Convertible:** Clear next steps

---

**Document Status**: Template Ready for Customization
**Version**: 1.0
**Usage**: Replace all bracketed placeholders with actual values