# Legal Domain Overlay

## Overview
This overlay applies to legal services and law firms. It enforces jurisdictional accuracy, case citation standards, ethical compliance, and legal-specific research requirements.

## Activation Criteria
Apply this overlay when:
- Services include legal representation, legal consulting, or paralegal services
- Business is regulated by state bar associations
- Claims involve legal outcomes, case results, or legal strategy
- Industry: Law Firms, Legal Services, Legal Tech, Compliance Services

---

## Mandatory Data Points

### Regulatory Compliance
- [ ] State bar admission requirements
- [ ] Attorney advertising rules (state-specific)
- [ ] Unauthorized practice of law boundaries
- [ ] Fee structure disclosure requirements
- [ ] Client confidentiality requirements
- [ ] Conflict of interest policies

### Practice Area Data
- [ ] Practice areas with specific expertise/credentials
- [ ] Jurisdictions of admission
- [ ] Court admission status (federal, state, specialty)
- [ ] Professional certifications (if applicable)

### Case/Matter Data Requirements
- [ ] Case citations with full Bluebook format
- [ ] Jurisdiction explicitly stated
- [ ] Case status (pending, decided, appealed)
- [ ] Subsequent history checked
- [ ] Binding vs. persuasive authority distinguished

---

## Source Requirements

### Primary Sources (Required for C1 Claims)
| Source Type | Priority | Examples |
|-------------|----------|----------|
| Court opinions | **Highest** | Published opinions, orders |
| Statutes and regulations | **Highest** | U.S.C., C.F.R., state codes |
| Agency guidance | **High** | DOJ, FTC, SEC guidance documents |
| Bar association data | **High** | Disciplinary records, ethics opinions |
| Westlaw/LexisNexis | **High** | Verified legal research platforms |
| Law reviews | **Medium** | Peer-reviewed legal scholarship |

### Citation Format Requirements
Use Bluebook format for all legal citations:

**Case Citation:**
> Smith v. Jones, 123 F.3d 456 (9th Cir. 2023)

**Statute Citation:**
> 15 U.S.C. § 1692 (2023)

**Regulation Citation:**
> 17 C.F.R. § 230.501 (2023)

