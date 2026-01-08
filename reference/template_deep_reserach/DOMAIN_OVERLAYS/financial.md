# Financial Domain Overlay

## Overview
This overlay applies to financial services, banking, insurance, investment, and fintech businesses. It enforces regulatory compliance, data verification against official filings, and financial-specific research standards.

## Activation Criteria
Apply this overlay when:
- Services include banking, lending, insurance, or investment products
- Business is regulated by SEC, FINRA, state insurance commissioners, or banking regulators
- Claims involve financial projections, returns, or risk assessments
- Industry: Banking, Insurance, Investment, Wealth Management, Fintech, Mortgage, Credit

---

## Mandatory Data Points

### Regulatory Compliance
- [ ] Primary regulator(s) (SEC, FINRA, OCC, state insurance commissioner)
- [ ] Licensing requirements (Series licenses, insurance licenses)
- [ ] Fiduciary duty status (if applicable)
- [ ] Consumer protection requirements (TILA, RESPA, FCRA)
- [ ] State-specific regulations and licensing
- [ ] Anti-money laundering (AML) considerations

### Financial Data Requirements
- [ ] All financial figures verified against official filings
- [ ] Reporting period clearly stated (Q1 2024, FY2023, etc.)
- [ ] Currency and date normalization
- [ ] Forward-looking statement identification
- [ ] Historical performance with appropriate disclaimers

### Market Data Requirements
- [ ] Market size from reputable financial data providers
- [ ] Growth rates with methodology and source
- [ ] Competitive landscape with market share data
- [ ] Economic indicators affecting the market

---

## Source Requirements

### Primary Sources (Required for C1 Claims)
| Source Type | Priority | Examples |
|-------------|----------|----------|
| SEC EDGAR filings | **Highest** | 10-K, 10-Q, 8-K, proxy statements |
| Federal Reserve data | **High** | FRED, H.8, Flow of Funds |
| Bloomberg/Reuters | **High** | Terminal data, news wire |
| FDIC/OCC data | **High** | Call reports, enforcement actions |
| Company earnings calls | **High** | Transcripts with timestamp |
| Industry associations | **Medium** | ABA, NAIC, ICI data |

### Citation Format Requirements
For financial claims, include:
- **Filing type and date** (10-K FY2023, filed 2/28/2024)
- **Page/exhibit reference** for specific data
- **Reporting period** explicitly stated
- **Restatement status** if applicable

**Example:**
> "Company X reported $2.3B in net revenue for FY2023 [HIGH CONFIDENCE] (10-K, filed 2/28/2024, p. 47)"

### Source Quality Grades (Financial-Specific)
| Grade | Criteria |
|-------|----------|
| **A** | SEC filings, audited financial statements, Federal Reserve data, regulator enforcement actions |
| **B** | Earnings call transcripts, Bloomberg/Reuters terminal data, FDIC call reports |
| **C** | Industry association reports, reputable financial journalism (WSJ, FT, Bloomberg News) |
| **D** | Analyst reports (may have conflicts), company press releases (unaudited) |
| **E** | Social media, anonymous sources, promotional content |

### Fallback Sources (Paywall-Free Alternatives)
When primary sources are behind paywalls, use these free alternatives:

| Source Type | Free Alternative | URL |
|-------------|------------------|-----|
| **Company filings** | SEC EDGAR | sec.gov/edgar |
| **Economic data** | FRED (Federal Reserve) | fred.stlouisfed.org |
| **Bank data** | FDIC BankFind | banks.data.fdic.gov |
| **Consumer complaints** | CFPB Database | consumerfinance.gov/data-research/consumer-complaints |
| **Broker/advisor checks** | FINRA BrokerCheck | brokercheck.finra.org |
| **Insurance data** | NAIC | naic.org |
| **Market data** | Yahoo Finance | finance.yahoo.com |
| **Economic indicators** | BEA/BLS | bea.gov, bls.gov |

### When in Doubt (Regulated Claims Guidance)
**Financial marketing is heavily regulated.** When uncertain:

1. **Performance claims:** ALWAYS include standard disclaimer; never cherry-pick periods
2. **Guarantees:** NEVER guarantee returns or "risk-free" claims
3. **Fee disclosures:** When in doubt, disclose ALL fees; omission is violation
4. **Forward-looking statements:** MUST flag with [FORWARD-LOOKING] and include risk disclaimer
5. **Comparisons:** Only use standardized, apples-to-apples comparisons with source
6. **Testimonials:** Cannot imply guaranteed results; require disclaimer
7. **Accredited investor content:** Verify audience status before sharing non-public offerings
8. **Default action:** When unsure about any financial claim, flag for compliance review before publishing

---

## Forward-Looking Statement Handling

### Identification
Flag any statement that:
- Projects future financial performance
- Estimates market growth or trends
- Uses words like "expects," "anticipates," "projects," "believes"

### Required Treatment
```markdown
## Forward-Looking Statement Protocol

1. **Identify**: Mark all forward-looking statements with [FORWARD-LOOKING]
2. **Source**: Cite the original source (earnings call, analyst day, etc.)
3. **Disclaimer**: Include "This is a forward-looking statement subject to risks and uncertainties"
4. **Risk factors**: Reference where risk factors are disclosed (10-K Item 1A)
5. **Update**: Note if guidance has been updated/withdrawn since original statement
```

---

## Persona Additions

