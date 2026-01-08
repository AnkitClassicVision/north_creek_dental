# Deep Research Request: Comprehensive Market & Funnel Analysis

## RESEARCH PROJECT NAME
**Single Service:** `[COMPANY_SHORTNAME]_[SERVICE]_Analysis`
*Example: EVEA_Aesthetics_Analysis*

**Multiple Services:** `[COMPANY_SHORTNAME]_[SERVICE1]_[SERVICE2]_Analysis`
*Example: EVEA_Aesthetics_DryEye_Analysis*

## TASK DEFINITION
Conduct a comprehensive end-to-end market and funnel analysis to build a strategic business plan for **[PRIMARY_SERVICE]** (and **[SECONDARY_SERVICE]** if applicable) at [COMPANY_NAME]. Use Graph of Thoughts (GoT) methodology to explore multiple research paths and synthesize findings.

## INPUT VARIABLES (MUST BE PROVIDED BY USER)

# BEGIN INPUT VARIABLES
```yaml
company:
  name: "Griebenow Eyecare"
  shortname: "GEC"
  website: "https://www.griebenoweyecare.com/"
  addresses:  # Use list format for multiple locations
    - "105 Northridge Dr, New London, WI 54961"
    - "45 10th St, Clintonville, WI 54929"
  
services:
  primary:
    name: "Dry Eye"
    subfolder: "[Dry Eye]"
    specific_offerings: "[List specific services/treatments]"
  secondary: # OPTIONAL - Leave blank if only one service
    name: "[Secondary Service Category or NONE]"
    subfolder: "[Folder name or NONE]"
    specific_offerings: "[List specific services or NONE]"
    
market_area:
  radius_miles: [10]
  radius_time: [25 minutes]
  
research_focus:
  industry: "Optometry"
  b2b_or_b2c: "B2C"
  price_point: " "
```
# END INPUT VARIABLES

## COMPANY LOGO RETRIEVAL

### Logo Extraction Process
**IMPORTANT: Extract the company logo from their website for use in the research website.**

```yaml
logo_retrieval:
  source: Company website URL (from INPUT VARIABLES above)
  output_folder: /RESEARCH/images/
  naming_convention: "[COMPANY_SHORTNAME]_logo.png"
  # Example: GEC_logo.png

  extraction_steps:
    1. Visit the company website URL specified in INPUT VARIABLES
    2. Locate the company logo (typically in header or footer)
    3. Download/extract the logo image in highest quality available
    4. Save to /RESEARCH/images/[COMPANY_SHORTNAME]_logo.png
    5. Also copy to /website/assets/images/[COMPANY_SHORTNAME]_logo.png for website use

  preferred_formats:
    - PNG (transparent background preferred)
    - SVG (if available, ideal for scalability)
    - JPG (acceptable if others unavailable)

  usage_locations:
    - Website header/navigation
    - Executive summary page
    - Footer across all pages
```

## DYNAMIC FOLDER STRUCTURE GENERATION

### Base Structure Template
The folder structure will automatically adapt based on your input services and company:

**For Single Service:**
```
RESEARCH/
├── images/                           # Persona headshot images (generated via nanobanana)
│   ├── [COMPANY_SHORTNAME]_logo.png  # Company logo from website
│   ├── [persona1_slug]_headshot.png
│   ├── [persona2_slug]_headshot.png
│   └── ...
└── [COMPANY_SHORTNAME]_[SERVICE]_Analysis/
```

