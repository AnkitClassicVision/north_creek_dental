# Claude.md V3.0 Implementation Plan

## Document Metadata
| Field | Value |
|-------|-------|
| **Created** | December 14, 2025 |
| **Source Files** | claude_1.md, claude_2.md, chatgpt_1.md, chatgpt_2.md, gemini_1.md, gemni_2.md |
| **Priority Sources** | claude_1.md, claude_2.md (per user directive) |
| **Target File** | Claude.md |
| **Status** | COMPLETE |

---

## Executive Summary

This plan transforms the existing Claude.md from a basic 6-phase workflow into a world-class research and website generation system by integrating:
- **9 critical improvements** from claude_1.md (V2 feedback)
- **12 specific implementations** from claude_2.md (V3 enhancements)
- **Evidence-based research systems** from chatgpt files
- **Operational excellence features** from gemini files

### Key Transformations
| From | To |
|------|----|
| Information gathering → Research | Complexity Classification → Intensity Tiers → Hypothesis Formation → Research |
| Basic GoT concept | Full GoT Controller with JSON state, scoring, pruning |
| Single verification pass | Multi-gate verification with Red Team |
| Implicit confidence | Explicit claim confidence scoring (C1/C2/C3) |
| Ad-hoc citations | Evidence Ledger with independence groups |
| No stop rules | Budget-based termination with saturation checks |

---

## Skill Integration Strategy

### Available Skills to Leverage

| Skill | Purpose in Research System | Integration Points |
|-------|---------------------------|-------------------|
| **perplexity** | Deep web searches, source validation, link checking, fact-verification | Phase 2 (Research), Phase 3 (Verification), Red Team searches |
| **codex** | Code reviews, verification audits, second opinions, research validation | Phase 3 (Research Review), Phase 5 (Website Verification) |
| **nanobanana** | Image generation for personas | Phase 2 (Persona Development) |
| **hubspot** | CRM data for B2B research | Phase 2 (Market Analysis, Partnerships) |
| **vercel** | Website deployment | Phase 6 (Deployment) |
| **gmail** | Outreach templates testing | Phase 2 (Marketing Strategy) |
| **frontend-designer** | Website design quality | Phase 4 (Website Generation) |

### Future Skill Integration Points
The system should be designed to automatically leverage any new skills that match these patterns:
- **Research/Search skills**: Integrate into Phase 2 research agents
- **Verification/Audit skills**: Integrate into Phase 3 and Phase 5 verification gates
- **Content generation skills**: Integrate into Phase 4 website generation
- **Deployment skills**: Integrate into Phase 6 deployment pipeline

---

## Implementation Phases

---

## PHASE 1: P0 Critical Foundation Changes

### 1.1 Add Phase 0: Question Complexity Classification

**Description**: Add a pre-research classification phase that routes questions to appropriate process depth.

**Deliverables**:
- [x] New "Phase 0: Question Complexity Classification" section in Claude.md
- [x] Type A/B/C/D classification criteria table
- [x] Classification prompt template
- [x] Process routing logic for each type

**Testing Criteria**:
```yaml
validation:
  - Section exists between "MASTER WORKFLOW" and "PHASE 1"
  - Contains Type A (LOOKUP), Type B (SYNTHESIS), Type C (ANALYSIS), Type D (INVESTIGATION)
  - Each type has: Characteristics, Process, Agents count, Time budget
  - Classification prompt is copy-paste ready
```

**Skill Integration**:
- Use **perplexity** skill for quick Type A lookups (single authoritative source)
- Use **codex** skill to validate classification logic

**Completion Verification**:
```bash
# Search for Phase 0 section
grep -n "Phase 0" Claude.md
# Verify Type classifications exist
grep -c "Type A\|Type B\|Type C\|Type D" Claude.md  # Should return 4+
```

---

### 1.2 Add Phase 1.1: Research Intensity Tiers

**Description**: Add intensity classification after information gathering to set resource allocation.

