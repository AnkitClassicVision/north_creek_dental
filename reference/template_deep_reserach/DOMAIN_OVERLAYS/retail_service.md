# Retail & Service Domain Overlay

## Overview
This overlay applies to retail businesses, local services, hospitality, and consumer-facing service businesses. It emphasizes local market dynamics, seasonal patterns, review platforms, and local SEO considerations.

## Activation Criteria
Apply this overlay when:
- Business serves local/regional customers directly
- Location and convenience are key purchase factors
- Online reviews significantly impact customer acquisition
- Industry: Retail, Restaurants, Salons, Auto Services, Home Services, Fitness, Hospitality

---

## Mandatory Data Points

### Local Market Data
- [ ] Trade area definition (radius, drive time, natural boundaries)
- [ ] Population within trade area
- [ ] Household income distribution
- [ ] Age demographics
- [ ] Commuter patterns and traffic flow
- [ ] Daytime vs. residential population
- [ ] Growth/decline trends in trade area

### Consumer Behavior Data
- [ ] Shopping patterns (weekday vs. weekend, time of day)
- [ ] Seasonal demand variation
- [ ] Purchase frequency benchmarks
- [ ] Average transaction value
- [ ] Customer lifetime value estimates
- [ ] Repeat visit patterns

### Foot Traffic & Location Data
- [ ] Foot traffic patterns (if physical location)
- [ ] Parking availability impact
- [ ] Visibility from major roads
- [ ] Co-tenancy effects (nearby businesses)
- [ ] Anchor tenant influence (for retail centers)

---

## Source Requirements

### Primary Sources (Required for C1 Claims)
| Source Type | Priority | Examples |
|-------------|----------|----------|
| Census Bureau | **High** | ACS data, Business Patterns |
| Bureau of Labor Statistics | **High** | Employment, consumer expenditure |
| State/local economic data | **High** | Dept. of Commerce, regional reports |
| Industry associations | **Medium** | NRF, NRA, specific trade associations |
| Location intelligence | **Medium** | Placer.ai, SafeGraph (for foot traffic) |
| Review platforms | **Medium** | Google, Yelp (for sentiment/competitive) |

### Local Data Verification
For local market claims, cross-reference:
- Census Bureau American Community Survey (5-year estimates)
- County business patterns
- Local chamber of commerce data
- Regional economic development reports

### Source Quality Grades (Retail/Service-Specific)
| Grade | Criteria |
|-------|----------|
| **A** | Census Bureau, BLS, audited company financials |
| **B** | Industry association reports, major market research firms |
| **C** | Local economic development reports, trade publications |
| **D** | Review platform aggregates, local news |
| **E** | Anecdotal, single-source claims, promotional content |

### Fallback Sources (Paywall-Free Alternatives)
When premium market research is unavailable, use these free alternatives:

| Source Type | Free Alternative | URL |
|-------------|------------------|-----|
| **Demographics** | Census Bureau ACS | data.census.gov |
| **Business patterns** | County Business Patterns | census.gov/programs-surveys/cbp |
| **Consumer spending** | BLS Consumer Expenditure | bls.gov/cex |
| **Economic data** | Data.gov | data.gov |
| **Search trends** | Google Trends | trends.google.com |
| **Foot traffic proxy** | Google Popular Times | maps.google.com |
| **Review data** | Google/Yelp (free tier) | Direct platform access |
| **Local economic data** | State labor departments | [varies by state] |
| **Small business data** | SBA Resources | sba.gov/business-guide |

### When in Doubt (Consumer Protection Guidance)
**Retail/service marketing must comply with consumer protection laws.** When uncertain:

1. **Price claims:** Verify "sale" prices against regular prices; substantiate "lowest price" claims
2. **Review responses:** NEVER incentivize reviews in ways that violate platform TOS
3. **Promotional terms:** Clearly disclose all restrictions, expiration dates, limitations
4. **Gift cards:** Check state-specific expiration and fee rules before marketing
5. **"Free" offers:** Must disclose all conditions; cannot require purchase for "free" item
6. **Testimonials:** If incentivized, must disclose; cannot fabricate reviews
7. **Local claims:** Verify "locally owned," "family-owned," or similar claims are accurate
8. **Default action:** When unsure about promotional claims, verify against FTC guidelines and state consumer protection laws