**For Multiple Services:**
```
RESEARCH/
├── images/                           # Persona headshot images (generated via nanobanana)
│   ├── [persona1_slug]_headshot.png
│   ├── [persona2_slug]_headshot.png
│   └── ...
└── [COMPANY_SHORTNAME]_[SERVICE1]_[SERVICE2]_Analysis/
    ├── README.md
    ├── PROGRESS.md
    ├── 01_Executive_Summary/
    │   └── Executive_Summary.md
    ├── 02_Market_Analysis/
    │   ├── Demographics_Analysis.md
    │   ├── Market_Size_Trends.md
    │   └── [INDUSTRY_SPECIFIC].md  # e.g., Insurance_Landscape.md for healthcare
    ├── 03_Persona_Research/
    │   ├── [SERVICE1]_Personas.md  # e.g., Aesthetic_Personas.md
    │   ├── [SERVICE2]_Personas.md  # Only if SERVICE2 exists
    │   └── Language_Patterns.md
    ├── 04_Competition_Analysis/
    │   ├── Competitor_Matrix.md
    │   ├── Pricing_Analysis.md
    │   └── Service_Gaps.md
    ├── 05_Marketing_Funnels/
    │   ├── [SERVICE1]_Funnels.md
    │   ├── [SERVICE2]_Funnels.md  # Only if SERVICE2 exists
    │   └── Funnel_Metrics.md
    ├── 06_Content_Library/
    │   ├── Email_Templates.md
    │   ├── Social_Content.md
    │   └── Ad_Creative.md
    ├── 07_Strategic_Opportunities/
    │   └── [INDUSTRY]_Partnerships.md  # e.g., Local_Partners.md
    ├── 08_Digital_Strategy/
    │   └── Paid_Ads_Strategy.md
    ├── 09_Financial_Projections/
    │   └── Revenue_Models.md
    ├── 10_Raw_Research/
    │   ├── Agent01_Demographics.md
    │   ├── Agent02_[SERVICE1]_Market.md
    │   ├── Agent03_[SERVICE2]_Market.md  # Or Industry_Analysis if no SERVICE2
    │   ├── Agent04_[INDUSTRY]_Trends.md
    │   ├── Agent05_Economic_Analysis.md
    │   ├── Agent06-10_Competitors.md
    │   ├── Agent11-16_Personas.md
    │   ├── Agent17-20_Digital_Intelligence.md
    │   ├── Agent21-25_Content_Strategy.md
    │   └── Agent26-30_Implementation.md
    └── 11_Data_Visualizations/
        └── Market_Charts.md
```

## DYNAMIC CONTENT GENERATION RULES

### Service-Adaptive Research Agents

Based on the services you specify, the system will automatically deploy appropriate research agents:

#### For Healthcare Services:
```yaml
if industry == "Healthcare":
  deploy_agents:
    - Insurance_Coverage_Analysis
    - Clinical_Regulations_Research
    - Medical_Referral_Networks
    - HIPAA_Compliance_Review
```

#### For Retail/E-commerce:
```yaml
if industry == "Retail":
  deploy_agents:
    - Inventory_Turnover_Analysis
    - Seasonal_Trend_Research
    - Supply_Chain_Evaluation
    - Customer_Lifetime_Value
```

#### For Professional Services:
```yaml
if industry == "Professional":
  deploy_agents:
    - B2B_Decision_Makers
    - Contract_Value_Analysis
    - Enterprise_Sales_Cycles
    - Partnership_Ecosystems
```

#### For Technology/SaaS:
```yaml
if industry == "Technology":
  deploy_agents:
    - Feature_Comparison_Matrix
    - Integration_Capabilities
    - API_Documentation_Review
    - Developer_Community_Analysis
```

### Dynamic Persona Generation

The system will create personas based on your service categories:

```markdown
## Persona Structure for [SERVICE1]

### Persona Name Formula:
"[First Name] [Last Name] - The [Service] [Archetype]"



### Persona Count Logic:
- Single Service Only: Generate 4-6 personas for comprehensive coverage
- Dual Services: Generate 2-3 personas per service
- Multi-Service: Generate 2 personas per primary service, 1 per secondary

### If No Secondary Service:
- Focus all persona development on primary service
- Create more detailed sub-segments within primary service
- Include edge cases and niche segments
```

### Industry-Specific File Generation