**Deliverables**:
- [x] New "Step 1.4: Research Intensity Classification" section
- [x] Tier table: Express/Standard/Comprehensive/Enterprise
- [x] Classification criteria YAML with scoring factors
- [x] Updated configuration display format with intensity tier

**Testing Criteria**:
```yaml
validation:
  - Section exists within Phase 1, after Step 1.3
  - Contains 4 tiers with: Trigger Conditions, Agents, Time Budget, Verification method
  - Scoring factors include: service_count, location_count, market_complexity, client_value
  - Configuration display includes "INTENSITY TIER" line
```

**Skill Integration**:
- Classification informs which skills to deploy (e.g., Enterprise tier uses more perplexity searches)

**Completion Verification**:
```bash
grep -n "Research Intensity Classification\|Intensity Tier" Claude.md
grep -c "Express\|Standard\|Comprehensive\|Enterprise" Claude.md  # Should return 4+
```

---

### 1.3 Add Phase 1.5: Hypothesis Formation

**Description**: Add hypothesis generation phase between information gathering and research.

**Deliverables**:
- [x] New "PHASE 1.5: Research Hypothesis Formation" section
- [x] Market hypothesis template (H-M1, H-M2, H-M3)
- [x] Competitive hypothesis template (H-C1, H-C2, H-C3)
- [x] Growth hypothesis template (H-G1, H-G2, H-G3)
- [x] Prior probability assignment structure
- [x] Hypothesis tracking in PROGRESS.md format
- [x] Research directive for hypothesis-driven research

**Testing Criteria**:
```yaml
validation:
  - Section exists between Phase 1 and Phase 2
  - Contains 3 hypothesis categories with 2-3 templates each
  - Prior probability format (0.XX) is specified
  - Confirming/disconfirming evidence requirements defined
  - Test queries requirement included
  - PROGRESS.md hypothesis status table format provided
```

**Skill Integration**:
- Use **perplexity** skill to test hypotheses with targeted searches
- Use **codex** skill to validate hypothesis logic and coverage

**Completion Verification**:
```bash
grep -n "Phase 1.5\|Hypothesis Formation" Claude.md
grep -c "H-M1\|H-C1\|H-G1\|prior_probability\|confirming_evidence\|disconfirming_evidence" Claude.md
```

---

### 1.4 Restore Full GoT Controller

**Description**: Replace minimal GoT description with complete implementation including JSON schema.

**Deliverables**:
- [x] Complete GoT state JSON schema with all fields
- [x] Node types enumeration (root, subquestion, query, source, extract, claim, synthesis, qa)
- [x] Edge types enumeration (supports, contradicts, refines, derived_from)
- [x] Scoring rubric (0-10) with dimension weights
- [x] Pruning rules with thresholds
- [x] Transformation operations: Generate(k), Aggregate(k), Refine(1), RedTeam(1)
- [x] GoT traversal strategy with iteration loop
- [x] graph_state.json file path specification

**Testing Criteria**:
```yaml
validation:
  - got_state.json schema is valid JSON when extracted
  - Contains: metadata, hypotheses, nodes, edges, frontier, budget, checkpoints
  - Scoring rubric includes: relevance, authority, rigor, independence, coherence
  - Pruning rules specify min_score threshold (7.0) and keep_best_per_depth (5)
  - All 4 transformation types documented with agent templates
  - Traversal loop has clear iteration steps and exit conditions
```

**Skill Integration**:
- GoT Controller directs **perplexity** for Generate operations
- GoT Controller uses **codex** for Score/Verify operations

**Completion Verification**:
```bash
grep -n "got_state.json\|graph_state.json" Claude.md
grep -c "Generate(k)\|Aggregate(k)\|Refine(1)\|RedTeam" Claude.md  # Should return 4+
grep -n "min_score\|keep_best" Claude.md
```

---

## PHASE 2: P1 High-Priority Changes

### 2.1 Add Contradiction Triage Protocol

**Description**: Add framework for handling conflicting information from sources.

