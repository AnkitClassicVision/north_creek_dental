# Healthcare Domain Overlay

## Overview
This overlay applies to healthcare, medical services, wellness, and health-adjacent businesses. It enforces regulatory compliance, clinical evidence standards, and healthcare-specific research requirements.

## Activation Criteria
Apply this overlay when:
- Services include medical treatment, diagnostics, or health consultations
- Business requires medical licensing or certification
- Claims must comply with FDA, HIPAA, or state medical board regulations
- Industry: Healthcare, Medical, Dental, Optometry, Mental Health, Physical Therapy, Wellness

---

## Mandatory Data Points

### Regulatory Compliance
- [ ] HIPAA compliance status and requirements
- [ ] State medical board licensing requirements
- [ ] FDA regulations (if devices/treatments involved)
- [ ] State-specific advertising restrictions (testimonials, guarantees)
- [ ] Insurance and billing codes (CPT, ICD-10)
- [ ] Telehealth regulations (if applicable)

### Clinical Evidence Requirements
- [ ] Evidence-based treatment efficacy data
- [ ] Clinical trial references (if claiming treatment outcomes)
- [ ] Peer-reviewed publication citations
- [ ] Safety data and contraindications (if relevant to marketing)

### Insurance & Payment
- [ ] Insurance acceptance patterns (commercial, Medicare, Medicaid)
- [ ] Out-of-pocket cost ranges
- [ ] Payment plan availability
- [ ] HSA/FSA eligibility

### Provider Credentials
- [ ] Required certifications and board certifications
- [ ] Continuing education requirements
- [ ] Supervision requirements (NP, PA, etc.)

---

## Source Requirements

### Primary Sources (Required for C1 Claims)
| Source Type | Priority | Examples |
|-------------|----------|----------|
| Peer-reviewed journals | **Highest** | JAMA, NEJM, Ophthalmology, specialty journals |
| Government agencies | **High** | CDC, FDA, CMS, NIH, state health departments |
| Professional associations | **High** | AMA, AAO, AAFP, specialty societies |
| Clinical guidelines | **High** | USPSTF, specialty society guidelines |
| Clinical trial registries | **Medium** | ClinicalTrials.gov |

### Citation Format Requirements
For clinical claims, include:
- **PMID** (PubMed ID) for journal articles
- **Study design** (RCT, cohort, case-control, etc.)
- **Sample size** and population
- **Key outcome metrics**

**Example:**
> "Dry eye treatment with [X] showed 60% symptom improvement in 12 weeks [HIGH CONFIDENCE] (Smith et al., JAMA Ophthalmology, 2023, PMID: 12345678; RCT, n=500)"

### Source Quality Grades (Healthcare-Specific)
| Grade | Criteria |
|-------|----------|
| **A** | Systematic reviews, meta-analyses, RCTs from major journals, FDA approvals, CDC guidelines |
| **B** | Cohort studies, official professional society guidelines, CMS data |
| **C** | Case-control studies, expert consensus, reputable medical news |
| **D** | Case reports, conference abstracts, preprints |
| **E** | Anecdotal, patient testimonials for efficacy claims, SEO content |

### Fallback Sources (Paywall-Free Alternatives)
When primary sources are behind paywalls, use these free alternatives:

| Source Type | Free Alternative | URL |
|-------------|------------------|-----|
| **Clinical research** | PubMed/PubMed Central | pubmed.ncbi.nlm.nih.gov |
| **Disease information** | CDC | cdc.gov |
| **Drug information** | FDA Drug Database | accessdata.fda.gov/scripts/cder/daf |
| **Clinical trials** | ClinicalTrials.gov | clinicaltrials.gov |
| **Provider licensing** | State licensing boards | [varies by state] |
| **Medicare data** | CMS Data | data.cms.gov |
| **Health statistics** | CDC WONDER | wonder.cdc.gov |
| **Guidelines** | USPSTF | uspreventiveservicestaskforce.org |

### When in Doubt (Regulated Claims Guidance)
**Healthcare marketing carries significant legal risk.** When uncertain:

1. **Efficacy claims:** Do NOT make claims without peer-reviewed evidence (PMID required)
2. **Testimonials:** ONLY use for service experience (wait times, friendliness), NEVER for treatment outcomes
3. **"Best"/"Leading" claims:** Require third-party verification; when in doubt, omit
4. **Off-label mentions:** Do NOT reference off-label uses in marketing
5. **Guarantees:** NEVER guarantee outcomes; always use "results may vary"
6. **Emergency services:** Verify proper licensing before claiming emergency capability
7. **Default action:** When unsure about any health claim, flag for legal/compliance review before publishing

---

## Persona Additions