#### Healthcare Industry Files:
```
02_Market_Analysis/
├── Demographics_Analysis.md
├── Insurance_Landscape.md        # Healthcare specific
├── Regulatory_Compliance.md      # Healthcare specific
└── Referral_Network_Analysis.md  # Healthcare specific
```

#### Retail/E-commerce Files:
```
02_Market_Analysis/
├── Demographics_Analysis.md
├── Shopping_Behavior_Analysis.md  # Retail specific
├── Seasonal_Trends.md            # Retail specific
└── Competition_Density.md        # Retail specific
```

#### B2B Services Files:
```
02_Market_Analysis/
├── Business_Demographics.md      # B2B specific
├── Industry_Verticals.md         # B2B specific
├── Decision_Maker_Analysis.md    # B2B specific
└── Sales_Cycle_Research.md       # B2B specific
```

## ADAPTIVE CONTENT TEMPLATES

### Dynamic Executive Summary Structure

**For Single Service:**
```markdown
# Executive Summary: [COMPANY_NAME] [SERVICE] Analysis

## 1. Market Opportunity Overview
- Total Addressable Market: $[Amount]
- Serviceable Addressable Market: $[Amount]
- Serviceable Obtainable Market: $[Amount]
- Growth projection: [X]% CAGR

## 2. Key Market Findings
[7-10 bullet points about market opportunity]

## 3. Service Deep Dive
[Comprehensive analysis of the single service]
```

**For Multiple Services:**
```markdown
# Executive Summary: [COMPANY_NAME] [SERVICE1] & [SERVICE2] Analysis

## 1. Market Opportunity Overview
- Total Addressable Market for [SERVICE1]: $[Amount]
- Total Addressable Market for [SERVICE2]: $[Amount]
- Combined market opportunity: $[Amount]
- Growth projection: [X]% CAGR

## 2. Key Findings for [SERVICE1]
[5 bullet points specific to SERVICE1]

## 3. Key Findings for [SERVICE2]
[5 bullet points specific to SERVICE2]

## 4. Target Personas Summary
[Dynamic list based on services provided]

## 5. Competitive Landscape
[Adjusted for industry type]

## 6. [INDUSTRY]-Specific Insights
[Healthcare: Regulatory considerations]
[Retail: Seasonal opportunities]
[B2B: Enterprise sales approach]
[Technology: Integration requirements]
```

### Service-Specific Funnel Templates

```markdown
# [SERVICE1] Marketing Funnel

## Funnel Stages (Adapt based on service type)

### B2C Services (Healthcare, Retail, Personal Services):
1. AWARENESS - Problem recognition
2. CONSIDERATION - Solution research
3. EVALUATION - Provider comparison
4. PURCHASE - Transaction decision
5. ONBOARDING - First experience
6. RETENTION - Continued engagement
7. ADVOCACY - Referral generation

### B2B Services (Enterprise, SaaS, Professional):
1. AWARENESS - Business challenge identification
2. DISCOVERY - Solution exploration
3. EVALUATION - Vendor assessment
4. NEGOTIATION - Terms and pricing
5. IMPLEMENTATION - Rollout and training
6. ADOPTION - User engagement
7. EXPANSION - Upsell and renewal

### Stage Details for [SERVICE1]
[Dynamically generated based on service type]
```

## RESEARCH EXECUTION FRAMEWORK

### Multi-Agent Deployment Strategy (30 Agents)

The agent deployment will automatically adjust based on your inputs:

```yaml
agent_allocation_single_service:  # Total: 30 agents
  market_foundation: 5 agents
    - Demographics (always)
    - [SERVICE]_Market_Research (2 agents for depth)
    - [INDUSTRY]_Specific_Analysis
    - Economic_Trends (always)

  competitive_intelligence: 5 agents
    - [SERVICE]_Direct_Competitors (2 agents)
    - Indirect_Competitors
    - Pricing_Intelligence
    - Differentiation_Opportunities

  persona_development: 6 agents
    - Generate 4-6 personas for single service

  digital_intelligence: 4 agents
    - Social_Listening
    - Online_Communities
    - Search_Behavior
    - Content_Gaps

  strategy_development: 10 agents
    - Content_Strategy (2 agents)
    - Partnership_Opportunities (2 agents)
    - Customer_Journey_Mapping (2 agents)
    - Implementation_Roadmap (2 agents)
    - Revenue_Modeling (2 agents)

agent_allocation_multi_service:  # Total: 30 agents
  market_foundation: 5 agents
    - Demographics (always)
    - [SERVICE1]_Market_Research
    - [SERVICE2]_Market_Research
    - [INDUSTRY]_Specific_Analysis
    - Economic_Trends (always)
    
  competitive_intelligence: 5 agents
    - [SERVICE1]_Direct_Competitors
    - [SERVICE2]_Direct_Competitors
    - Indirect_Competitors
    - Pricing_Intelligence
    - Differentiation_Opportunities
    
  persona_development: 6 agents
    - Generate 2-3 personas per service
    
  digital_intelligence: 4 agents
    - Social_Listening
    - Online_Communities
    - Search_Behavior
    - Content_Gaps
    
  strategy_development: 10 agents
    - Content_Strategy (2 agents)
    - Partnership_Opportunities (2 agents)
    - Customer_Journey_Mapping (2 agents)
    - Implementation_Roadmap (2 agents)
    - Revenue_Modeling (2 agents)
```

### Dynamic Research Questions

The system will generate research questions based on your service inputs:

```python
research_questions = {
    "healthcare": [
        "What insurance covers [SERVICE1]?",
        "What are the clinical outcomes for [SERVICE2]?",
        "What regulations govern these services?",
        "What is the referral pattern in the area?"
    ],
    "retail": [
        "What is the average transaction value for [SERVICE1]?",
        "What is the purchase frequency for [SERVICE2]?",
        "What are the seasonal patterns?",
        "What is the local competition density?"
    ],
    "b2b": [
        "What is the typical contract value for [SERVICE1]?",
        "What is the sales cycle length for [SERVICE2]?",
        "Who are the decision makers?",
        "What are the implementation requirements?"
    ],
    "technology": [
        "What integrations are required for [SERVICE1]?",
        "What is the technical expertise needed for [SERVICE2]?",
        "What are the security requirements?",
        "What is the typical deployment timeline?"
    ]
}
```

## PERSONA DEVELOPMENT FRAMEWORK

### Persona Headshot Image Generation

**IMPORTANT: Generate photorealistic headshot images for each persona using the nanobanana skill.**

After creating each persona, use the nanobanana skill to generate a photorealistic headshot image that represents the persona. These images will be used on the website to visually represent each target customer segment.

```yaml
image_generation:
  tool: nanobanana skill
  output_folder: /RESEARCH/images/
  naming_convention: "[PERSONA_NAME_SLUG]_headshot.png"
  # Example: busy_professional_brian_headshot.png

  image_requirements:
    style: "photorealistic professional headshot"
    background: "neutral or softly blurred"
    lighting: "professional studio lighting"
    expression: "approachable and authentic"

  prompt_template: |
    "Generate a photorealistic professional headshot photograph of a
    [AGE] year old [GENDER] [ETHNICITY] person who is a [OCCUPATION/ROLE].
    They should appear [KEY_PERSONALITY_TRAITS].
    Professional studio lighting, neutral background, high quality portrait."

  example_prompts:
    - "Generate a photorealistic professional headshot photograph of a 45 year old female Caucasian working professional. She should appear confident, busy, and health-conscious. Professional studio lighting, neutral background, high quality portrait."
    - "Generate a photorealistic professional headshot photograph of a 62 year old male African American retiree. He should appear wise, active, and approachable. Professional studio lighting, neutral background, high quality portrait."

execution_steps:
  1. Complete persona research and documentation
  2. For each persona, invoke the nanobanana skill
  3. Provide a detailed prompt based on persona demographics
  4. Save generated image to /RESEARCH/images/[persona_slug]_headshot.png
  5. Update persona documentation with image path reference
  6. Verify all images are saved before proceeding to website generation
```