**Deliverables**:
- [x] Contradiction Triage Protocol section in Phase 2
- [x] Conflict type classification table (Data, Interpretation, Methodological, Temporal)
- [x] Resolution method per conflict type
- [x] Contradiction documentation template
- [x] Hypothesis update rules when conflicts affect hypotheses

**Testing Criteria**:
```yaml
validation:
  - Section exists within Phase 2 research instructions
  - 4 conflict types defined with examples
  - Resolution methods specified for each type
  - Documentation template includes: Topic, Source A, Source B, Conflict Type, Resolution, Confidence, User Note
  - Links to hypothesis probability updates
```

**Skill Integration**:
- Use **perplexity** to find primary sources when data conflicts
- Use **codex** to validate resolution logic

**Completion Verification**:
```bash
grep -n "Contradiction Triage\|Conflict Type" Claude.md
grep -c "Data Disagreement\|Interpretation\|Methodological\|Temporal" Claude.md
```

---

### 2.2 Add Implications Engine

**Description**: Add "So What?" analysis requirement for every major research section.

**Deliverables**:
- [x] Implications Engine section at end of Phase 2 synthesis
- [x] Four-question framework: SO WHAT?, NOW WHAT?, WHAT IF?, COMPARED TO?
- [x] Application table by research section
- [x] Aggregate Agent template update with implications

**Testing Criteria**:
```yaml
validation:
  - Section exists in Phase 2 synthesis requirements
  - All 4 questions defined with clear descriptions
  - Application mapping for: Market Analysis, Personas, Competitive, Funnels, Marketing, Partnerships
  - Template shows how implications flow to website content
```

**Skill Integration**:
- Use **perplexity** to find benchmark data for "COMPARED TO?" analysis

**Completion Verification**:
```bash
grep -n "Implications Engine\|So What" Claude.md
grep -c "SO WHAT\|NOW WHAT\|WHAT IF\|COMPARED TO" Claude.md  # Should return 4+
```

---

### 2.3 Add Enhanced Research Verification Checklist

**Description**: Expand Phase 3 verification with hypothesis, contradiction, confidence, and citation audits.

**Deliverables**:
- [x] Hypothesis verification checklist
- [x] Contradiction verification checklist
- [x] Implications verification checklist
- [x] Confidence scoring verification checklist
- [x] Citation audit checklist with enhanced requirements
- [x] Numerical verification checklist (TAM/SAM/SOM, LTV/CAC, market sizing)
- [x] GoT state verification checklist

**Testing Criteria**:
```yaml
validation:
  - All 7 verification categories present
  - Each category has actionable checkbox items
  - Cross-reference checks included (same number used consistently)
  - GoT state check includes: valid JSON, scores assigned, best path > 8.0
```

**Skill Integration**:
- Use **codex** skill as primary verification engine
- Use **perplexity** to spot-check citation accuracy

**Completion Verification**:
```bash
grep -n "hypothesis_verification\|contradiction_verification\|confidence_scoring" Claude.md
grep -c "\[ \]" Claude.md | head -1  # Count checkbox items (should be 30+)
```

---

### 2.4 Add Checkpoint Aggregation Protocol

**Description**: Add mid-research coordination checkpoint at GoT depth 2.

**Deliverables**:
- [x] Checkpoint Aggregation Protocol section in GoT Controller
- [x] 5-step checkpoint process (PAUSE, COLLECT, ANALYZE, ISSUE, RESUME)
- [x] Analysis criteria: OVERLAP, GAPS, CONTRADICTIONS, DEAD ENDS, HYPOTHESIS UPDATE
- [x] Checkpoint state file path specification

**Testing Criteria**:
```yaml
validation:
  - Section exists within GoT Controller documentation
  - Executes at depth=2 (approximately 50% of Phase 3)
  - All 5 analysis criteria defined with actions
  - Checkpoint file path: /RESEARCH/[topic]/checkpoint_[iteration].json
```

**Completion Verification**:
```bash
grep -n "Checkpoint Aggregation\|CHECKPOINT" Claude.md
grep -c "OVERLAP\|GAPS\|CONTRADICTIONS\|DEAD ENDS\|HYPOTHESIS UPDATE" Claude.md
```