---

## Seasonal Demand Analysis

### Required Seasonal Documentation
```yaml
seasonal_analysis:
  peak_periods:
    - period: "[Month/Season]"
      demand_index: [100 = baseline]
      drivers: ["Holiday", "Weather", "School schedule", etc.]

  off_peak_periods:
    - period: "[Month/Season]"
      demand_index: [vs. baseline]
      mitigation_strategies: ["Promotions", "Alternative services", etc.]

  weather_sensitivity:
    impact: "[High/Medium/Low]"
    affected_services: ["List specific services"]

  event_driven_demand:
    - event_type: "[Local events, sports, conventions]"
      impact: "[Description]"
```

### Marketing Calendar Integration
Document how seasonal patterns should influence:
- Advertising timing and budget allocation
- Promotional calendar
- Staffing recommendations
- Inventory/capacity planning

---

## Persona Additions

### Required Retail/Service Persona Fields
```yaml
persona_retail_fields:
  shopping_behavior:
    options: ["Browser", "Mission shopper", "Bargain hunter", "Convenience-first", "Experience seeker"]

  price_sensitivity:
    options: ["Price-driven", "Value-conscious", "Quality-first", "Premium/luxury"]

  channel_preference:
    options: ["In-store only", "Online research/in-store buy", "Buy online/pickup in-store", "Online only", "Omnichannel"]

  discovery_method:
    options: ["Drive-by", "Google search", "Social media", "Word of mouth", "Review sites", "Local advertising"]

  loyalty_potential:
    options: ["One-time", "Occasional", "Regular", "Loyal advocate"]

  visit_occasion:
    options: ["Routine/maintenance", "Special occasion", "Emergency/urgent", "Exploratory/trial"]

  time_constraints:
    options: ["Time-rich", "Moderate flexibility", "Time-poor/convenience-critical"]

  local_connection:
    options: ["Long-term resident", "New to area", "Visitor/tourist", "Commuter"]
```

---

## Review & Reputation Analysis

### Platform Coverage (Required)
```yaml
review_platforms:
  google_business:
    priority: "Critical"
    metrics: ["Rating", "Review count", "Response rate", "Recent trend"]

  yelp:
    priority: "High (varies by category)"
    metrics: ["Rating", "Review count", "Elite reviews"]

  facebook:
    priority: "Medium"
    metrics: ["Rating", "Recommendations", "Check-ins"]

  industry_specific:
    - platform: "[TripAdvisor/OpenTable/Angi/etc.]"
      priority: "[Based on category]"
      metrics: ["Relevant metrics"]
```

### Review Sentiment Analysis
Document:
- Common positive themes
- Common negative themes/complaints
- Response patterns and quality
- Comparison to competitors
- Trend over time (improving/declining)

### Review Response Strategy
Include recommendations for:
- Response timing expectations
- Tone and approach
- Handling negative reviews
- Leveraging positive reviews

---

## Local SEO Considerations

### Google Business Profile Optimization
```yaml
gbp_analysis:
  current_status:
    - [ ] Profile claimed and verified
    - [ ] All locations listed
    - [ ] Categories optimized
    - [ ] Hours accurate (including special hours)
    - [ ] Services/products listed
    - [ ] Photos recent and quality
    - [ ] Posts/updates regular

  optimization_opportunities:
    - "[List specific improvements]"

  competitor_gbp_comparison:
    - "[Compare key metrics]"
```

### Local Search Factors
Document:
- "Near me" search volume for category
- Local pack competition
- Review quantity/quality vs. competitors
- Local link opportunities
- Citation consistency issues

---

## Marketing Constraints

### Location-Based Restrictions
- Zoning restrictions on signage
- Noise ordinances (for events/promotions)
- Permit requirements for outdoor activities
- Local advertising restrictions