### Subsequent History Requirements
For any cited case, verify:
- [ ] Has not been overruled
- [ ] Has not been reversed on appeal
- [ ] Is still good law (KeyCite/Shepard's)
- [ ] Note any distinguishing treatment

### Source Quality Grades (Legal-Specific)
| Grade | Criteria |
|-------|----------|
| **A** | Published court opinions (binding authority), statutes, regulations |
| **B** | Unpublished opinions (persuasive), agency guidance, Restatements |
| **C** | Law review articles, treatises, CLE materials |
| **D** | Legal blogs, practice guides, news reports on legal matters |
| **E** | Social media, unverified claims, non-legal sources for legal claims |

### Fallback Sources (Paywall-Free Alternatives)
When Westlaw/LexisNexis are unavailable, use these free alternatives:

| Source Type | Free Alternative | URL |
|-------------|------------------|-----|
| **Case law** | Google Scholar (Cases) | scholar.google.com |
| **Federal cases** | CourtListener | courtlistener.com |
| **Federal court records** | PACER | pacer.uscourts.gov |
| **State statutes** | State legislature sites | [varies by state] |
| **Federal statutes** | U.S. Code (GPO) | uscode.house.gov |
| **Federal regulations** | eCFR | ecfr.gov |
| **Attorney lookup** | State bar websites | [varies by state] |
| **Law reviews** | SSRN Legal | papers.ssrn.com |
| **Supreme Court** | Supreme Court website | supremecourt.gov |

### When in Doubt (Regulated Claims Guidance)
**Legal advertising is state-regulated with significant penalties.** When uncertain:

1. **"Expert"/"Specialist" claims:** Do NOT use unless attorney has official certification (check state rules)
2. **Case results:** ALWAYS include disclaimer; never cherry-pick wins; check state-specific rules
3. **Guarantees:** NEVER guarantee outcomes; always note "each case is different"
4. **Comparisons:** Cannot claim "better than" other attorneys without substantiation
5. **Testimonials:** Check state rules; many states restrict or require disclaimers
6. **Solicitation:** NEVER solicit accident victims directly; check cooling-off periods
7. **Jurisdiction:** ALWAYS state licensed jurisdictions; do not imply practice where not admitted
8. **Default action:** When unsure, check specific state bar advertising rules before publishing; flag for ethics review

---

## Jurisdictional Requirements

### Jurisdiction Tracking
Every legal claim must specify:
- **Jurisdiction:** Federal, state (which state), local
- **Court level:** Trial, appellate, supreme
- **Binding status:** Binding in [jurisdiction] vs. persuasive only

### Circuit Split Flagging
```markdown
## Circuit Split Alert

**Issue:** [Legal question]
**Split:**
- Circuit A position: [View] (cite)
- Circuit B position: [View] (cite)
**Supreme Court status:** [Cert denied/pending/granted/decided]
**Client impact:** [Why this matters for the client's jurisdiction]
```

---

## Persona Additions

### Required Legal Persona Fields
```yaml
persona_legal_fields:
  client_type:
    options: ["Individual", "Small business", "Mid-market company", "Enterprise", "Institutional"]

  matter_urgency:
    options: ["Routine", "Time-sensitive", "Emergency/Urgent"]

  legal_sophistication:
    options: ["First-time legal consumer", "Occasional legal needs", "Sophisticated/repeat client", "In-house counsel"]

  fee_sensitivity:
    options: ["Price-driven", "Value-focused", "Quality-first regardless of cost"]

  engagement_preference:
    options: ["Hourly", "Flat fee", "Contingency", "Hybrid", "Subscription/retainer"]

  decision_factors:
    options: ["Reputation/track record", "Specialization", "Location/convenience", "Price", "Personal referral", "Online reviews"]

  communication_preference:
    options: ["Phone", "Email", "Portal/app", "In-person", "Text"]

  risk_tolerance_legal:
    options: ["Risk-averse (settle early)", "Balanced", "Aggressive (willing to litigate)"]
```

---

## Marketing Constraints

### Prohibited Claims (DO NOT USE)
- Guarantees of legal outcomes
- "Expert" or "specialist" without certification (in most states)
- Misleading case results presentation
- Comparisons to other attorneys without substantiation
- Solicitation of accident victims (ambulance chasing)
- Claims that create unjustified expectations

### State-Specific Advertising Rules
**Note:** Legal advertising rules vary significantly by state. Research the specific state bar rules for:
- Required disclaimers
- Testimonial restrictions
- "Results" advertising requirements
- Filing/submission requirements
- Specialization/certification claims

### Required Disclaimers
```markdown
## Standard Legal Disclaimers

**Results Disclaimer:**
"Past results do not guarantee future outcomes. Each case is different and must be evaluated on its own facts."

**Attorney Advertising:**
"Attorney Advertising. Prior results do not guarantee a similar outcome."

**Not Legal Advice:**
"This information is for general educational purposes only and does not constitute legal advice. For advice specific to your situation, consult a licensed attorney."

**Jurisdiction:**
"Licensed in [STATE(s)]. Not licensed in [other states where advertising may reach]."

**Free Consultation (if offered):**
"Free consultation does not create an attorney-client relationship."
```

### Case Results Presentation
If presenting past case results:
- Must not be misleading or create unjustified expectations
- Should include representative sample, not cherry-picked wins
- Must include disclaimer about individual case variation
- Check state-specific rules on results advertising

---

## Competitive Intelligence

### Legal-Specific Sources
- **State bar websites:** Attorney lookup, disciplinary records
- **PACER/state court records:** Litigation history, outcomes
- **Martindale-Hubbell:** Ratings, peer reviews
- **Avvo:** Client reviews, ratings
- **Super Lawyers/Best Lawyers:** Recognition (verify methodology)
- **Chambers/Legal 500:** Firm rankings (for larger firms)

### Competitive Analysis Requirements
- [ ] Bar standing verification (all attorneys)
- [ ] Disciplinary history check
- [ ] Practice area overlap analysis
- [ ] Fee structure comparison (where available)
- [ ] Client review analysis
- [ ] Notable case/matter comparison
- [ ] Geographic coverage comparison

---

## Research Verification

### Case Citation Verification
```yaml
case_verification:
  - Check case exists in official reporter
  - Verify citation format is correct
  - Run KeyCite/Shepard's for subsequent history
  - Confirm case is still good law
  - Identify any negative treatment
  - Note if case has been distinguished
```

### Statute/Regulation Verification
```yaml
statute_verification:
  - Verify current version (not superseded)
  - Check for recent amendments
  - Confirm effective date
  - Note any pending changes
  - Identify implementing regulations
```

---

## Red Flags (Automatic Review Triggers)

If research uncovers any of these, flag for user attention:

1. **Disciplinary Issues:**
   - Bar disciplinary actions (suspension, disbarment)
   - Malpractice claims
   - Trust account violations
   - Public reprimands

2. **Case Concerns:**
   - Cited case has been overruled
   - Circuit split affects client's jurisdiction
   - Recent statutory changes affect analysis
   - Pending appeals on key precedent

3. **Compliance Issues:**
   - Advertising violations
   - Unauthorized practice concerns
   - Fee agreement issues

---

## Skill Integration

### perplexity Usage for Legal
- Research bar disciplinary records
- Find recent case law developments
- Verify statute/regulation currency
- Research legal market trends

### codex Usage for Legal
- Audit citation format accuracy
- Verify case subsequent history claims
- Check disclaimer compliance
- Review for prohibited advertising claims

---

## Checklist: Legal Research Complete

```yaml
legal_completion_checklist:
  regulatory:
    - [ ] State bar advertising rules researched
    - [ ] Required disclaimers identified
    - [ ] Specialization claim rules verified
    - [ ] Jurisdiction limitations documented

  legal_accuracy:
    - [ ] All case citations verified
    - [ ] Subsequent history checked (KeyCite/Shepard's)
    - [ ] Statutes verified as current
    - [ ] Jurisdictional scope accurate
    - [ ] Binding vs. persuasive distinguished

  personas:
    - [ ] Client type identified
    - [ ] Legal sophistication assessed
    - [ ] Fee preference documented
    - [ ] Decision factors identified

  marketing:
    - [ ] Disclaimers complete and state-compliant
    - [ ] Case results presented appropriately
    - [ ] No prohibited claims
    - [ ] No unjustified expectations created

  competitive:
    - [ ] Bar standing verified for competitors
    - [ ] Disciplinary history checked
    - [ ] Practice areas compared
    - [ ] Client reviews analyzed
```

---

*End of Legal Domain Overlay*