---

## PHASE 3: P2 Medium-Priority Changes

### 3.1 Add Red Team Agent

**Description**: Add mandatory devil's advocate agent for counter-evidence at depth 3+.

**Deliverables**:
- [x] Red Team transformation section alongside Generate/Aggregate/Refine
- [x] Red Team Agent template with search directives
- [x] Deployment trigger (depth 3+ AND aggregate score > 8.0)
- [x] Required output sections (Counterarguments, Methodological concerns, Alternative explanations)
- [x] Updated traversal strategy with mandatory RedTeam
- [x] Updated folder structure with 08_Red_Team/

**Testing Criteria**:
```yaml
validation:
  - Red Team listed as transformation type
  - Agent template is copy-paste ready
  - Trigger conditions specified (depth 3+, score > 8.0)
  - Output includes "Limitations & Counter-Evidence" requirement for final report
  - Folder structure shows 08_Red_Team/ with expected files
```

**Skill Integration**:
- Red Team uses **perplexity** for negative/disconfirming searches
- Red Team results validated by **codex**

**Completion Verification**:
```bash
grep -n "Red Team\|RedTeam\|Devil's Advocate" Claude.md
grep -n "08_Red_Team" Claude.md
```

---

### 3.2 Add Claim Confidence Scoring System

**Description**: Add confidence tagging requirement for all major claims.

**Deliverables**:
- [x] Claim Confidence Scoring section in citation requirements
- [x] Confidence levels table: HIGH (90%+), MEDIUM (60-90%), LOW (30-60%), SPECULATIVE (<30%)
- [x] Criteria for each confidence level
- [x] Format examples (WRONG vs RIGHT)
- [x] Confidence aggregation rules for website display

**Testing Criteria**:
```yaml
validation:
  - 4 confidence levels defined with criteria
  - Each level has specific source/sample requirements
  - Format shows inline confidence tags: [HIGH CONFIDENCE], [MEDIUM CONFIDENCE], etc.
  - Website aggregation rules specify when to display vs. add footnote
```

**Skill Integration**:
- Use **perplexity** to verify claim sources for confidence scoring
- Use **codex** to audit confidence tag consistency

**Completion Verification**:
```bash
grep -n "Claim Confidence\|Confidence Scoring" Claude.md
grep -c "HIGH CONFIDENCE\|MEDIUM CONFIDENCE\|LOW CONFIDENCE\|SPECULATIVE" Claude.md
```

---

### 3.3 Add Website-Research Data Validation

**Description**: Add traceability system ensuring website only uses verified research data.

**Deliverables**:
- [x] Data Traceability Matrix template
- [x] content_map.json specification (page → sections → claim_ids)
- [x] Validation script concept (Python pseudocode)
- [x] Manual spot-check checklist per page type
- [x] Hard rule: website cannot invent data

**Testing Criteria**:
```yaml
validation:
  - Data Traceability Matrix format specified with columns
  - content_map.json structure defined
  - Spot-check checklists for: executive_summary, personas, competitive, funnels, marketing
  - "Derived-Only Rule" explicitly stated
```

**Skill Integration**:
- Use **codex** to validate content_map.json accuracy
- Use **frontend-designer** for website quality

**Completion Verification**:
```bash
grep -n "content_map.json\|Data Traceability" Claude.md
grep -n "Derived-Only Rule\|website cannot invent" Claude.md
```

---

### 3.4 Add Deployment Rollback Protocol

**Description**: Add recovery procedures for failed deployments.

**Deliverables**:
- [x] Pre-deployment checklist
- [x] Post-deployment verification steps
- [x] Rollback protocol (3 options: Vercel rollback, git revert, manual fix)
- [x] Incident documentation template

**Testing Criteria**:
```yaml
validation:
  - Pre-deploy checklist has 6+ items
  - Post-deploy verification includes: site loads, pages load, assets load
  - All 3 rollback options documented with commands
  - Incident report template has: Date, Project, Issue, Detection, Impact, Resolution, Prevention
```