### Required Healthcare Persona Fields
```yaml
persona_healthcare_fields:
  insurance_status:
    options: ["Commercial PPO", "Commercial HMO", "Medicare", "Medicare Advantage", "Medicaid", "Uninsured", "HSA/High-Deductible"]

  decision_making_style:
    options: ["Doctor-directed", "Shared decision-making", "Self-directed/researcher", "Family-influenced"]

  health_literacy:
    options: ["Low", "Medium", "High"]
    note: "Affects messaging complexity"

  trust_factors:
    options: ["Doctor recommendation", "Online reviews", "Personal referrals", "Research/evidence", "Brand reputation"]

  access_barriers:
    options: ["Transportation", "Time off work", "Childcare", "Cost/insurance", "Fear/anxiety", "Language"]

  chronic_condition_management:
    note: "If relevant to service"

  caregiver_status:
    options: ["Self", "Caregiver for parent", "Caregiver for child", "Caregiver for spouse"]
```

---

## Marketing Constraints

### Prohibited Claims (DO NOT USE)
- Guarantees of cure or treatment outcomes
- "Best" or superlative claims without substantiation
- Before/after images without proper disclaimers
- Testimonials implying specific treatment outcomes
- Comparative claims vs. competitors without clinical evidence
- Off-label use promotion
- Emergency services claims without proper licensing

### Required Disclaimers
```markdown
## Standard Disclaimers (include as appropriate)

**Results Disclaimer:**
"Individual results may vary. Consult with a qualified healthcare provider to determine if [treatment] is right for you."

**Testimonial Disclaimer:**
"Testimonials represent individual experiences and are not guarantees of results."

**Educational Content:**
"This information is for educational purposes only and is not intended as medical advice."

**Emergency Disclaimer:**
"If you are experiencing a medical emergency, call 911 or go to your nearest emergency room."
```

### Testimonial Rules
- May use testimonials for service experience (wait time, staff friendliness)
- May NOT use testimonials as evidence of treatment efficacy
- Must not cherry-pick only positive outcomes
- Must include results-may-vary disclaimer

---

## Competitive Intelligence

### Healthcare-Specific Sources
- **State medical board:** License verification, disciplinary actions
- **Healthgrades:** Patient reviews, quality metrics
- **Vitals:** Patient reviews
- **ZocDoc:** Availability, patient ratings
- **Medicare Compare:** Quality scores (if applicable)
- **Leapfrog Group:** Hospital safety grades (if applicable)
- **NCQA:** Health plan ratings

### Competitive Analysis Requirements
- [ ] Provider credentials comparison
- [ ] Insurance acceptance comparison
- [ ] Wait time / availability comparison
- [ ] Technology/equipment comparison
- [ ] Outcome data (if publicly available)
- [ ] Patient satisfaction scores
- [ ] Accreditations and certifications

---

## Marketing Channel Considerations

### High-Priority Channels for Healthcare
1. **Google Search (Local)** - "Near me" searches critical
2. **Google Business Profile** - Reviews, hours, booking
3. **Physician referrals** - Often primary acquisition channel
4. **Insurance directories** - Must maintain accurate listings
5. **Health plan partnerships** - Centers of Excellence, preferred providers

### Channel Restrictions
- **Facebook/Meta:** Limited targeting for health conditions
- **Google Ads:** Restricted keywords require certification
- **Email:** HIPAA considerations for patient communication
- **Retargeting:** Cannot retarget based on health conditions

---

## Red Flags (Automatic Review Triggers)

If research uncovers any of these, flag for user attention:

1. **Regulatory Issues:**
   - Medical board complaints or disciplinary actions
   - FDA warning letters
   - HIPAA violation history
   - Pending litigation

2. **Clinical Evidence Gaps:**
   - Claims of efficacy without peer-reviewed evidence
   - Treatments not supported by professional guidelines
   - Off-label use without disclosure

3. **Marketing Compliance:**
   - Competitor using prohibited claims (opportunity or risk?)
   - Social media reviews mentioning outcomes (liability)
   - Website making guarantee claims

---

## Skill Integration

### perplexity Usage for Healthcare
- Search PubMed for clinical evidence
- Find FDA approval status
- Verify CMS coverage decisions
- Check state medical board records

### codex Usage for Healthcare
- Audit clinical claim accuracy
- Verify PMID citations are valid
- Check disclaimer compliance
- Review for prohibited marketing claims

---

## Checklist: Healthcare Research Complete

```yaml
healthcare_completion_checklist:
  regulatory:
    - [ ] HIPAA requirements documented
    - [ ] State licensing requirements identified
    - [ ] Advertising restrictions noted
    - [ ] Insurance/billing codes researched

  clinical:
    - [ ] Treatment efficacy claims have PMID citations
    - [ ] Evidence grades assigned (A-E)
    - [ ] Contraindications/risks noted where relevant

  personas:
    - [ ] Insurance status included
    - [ ] Decision-making style identified
    - [ ] Health literacy considered
    - [ ] Access barriers documented

  marketing:
    - [ ] Disclaimers drafted
    - [ ] Prohibited claims avoided
    - [ ] Channel restrictions noted

  competitive:
    - [ ] Medical board records checked
    - [ ] Quality metrics compared
    - [ ] Review platforms analyzed
```

---

*End of Healthcare Domain Overlay*