### Dynamic Persona Attributes by Industry

```yaml
healthcare_personas:
  demographic_focus:
    - Age and life stage
    - Race & Ethnicity
    - Health conditions
    - Insurance coverage
    - Healthcare spending
  psychographic_focus:
    - Health consciousness
    - Treatment preferences
    - Trust in medical providers
    - Preventive vs. reactive care
    - Online and offline local channels where they spend time
    - Words they use as pain points from local online sources

retail_personas:
  demographic_focus:
    - Income and discretionary spending
    - Race & Ethnicity
    - Shopping frequency
    - Brand loyalty
    - Channel preferences
    - Online and offline local channels where they spend time
  psychographic_focus:
    - Price sensitivity
    - Quality expectations
    - Social shopping behavior
    - Environmental consciousness

b2b_personas:
  demographic_focus:
    - Company size
    - Race & Ethnicity
    - Industry vertical
    - Role and seniority
    - Budget authority
  psychographic_focus:
    - Risk tolerance
    - Innovation adoption
    - Vendor preferences
    - Success metrics

technology_personas:
  demographic_focus:
    - Technical expertise
    - Race & Ethnicity
    - Team size
    - Stack preferences
    - Implementation capacity
  psychographic_focus:
    - Build vs. buy preference
    - Open source affinity
    - Security priorities
    - Scalability needs
```

### Service-Specific Journey Mapping

```markdown
## Journey Stages for [SERVICE1]

### Healthcare Service Journey:
1. Symptom Recognition → 2. Provider Research → 3. Insurance Check → 
4. Appointment Booking → 5. Treatment → 6. Follow-up → 7. Maintenance

### Retail Product Journey:
1. Need Identification → 2. Product Discovery → 3. Comparison Shopping → 
4. Purchase Decision → 5. Delivery/Pickup → 6. Usage → 7. Repurchase

### B2B Service Journey:
1. Problem Definition → 2. Solution Research → 3. Vendor Evaluation → 
4. Proof of Concept → 5. Contract Negotiation → 6. Implementation → 7. Renewal

### Technology Solution Journey:
1. Technical Requirements → 2. Solution Architecture → 3. Vendor Selection → 
4. Technical Validation → 5. Deployment → 6. Optimization → 7. Scaling
```

## COMPETITIVE ANALYSIS ADAPTATION

### Industry-Specific Competitive Factors

```yaml
competitive_dimensions:
  healthcare:
    - Clinical outcomes
    - Insurance acceptance
    - Wait times
    - Provider credentials
    - Technology/equipment
    - Patient experience
    
  retail:
    - Price points
    - Product selection
    - Convenience/location
    - Customer service
    - Return policy
    - Loyalty programs
    
  b2b:
    - Feature set
    - Integration capabilities
    - Support quality
    - Contract terms
    - Implementation time
    - ROI metrics
    
  technology:
    - Technical specifications
    - API capabilities
    - Security features
    - Scalability
    - Documentation quality
    - Community support
```

## FINANCIAL MODELING ADAPTATION

### Revenue Model Templates by Service Type

```markdown
## Revenue Projections for [SERVICE1]

### Transaction-Based Services (Healthcare, Retail):
- Average transaction value: $[Amount]
- Transactions per customer per year: [Number]
- Customer acquisition cost: $[Amount]
- Customer lifetime value: $[Amount]
- Gross margin: [X]%

### Subscription Services (SaaS, Memberships):
- Monthly recurring revenue per user: $[Amount]
- Annual contract value: $[Amount]
- Churn rate: [X]%
- Expansion revenue: [X]%
- CAC payback period: [X] months

### Project-Based Services (Consulting, Professional):
- Average project value: $[Amount]
- Projects per client per year: [Number]
- Utilization rate: [X]%
- Hourly/daily rate: $[Amount]
- Pipeline conversion: [X]%
```