**Skill Integration**:
- Use **vercel** skill for deployment and rollback

**Completion Verification**:
```bash
grep -n "Rollback Protocol\|Deployment Rollback" Claude.md
grep -c "vercel rollback\|git revert" Claude.md
```

---

## PHASE 4: P3 & Additional Systems

### 4.1 Add Evidence Ledger System

**Description**: Add structured claim tracking with CSV-based ledger.

**Deliverables**:
- [x] Evidence Ledger section in artifact standards
- [x] evidence_ledger.csv column specification
- [x] Claim taxonomy (C1 Critical, C2 Supporting, C3 Context)
- [x] Citation content standard for C1 claims
- [x] Ledger population requirements

**Testing Criteria**:
```yaml
validation:
  - evidence_ledger.csv columns defined: claim_id, claim_text, claim_type, claim_scope, evidence_quote, evidence_location, source_id, independence_group_id, confidence, verification_status, notes
  - 3 claim types defined with requirements
  - C1 requires: quote, full citation, independence check
  - Ledger file path: /RESEARCH/[project]/02_logs/evidence_ledger.csv
```

**Completion Verification**:
```bash
grep -n "evidence_ledger\|Evidence Ledger" Claude.md
grep -c "C1 Critical\|C2 Supporting\|C3 Context" Claude.md
```

---

### 4.2 Add Source Catalog with Independence Groups

**Description**: Add source tracking with anti-laundering independence grouping.

**Deliverables**:
- [x] Source Catalog section in artifact standards
- [x] source_catalog.csv column specification
- [x] Source Quality Ratings (A-E) with definitions
- [x] Independence Grouping rules and examples
- [x] Lineage tracking requirements

**Testing Criteria**:
```yaml
validation:
  - source_catalog.csv columns defined: source_id, title, author_org, date_published, url, type, domain, quality_grade, method_rigor, authority, recency, relevance, independence_group_id, lineage_notes, paywalled, accessed_date
  - 5 quality grades (A-E) with clear criteria
  - Independence group examples provided (G01_, G02_, etc.)
  - Rule: "Multiple sources must be independent origins"
```

**Completion Verification**:
```bash
grep -n "source_catalog\|Source Catalog\|Independence Group" Claude.md
grep -c "independence_group_id" Claude.md
```

---

### 4.3 Add Budgets and Stop Rules

**Description**: Add explicit termination criteria to prevent endless research loops.

**Deliverables**:
- [x] Budget specification section (N_search, N_fetch, N_docs, N_iter)
- [x] Default budget values
- [x] Stop rules (4 conditions, stop when 2 are true)
- [x] Saturation check definition
- [x] Budget exhaustion reporting requirement

**Testing Criteria**:
```yaml
validation:
  - 4 budget types defined with default values
  - Default: N_search=30, N_fetch=30, N_docs=12, N_iter=6
  - 4 stop conditions: Coverage, Saturation, Confidence, Budget
  - Saturation rule: "last K queries yield <10% net-new high-quality info"
  - Report requirement: "What we would do next with 2x budget"
```

**Completion Verification**:
```bash
grep -n "N_search\|N_fetch\|N_docs\|N_iter" Claude.md
grep -n "Saturation\|stop when" Claude.md
```

---

### 4.4 Add Prompt Injection Firewall

**Description**: Add security rules for handling untrusted web content.

**Deliverables**:
- [x] Prompt Injection Firewall section
- [x] Hard rules (never follow page instructions, never reveal prompts, never enter credentials, never run code)
- [x] Soft rules (hostile page detection, SEO spam downgrade)
- [x] Hostile page logging requirement

**Testing Criteria**:
```yaml
validation:
  - Hard rules section with 4+ rules
  - Soft rules for "ignore prior instructions" detection
  - Logging requirement in source_catalog notes
```

**Completion Verification**:
```bash
grep -n "Prompt Injection\|Injection Firewall\|hostile" Claude.md
```

---

### 4.5 Add Numeric Audit Requirements