### Required Financial Persona Fields
```yaml
persona_financial_fields:
  financial_sophistication:
    options: ["Novice", "Intermediate", "Sophisticated", "Professional"]
    note: "Determines messaging complexity and compliance requirements"

  risk_tolerance:
    options: ["Conservative", "Moderate", "Aggressive"]

  investment_horizon:
    options: ["Short-term (<1 year)", "Medium-term (1-5 years)", "Long-term (5+ years)"]

  account_types:
    options: ["Checking/Savings", "IRA/401k", "Brokerage", "Trust", "Business"]

  net_worth_segment:
    options: ["Mass market", "Mass affluent ($100K-$1M)", "High net worth ($1M-$10M)", "Ultra high net worth ($10M+)"]

  life_stage_financial:
    options: ["Accumulation", "Pre-retirement", "Retirement", "Wealth transfer"]

  regulatory_status:
    options: ["Retail", "Accredited investor", "Qualified purchaser", "Institutional"]

  decision_influences:
    options: ["Fee sensitivity", "Performance track record", "Brand trust", "Advisor relationship", "Technology/UX"]
```

---

## Marketing Constraints

### Prohibited Claims (DO NOT USE)
- Guaranteed returns or performance
- "Risk-free" investment claims
- Misleading fee disclosures
- Cherry-picked performance periods
- Unsubstantiated "best" claims
- Promises of specific outcomes
- Testimonials implying guaranteed results

### Required Disclaimers
```markdown
## Standard Financial Disclaimers

**Investment Risk:**
"Past performance is not indicative of future results. Investments involve risk, including possible loss of principal."

**FDIC/SIPC:**
"[Deposits/Securities] [are/are not] FDIC insured. [Are/Are not] bank guaranteed. May lose value."

**Not Advice:**
"This information is for educational purposes only and is not intended as investment advice. Consult a qualified financial advisor."

**Fee Disclosure:**
"Fees and expenses apply. See [document] for complete fee schedule."

**Forward-Looking:**
"Forward-looking statements are subject to risks and uncertainties. Actual results may differ materially."
```

### Performance Reporting Rules
- Must show standardized time periods (1yr, 3yr, 5yr, 10yr, since inception)
- Must include benchmark comparison
- Must be net of fees (or clearly disclosed as gross)
- Must include worst-period performance
- Cannot cherry-pick favorable periods

---

## Competitive Intelligence

### Financial-Specific Sources
- **SEC EDGAR:** All public company filings
- **FINRA BrokerCheck:** Advisor backgrounds, disciplinary history
- **State insurance commissioner:** Company ratings, complaints
- **AM Best/Moody's/S&P:** Credit ratings
- **J.D. Power:** Customer satisfaction rankings
- **NPS benchmarks:** Industry comparison data

### Competitive Analysis Requirements
- [ ] Fee comparison (apples-to-apples)
- [ ] Performance comparison (standardized periods)
- [ ] Product feature comparison
- [ ] Regulatory standing comparison
- [ ] Customer satisfaction comparison
- [ ] Technology/UX comparison
- [ ] Financial strength ratings

---

## Numeric Audit (Financial-Specific)

### Required Verifications
```yaml
financial_numeric_audit:
  - field: "Revenue/AUM/deposits"
    verify_against: "10-K or quarterly filing"
    check: "Period matches, currency correct, restatement status"

  - field: "Growth rates"
    verify_against: "Calculated from filing data"
    check: "Period-over-period consistent, methodology disclosed"

  - field: "Market share"
    verify_against: "Industry report or filing"
    check: "Denominator defined, period stated"

  - field: "Performance returns"
    verify_against: "Audited performance report"
    check: "Net vs gross, time periods, benchmark"

  - field: "Fee quotes"
    verify_against: "Current fee schedule/prospectus"
    check: "All fees included, effective date"
```

---

## Red Flags (Automatic Review Triggers)

If research uncovers any of these, flag for user attention:

1. **Regulatory Issues:**
   - FINRA/SEC enforcement actions
   - State regulatory orders
   - Consumer complaints (CFPB database)
   - Material weaknesses in internal controls

2. **Financial Health:**
   - Credit rating downgrades
   - Going concern opinions
   - Significant restatements
   - Unusual auditor changes

3. **Compliance Concerns:**
   - Misleading advertising (competitor or client)
   - Fee disclosure gaps
   - Suitability concerns

---

## Skill Integration

### perplexity Usage for Financial
- Search SEC EDGAR for specific filings
- Find regulatory enforcement actions
- Verify financial news accuracy
- Research industry benchmarks

### codex Usage for Financial
- Audit financial claim accuracy against filings
- Verify calculation methodologies
- Check disclaimer compliance
- Review for prohibited marketing claims

---

## Checklist: Financial Research Complete

```yaml
financial_completion_checklist:
  regulatory:
    - [ ] Primary regulator(s) identified
    - [ ] Licensing requirements documented
    - [ ] Advertising restrictions noted
    - [ ] Required disclaimers drafted

  data_verification:
    - [ ] All financial figures verified against filings
    - [ ] Reporting periods explicit
    - [ ] Forward-looking statements flagged
    - [ ] Performance data standardized

  personas:
    - [ ] Financial sophistication level identified
    - [ ] Risk tolerance profiled
    - [ ] Regulatory status (retail/accredited) noted
    - [ ] Decision influences documented

  marketing:
    - [ ] Disclaimers complete
    - [ ] Performance presentation compliant
    - [ ] Fee disclosures accurate
    - [ ] Prohibited claims avoided

  competitive:
    - [ ] FINRA BrokerCheck reviewed (if applicable)
    - [ ] Fee comparison apples-to-apples
    - [ ] Performance comparison standardized
    - [ ] Regulatory standing compared
```

---

*End of Financial Domain Overlay*