### Consumer Protection
- State-specific pricing display requirements
- Return policy disclosure requirements
- Gift card regulations
- Promotional terms disclosure

### Platform-Specific Rules
- Google Business Profile guidelines
- Yelp review policies
- Facebook promotional rules
- SMS/text marketing consent requirements

---

## Competitive Intelligence

### Retail/Service-Specific Sources
- **Google Maps/Business Profile:** Location, hours, reviews, photos
- **Yelp:** Reviews, pricing indicators, popular times
- **Social media:** Engagement, content strategy, promotions
- **Mystery shopping:** (If budget allows) Experience comparison
- **Permit records:** New locations, renovations
- **Job postings:** Expansion signals, service offerings

### Competitive Analysis Requirements
- [ ] Location analysis (proximity, accessibility)
- [ ] Pricing comparison (where visible)
- [ ] Service/product offering comparison
- [ ] Hours of operation comparison
- [ ] Review rating and volume comparison
- [ ] Social media presence comparison
- [ ] Promotional strategy comparison
- [ ] Staff/expertise comparison

---

## Funnel Adaptations

### Retail/Service Customer Journey
```
AWARENESS
├── Discovery methods: [Near-me search, drive-by, social, referral]
├── Key metrics: [Impression share, brand search volume]

CONSIDERATION
├── Research behavior: [Review reading, website visit, social check]
├── Key metrics: [Website visits, directions requests]

VISIT/TRIAL
├── Conversion triggers: [Promotion, convenience, availability]
├── Key metrics: [Store visits, appointments, calls]

PURCHASE
├── Transaction factors: [In-store experience, checkout friction]
├── Key metrics: [Conversion rate, average ticket]

RETENTION
├── Loyalty drivers: [Quality, convenience, relationship, rewards]
├── Key metrics: [Return visit rate, loyalty program enrollment]

ADVOCACY
├── Referral triggers: [Exceptional experience, rewards program]
├── Key metrics: [Review rate, referral rate, social shares]
```

---

## Red Flags (Automatic Review Triggers)

If research uncovers any of these, flag for user attention:

1. **Location Issues:**
   - Declining foot traffic in area
   - Major anchor tenant closure
   - Planned road construction affecting access
   - Zoning changes pending

2. **Reputation Issues:**
   - Recent significant negative reviews
   - Declining review trend
   - Health/safety violations (restaurants)
   - BBB complaints

3. **Competitive Threats:**
   - New competitor opening nearby
   - Major competitor renovation/upgrade
   - Disruptive delivery/service model entering market

---

## Skill Integration

### perplexity Usage for Retail/Service
- Research local market demographics
- Find industry benchmark data
- Research competitor openings/closings
- Verify local economic trends

### codex Usage for Retail/Service
- Audit local SEO accuracy
- Verify review platform data
- Check promotional compliance
- Review competitive analysis completeness

---

## Checklist: Retail/Service Research Complete

```yaml
retail_service_completion_checklist:
  local_market:
    - [ ] Trade area defined
    - [ ] Demographics documented
    - [ ] Traffic/accessibility analyzed
    - [ ] Growth trends identified

  seasonal:
    - [ ] Peak/off-peak periods identified
    - [ ] Demand drivers documented
    - [ ] Marketing calendar implications noted

  reviews:
    - [ ] All major platforms analyzed
    - [ ] Sentiment themes documented
    - [ ] Competitor comparison complete
    - [ ] Response strategy recommended

  local_seo:
    - [ ] GBP optimization opportunities identified
    - [ ] Local search competitive position assessed
    - [ ] Citation consistency checked

  personas:
    - [ ] Shopping behavior identified
    - [ ] Price sensitivity assessed
    - [ ] Discovery methods documented
    - [ ] Visit occasions characterized

  competitive:
    - [ ] Location comparison complete
    - [ ] Pricing comparison complete
    - [ ] Review comparison complete
    - [ ] Service offering comparison complete
```

---

*End of Retail & Service Domain Overlay*