**Description**: Add validation requirements for all numeric claims.

**Deliverables**:
- [x] Numeric Audit section in QA phase
- [x] key_metrics.csv column specification
- [x] Audit checklist (units, denominators, timeframes, geography, currency normalization)

**Testing Criteria**:
```yaml
validation:
  - key_metrics.csv columns: metric_id, metric_name, value, unit, timeframe, geography, denominator, source_id, confidence, notes
  - 6-point audit checklist
  - File path: /RESEARCH/[project]/02_logs/key_metrics.csv
```

**Completion Verification**:
```bash
grep -n "key_metrics\|Numeric Audit" Claude.md
```

---

## PHASE 5: Create Domain Overlay Files

### 5.1 Create Healthcare Domain Overlay

**Deliverables**:
- [x] File: /DOMAIN_OVERLAYS/healthcare.md
- [x] Mandatory data points (HIPAA, licensing, insurance, FDA, clinical evidence)
- [x] Source requirements (peer-reviewed, CMS, PMID)
- [x] Persona additions (insurance status, decision-making style)
- [x] Marketing constraints (no guarantees, disclaimers, testimonials)
- [x] Competitive intelligence (medical board, health grades)

**Testing Criteria**:
```yaml
validation:
  - File exists at specified path
  - All 5 sections present
  - PMID requirement explicitly stated
  - Red flags section included
```

---

### 5.2 Create Financial Domain Overlay

**Deliverables**:
- [x] File: /DOMAIN_OVERLAYS/financial.md
- [x] Mandatory data points (SEC filings, reporting periods, Bloomberg/Reuters)
- [x] Source requirements (EDGAR, earnings calls, wire services)
- [x] Required checks (verify against filings, restatements, accounting changes)
- [x] Red flags (numbers without filing reference, unverified projections)

**Testing Criteria**:
```yaml
validation:
  - File exists at specified path
  - SEC EDGAR cited as primary source
  - Forward-looking statement identification required
```

---

### 5.3 Create Legal Domain Overlay

**Deliverables**:
- [x] File: /DOMAIN_OVERLAYS/legal.md
- [x] Mandatory citation elements (jurisdiction, case status, statutory authority)
- [x] Required checks (Westlaw/LexisNexis verification, subsequent history)
- [x] Source priority (primary sources → agency guidance → treatises → law review)
- [x] Red flags (overruled cases, wrong jurisdiction)

**Testing Criteria**:
```yaml
validation:
  - File exists at specified path
  - Binding vs. persuasive authority distinction included
  - Circuit splits flagging required
```

---

### 5.4 Create Retail/Service Domain Overlay

**Deliverables**:
- [x] File: /DOMAIN_OVERLAYS/retail_service.md
- [x] Mandatory data points (foot traffic, seasonal demand, local economics)
- [x] Source requirements (Yelp, Google Business, Census, BLS)
- [x] Persona additions (shopping behavior, price sensitivity)
- [x] Marketing opportunities (local SEO, review generation)

**Testing Criteria**:
```yaml
validation:
  - File exists at specified path
  - Local SEO emphasized
  - Seasonal demand variation tracking included
```

---

### 5.5 Create B2B Domain Overlay

**Deliverables**:
- [x] File: /DOMAIN_OVERLAYS/b2b.md
- [x] Mandatory data points (decision-maker ID, buying committee, RFP processes)
- [x] Source requirements (LinkedIn, industry associations, trade publications)
- [x] Persona additions (role in buying decision, KPIs, career motivations)
- [x] Funnel differences (longer cycles, multiple touchpoints)

**Testing Criteria**:
```yaml
validation:
  - File exists at specified path
  - Buying committee composition required
  - Budget cycle timing included
```

---

### 5.6 Update Claude.md with Overlay Loading

**Deliverables**:
- [x] Overlay configuration section in Claude.md
- [x] Overlay loading YAML structure
- [x] Reference to /DOMAIN_OVERLAYS/ folder
- [x] Auto-detection logic based on industry