## QUALITY ASSURANCE CHECKLIST

Adaptive checklist based on inputs:

- [ ] All folder names reflect actual [SERVICE1] and [SERVICE2]
- [ ] Industry-specific files are included ([INDUSTRY] analysis files)
- [ ] Personas match the service categories (minimum 2 per service)
- [ ] Funnels appropriate for B2B/B2C model
- [ ] Competitive factors relevant to [INDUSTRY]
- [ ] Financial model matches service delivery type
- [ ] All agent reports align with specified services
- [ ] Marketing strategies fit the target market
- [ ] Partnerships relevant to [INDUSTRY] and location
- [ ] Compliance/regulatory sections if healthcare
- [ ] Technical specifications if technology
- [ ] Seasonal analysis if retail

## EXECUTION COMMAND TEMPLATE

To begin research, provide this information and execute:

**For Single Service:**
```yaml
# Fill in these variables:
COMPANY_NAME: "[Your Company]"
COMPANY_SHORTNAME: "[Abbreviation]"
SERVICE: "[Primary Service]"
SERVICE_FOLDER: "[FolderName]"
INDUSTRY: "[Industry Type]"
B2B_OR_B2C: "[Business Model]"
LOCATION: "[City, State]"
RADIUS: "[X miles]"

# Then execute:
"Deep research [COMPANY_NAME] offering [SERVICE] in [LOCATION]. 
Industry type: [INDUSTRY], Model: [B2B_OR_B2C]. 
Create research in /RESEARCH/[COMPANY_SHORTNAME]_[SERVICE_FOLDER]_Analysis/ 
with dynamic structure adapted for this specific service and industry."
```

**For Multiple Services:**
```yaml
# Fill in these variables:
COMPANY_NAME: "[Your Company]"
COMPANY_SHORTNAME: "[Abbreviation]"
SERVICE1: "[Primary Service]"
SERVICE1_FOLDER: "[FolderName1]"
SERVICE2: "[Secondary Service]"
SERVICE2_FOLDER: "[FolderName2]"
INDUSTRY: "[Industry Type]"
B2B_OR_B2C: "[Business Model]"
LOCATION: "[City, State]"
RADIUS: "[X miles]"

# Then execute:
"Deep research [COMPANY_NAME] offering [SERVICE1] and [SERVICE2] in [LOCATION]. 
Industry type: [INDUSTRY], Model: [B2B_OR_B2C]. 
Create research in /RESEARCH/[COMPANY_SHORTNAME]_[SERVICE1_FOLDER]_[SERVICE2_FOLDER]_Analysis/ 
with dynamic structure adapted for these specific services and industry."
```

## EXAMPLES OF DYNAMIC ADAPTATION

### Example 1: Law Firm (Multiple Services)
```yaml
Input:
  company: "Smith & Associates Law Firm"
  services:
    primary: "Estate Planning"
    secondary: "Business Law"
  industry: "Legal Services"
  model: "B2B/B2C Mixed"

Output Structure:
  /RESEARCH/SmithLaw_EstatePlanning_BusinessLaw_Analysis/
  - 03_Persona_Research/
    - EstatePlanning_Personas.md (Retirees, Young Families)
    - BusinessLaw_Personas.md (Startups, SMBs)
  - 07_Strategic_Opportunities/
    - Legal_Referral_Networks.md
    - CPA_Partnerships.md
```

### Example 2: Dental Practice (Single Service)
```yaml
Input:
  company: "Bright Smiles Dental"
  services:
    primary: "Cosmetic Dentistry"
    secondary: NONE
  industry: "Healthcare"
  model: "B2C"

Output Structure:
  /RESEARCH/BrightSmiles_CosmeticDentistry_Analysis/
  - 03_Persona_Research/
    - CosmeticDentistry_Personas.md (5-6 detailed personas)
    - Language_Patterns.md
  - 02_Market_Analysis/
    - Insurance_Landscape.md
    - Regulatory_Compliance.md
  - 10_Raw_Research/
    - Agent02_CosmeticDentistry_Market.md (2 agents for depth)
    - Agent03_Healthcare_Industry_Analysis.md
```