**Testing Criteria**:
```yaml
validation:
  - overlay configuration block in Claude.md
  - load_overlay and apply_requirements flags
  - List of available overlays
```

**Completion Verification**:
```bash
grep -n "DOMAIN_OVERLAYS\|overlay" Claude.md
ls -la /DOMAIN_OVERLAYS/
```

---

## PHASE 6: Final Integration & Validation

### 6.1 Update Master Workflow Diagram

**Deliverables**:
- [x] Updated workflow diagram showing Phase 0, 1.1, 1.5
- [x] Quality gates updated with new checkpoints
- [x] Skill integration points marked

**Testing Criteria**:
```yaml
validation:
  - Workflow shows: Phase 0 → 1 → 1.1 → 1.5 → 2 → 3 → 4 → 5 → 6
  - New gates: Complexity classified, Intensity assigned, Hypotheses formed
```

---

### 6.2 Update Quick Reference Section

**Deliverables**:
- [x] Updated key files table
- [x] Updated workflow summary
- [x] New artifact files listed
- [x] Skill usage reference

**Testing Criteria**:
```yaml
validation:
  - Key files includes: evidence_ledger.csv, source_catalog.csv, key_metrics.csv, got_state.json, content_map.json
  - Workflow summary shows all phases including 0, 1.1, 1.5
```

---

### 6.3 Final Comprehensive Validation

**Deliverables**:
- [x] All P0 changes implemented and verified
- [x] All P1 changes implemented and verified
- [x] All P2 changes implemented and verified
- [x] All P3 changes implemented and verified
- [x] All Domain Overlay files created
- [x] No broken references in Claude.md
- [x] All skill integration points documented

**Testing Criteria**:
```yaml
final_validation:
  structure:
    - [x] Phase 0 exists and complete
    - [x] Phase 1.1 exists and complete
    - [x] Phase 1.5 exists and complete
    - [x] Full GoT Controller documented
    - [x] All 6 phases have clear gates

  artifacts:
    - [x] evidence_ledger.csv schema defined
    - [x] source_catalog.csv schema defined
    - [x] key_metrics.csv schema defined
    - [x] got_state.json schema defined
    - [x] content_map.json schema defined

  systems:
    - [x] Contradiction Triage documented
    - [x] Implications Engine documented
    - [x] Red Team Agent documented
    - [x] Claim Confidence Scoring documented
    - [x] Budgets and Stop Rules documented
    - [x] Prompt Injection Firewall documented
    - [x] Deployment Rollback documented

  overlays:
    - [x] /DOMAIN_OVERLAYS/healthcare.md exists
    - [x] /DOMAIN_OVERLAYS/financial.md exists
    - [x] /DOMAIN_OVERLAYS/legal.md exists
    - [x] /DOMAIN_OVERLAYS/retail_service.md exists
    - [x] /DOMAIN_OVERLAYS/b2b.md exists

  skills:
    - [x] perplexity integration points documented
    - [x] codex integration points documented
    - [x] nanobanana integration points documented
    - [x] vercel integration points documented
    - [x] Future skill extension points documented
```

---

## Execution Checklist

Use this checklist to track implementation progress:

### Pre-Implementation
- [x] Read existing Claude.md completely
- [x] Read all 6 update files
- [x] Identify conflicts and resolutions
- [x] Create backup of existing Claude.md

### Phase 1 Execution
- [x] 1.1 Phase 0 Classification - IMPLEMENTED
- [x] 1.2 Phase 1.1 Intensity Tiers - IMPLEMENTED
- [x] 1.3 Phase 1.5 Hypothesis Formation - IMPLEMENTED
- [x] 1.4 Full GoT Controller - IMPLEMENTED
- [x] Phase 1 Verification - PASSED

### Phase 2 Execution
- [x] 2.1 Contradiction Triage - IMPLEMENTED
- [x] 2.2 Implications Engine - IMPLEMENTED
- [x] 2.3 Enhanced Verification - IMPLEMENTED
- [x] 2.4 Checkpoint Aggregation - IMPLEMENTED
- [x] Phase 2 Verification - PASSED

### Phase 3 Execution
- [x] 3.1 Red Team Agent - IMPLEMENTED
- [x] 3.2 Claim Confidence Scoring - IMPLEMENTED
- [x] 3.3 Website-Research Validation - IMPLEMENTED
- [x] 3.4 Deployment Rollback - IMPLEMENTED
- [x] Phase 3 Verification - PASSED

### Phase 4 Execution
- [x] 4.1 Evidence Ledger - IMPLEMENTED
- [x] 4.2 Source Catalog - IMPLEMENTED
- [x] 4.3 Budgets/Stop Rules - IMPLEMENTED
- [x] 4.4 Prompt Injection Firewall - IMPLEMENTED
- [x] 4.5 Numeric Audit - IMPLEMENTED
- [x] Phase 4 Verification - PASSED

### Phase 5 Execution
- [x] 5.1 Healthcare Overlay - CREATED
- [x] 5.2 Financial Overlay - CREATED
- [x] 5.3 Legal Overlay - CREATED
- [x] 5.4 Retail/Service Overlay - CREATED
- [x] 5.5 B2B Overlay - CREATED
- [x] 5.6 Overlay Loading in Claude.md - IMPLEMENTED
- [x] Phase 5 Verification - PASSED

### Phase 6 Execution
- [x] 6.1 Master Workflow Updated - DONE
- [x] 6.2 Quick Reference Updated - DONE
- [x] 6.3 Final Validation - PASSED

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Dec 14, 2025 | Initial implementation plan created |
| 1.1 | Dec 14, 2025 | **IMPLEMENTATION COMPLETE** - All phases implemented, all domain overlays created |

---

## Implementation Status: COMPLETE

### Summary of Changes Made

**Claude.md Updated (1,786 lines):**
- Phase 0: Question Complexity Classification (Type A/B/C/D)
- Phase 1.1: Research Intensity Tiers (Express/Standard/Comprehensive/Enterprise)
- Phase 1.5: Hypothesis Formation with priors
- Full GoT Controller with JSON schema, scoring rubric, pruning rules
- Contradiction Triage Protocol
- Implications Engine ("So What?" framework)
- Enhanced Research Verification (7 audit categories)
- Checkpoint Aggregation Protocol
- Red Team Agent (mandatory at depth 3+)
- Claim Confidence Scoring (HIGH/MEDIUM/LOW/SPECULATIVE)
- Website-Research Data Validation (content_map.json)
- Deployment Rollback Protocol
- Evidence Ledger System (C1/C2/C3 taxonomy)
- Source Catalog with Independence Groups
- Budgets and Stop Rules
- Prompt Injection Firewall
- Numeric Audit Requirements
- Skill Integration (perplexity, codex, nanobanana, vercel, hubspot, frontend-designer)
- Domain Overlay loading configuration

**Domain Overlays Created (5 files):**
- `/DOMAIN_OVERLAYS/healthcare.md` (8,479 bytes)
- `/DOMAIN_OVERLAYS/financial.md` (9,560 bytes)
- `/DOMAIN_OVERLAYS/legal.md` (9,372 bytes)
- `/DOMAIN_OVERLAYS/retail_service.md` (10,538 bytes)
- `/DOMAIN_OVERLAYS/b2b.md` (12,191 bytes)

---

## Appendix: Conflict Resolution Log

| Conflict | Source A | Source B | Resolution | Rationale |
|----------|----------|----------|------------|-----------|
| Phase structure | chatgpt (7+1 phases) | claude (6 phases + 0/1.5) | Use claude structure | End-to-end workflow preferred |
| GoT state path | chatgpt (/10_graph/) | claude (/04_graph/) | Use /04_graph/ | Consistent with claude_2 folder structure |
| Stop rules | chatgpt (2 of 4) | claude (tier-based) | Merge both | Intensity tiers with condition-based stops |
| Folder structure | chatgpt (flat + CSVs) | claude (hierarchical) | Merge both | Hierarchical with CSV logs subfolder |

---

*End of Implementation Plan*