### Example 3: Fitness Studio (Multiple Services)
```yaml
Input:
  company: "CorePower Fitness Studio"
  services:
    primary: "Group Classes"
    secondary: "Personal Training"
  industry: "Fitness/Wellness"
  model: "B2C"

Output Structure:
  /RESEARCH/CorePower_GroupClasses_PersonalTraining_Analysis/
  - 03_Persona_Research/
    - GroupClasses_Personas.md (Millennials, Working Moms)
    - PersonalTraining_Personas.md (Executives, Athletes)
  - 02_Market_Analysis/
    - Seasonal_Membership_Trends.md
    - Local_Gym_Saturation.md
```

### Example 4: IT Consulting (Multiple Services)
```yaml
Input:
  company: "TechForward Consulting"
  services:
    primary: "Cloud Migration"
    secondary: "Cybersecurity"
  industry: "Technology"
  model: "B2B"

Output Structure:
  /RESEARCH/TechForward_CloudMigration_Cybersecurity_Analysis/
  - 03_Persona_Research/
    - CloudMigration_Personas.md (CTOs, IT Directors)
    - Cybersecurity_Personas.md (CISOs, Compliance Officers)
  - 05_Marketing_Funnels/
    - CloudMigration_B2B_Funnel.md (7-stage enterprise sales)
    - Cybersecurity_B2B_Funnel.md (Risk-based approach)
```

### Example 5: Marketing Agency (Single Service)
```yaml
Input:
  company: "Digital Growth Partners"
  services:
    primary: "SEO Services"
    secondary: NONE
  industry: "Marketing/Advertising"
  model: "B2B"

Output Structure:
  /RESEARCH/DigitalGrowth_SEO_Analysis/
  - 03_Persona_Research/
    - SEO_Personas.md (6 detailed B2B personas)
      * Small Business Owner - Local Focus
      * E-commerce Director - National Reach
      * Marketing Manager - Enterprise
      * Startup Founder - Growth Stage
      * Agency Partner - White Label
      * SaaS CMO - Technical SEO
  - 05_Marketing_Funnels/
    - SEO_Funnels.md (B2B enterprise sales cycle)
  - 10_Raw_Research/
    - Agent02_SEO_Market.md (2 dedicated agents)
    - Agent03_Marketing_Industry_Analysis.md
```

## HANDLING SINGLE VS MULTIPLE SERVICES

### When User Provides Only One Service:
1. **Folder Structure:** Simpler naming without SERVICE2
2. **Persona Count:** Increase to 4-6 personas for deeper coverage
3. **Agent Allocation:** Double up on primary service research
4. **Funnel Development:** Create variations for different segments
5. **Content Depth:** More detailed analysis of single service

### Automatic Adjustments for Single Service:
```yaml
if services.secondary == "NONE" or empty:
  - Remove [SERVICE2] from all file paths
  - Allocate 2 research agents to primary service
  - Generate 4-6 personas instead of 2-3
  - Create segment-specific funnels
  - Expand competitive analysis for primary service
  - Deep dive into sub-categories of primary service
```

## FINAL NOTES

This dynamic framework ensures that:
1. **Folder names** automatically reflect your actual services (single or multiple)
2. **File contents** adapt to your industry and business model
3. **Personas** scale appropriately (more for single service, split for multiple)
4. **Research agents** adjust focus based on service count
5. **Marketing funnels** match B2B vs B2C requirements
6. **Financial models** align with your revenue structure
7. **Competitive analysis** uses relevant comparison factors
8. **Single service** gets deeper analysis when no secondary service exists

The system will generate a complete, customized research structure that makes sense for YOUR specific business, whether you have one service or multiple services.
