# Deep Research Process V3
## Update Implementation Guide — End-to-End Workflow Enhancement

| | |
|---|---|
| **Prepared For** | Technical Implementation Team |
| **Date** | December 14, 2025 |
| **Document Type** | Implementation Specification for V3 Workflow System |

---

# Executive Summary

Version 3 represents a **major architectural shift** from V2. It's no longer just a research framework—it's a complete end-to-end workflow system that takes user input through research, website generation, and deployment. This is a significant evolution.

**What V3 Got Right:**
- Complete workflow orchestration (Research → Website → Deployment)
- Structured information gathering with dynamic configuration
- Multiple verification gates with Codex/Claude fallback
- Clear folder structures for single vs. multiple services
- "Do not stop" execution philosophy for completion
- GitHub + Vercel deployment integration

**What V3 Is Missing:**
The core research quality frameworks from V1/V2 feedback were not integrated. The GoT implementation is actually *less detailed* than V2, and critical decision-making frameworks are absent.

**This guide provides:** 12 specific implementations to transform V3 from a good workflow system into a world-class research + delivery engine.

---

# V2 → V3 Comparison

## What V3 Improved

| Area | V2 | V3 |
|------|----|----|
| **Scope** | Research only | Research + Website + Deployment |
| **User Input** | Ad-hoc | Structured questionnaire with dynamic config file |
| **Verification** | Single review phase | Multiple checkpoint gates |
| **Output** | Research files | Research + Live website |
| **Execution** | Manual phase transitions | Continuous until complete |
| **Deployment** | None | GitHub + Vercel integration |
| **Progress Tracking** | Basic | PROGRESS.md with completion percentages |

## What V3 Lost (Regression from V2)

| Area | V2 Had | V3 Has |
|------|--------|--------|
| **GoT Controller** | Full implementation with graph state | Only conceptual mention |
| **Transformation Agents** | Detailed Generate/Aggregate/Refine prompts | Brief description |
| **Graph State JSON** | Explicit schema | Not present |
| **Citation Requirements** | Detailed format with A-E ratings | Minimal |
| **Agent Templates** | Copy-paste ready prompts | Generic descriptions |

## What's Still Missing (From V1/V2 Feedback)

| Priority | Gap | Status in V3 |
|----------|-----|--------------|
| **P0** | Research Intensity Tiers | ❌ NOT IMPLEMENTED |
| **P0** | Hypothesis Formation | ❌ NOT IMPLEMENTED |
| **P1** | Contradiction Triage | ❌ NOT IMPLEMENTED |
| **P1** | Implications Engine ("So What?") | ❌ NOT IMPLEMENTED |
| **P1** | Inter-Agent Checkpoint Coordination | ⚠️ PARTIAL (has checkpoints, not mid-research) |
| **P2** | Red Team Agent | ❌ NOT IMPLEMENTED |
| **P2** | Question Complexity Classifier | ❌ NOT IMPLEMENTED |
| **P2** | Claim Confidence Scoring | ❌ NOT IMPLEMENTED |
| **P3** | Domain-Specific Overlays | ❌ NOT IMPLEMENTED |

---

# Implementation Priority Matrix

| Pri | Implementation | Effort | Impact | Location in V3 |
|-----|----------------|--------|--------|----------------|
| **P0** | Research Intensity Tiers | Low | High | Add to Phase 1 |
| **P0** | Hypothesis Formation | Medium | High | Add as Phase 1.5 |
| **P0** | Restore GoT Controller from V2 | Medium | High | Replace Phase 2 GoT section |
| **P1** | Contradiction Triage | Low | High | Add to Phase 2 research |
| **P1** | Implications Engine | Low | High | Add to Phase 2 synthesis |
| **P1** | Enhanced Research Verification | Medium | High | Enhance Phase 3 checklist |
| **P2** | Red Team Agent | Low | Medium | Add to agent deployment |
| **P2** | Claim Confidence Scoring | Medium | Medium | Add to citation requirements |
| **P2** | Question Complexity Classifier | Low | Medium | Add to Phase 1 |
| **P3** | Domain Overlays | High | Medium | Create separate files |
| **NEW** | Website-Research Data Validation | Medium | High | Add to Phase 5 |
| **NEW** | Deployment Rollback Protocol | Low | Medium | Add to Phase 6 |

---

# Implementation 1: Research Intensity Tiers (P0)

## Location in V3
Add to **Phase 1: Information Gathering**, after Step 1.3 (Update New_question_dynamic.md)

## Add This Section

```markdown
### Step 1.4: Research Intensity Classification

Before proceeding to research, classify the project to set appropriate resource allocation:

| Tier | Trigger Conditions | Agents | Time Budget | Verification |
|------|-------------------|--------|-------------|--------------|
| **Express** | Single service, known market, basic analysis | 10-15 | 30-60 min | Claude only |
| **Standard** | Single service, moderate complexity | 20-25 | 2-3 hours | Codex preferred |
| **Comprehensive** | Multiple services OR high-value client | 30 | 4-6 hours | Codex required |
| **Enterprise** | Complex multi-location, multi-service | 40+ | 8-12 hours | Codex + manual review |
```

**Classification Criteria:**

```yaml
intensity_factors:
  service_count:
    single: +0
    multiple: +1
  
  location_count:
    single: +0
    2-3: +1
    4+: +2
  
  market_complexity:
    established_simple: +0  # e.g., general optometry
    established_complex: +1  # e.g., dry eye specialty
    emerging: +2  # e.g., new aesthetic treatments
  
  client_value:
    standard: +0
    strategic: +1
    enterprise: +2

tier_assignment:
  0-1 points: Express
  2-3 points: Standard
  4-5 points: Comprehensive
  6+ points: Enterprise
```

**Update the configuration display:**

```
RESEARCH CONFIGURATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Business Name: [FULL NAME]
Short Name: [SHORT]
Website: [URL]
Service 1: [PRIMARY SERVICE]
Service 2: [SECONDARY SERVICE or None]
Location(s): [ALL ADDRESSES FOUND]
Industry: [DETECTED]
Model: [B2B/B2C]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTENSITY TIER: [EXPRESS/STANDARD/COMPREHENSIVE/ENTERPRISE]
Agent Budget: [X] agents
Time Budget: [Y] hours
Verification: [Codex required / Claude only]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

# Implementation 2: Hypothesis Formation (P0)

## Location in V3
Add as **Phase 1.5** between Information Gathering (Phase 1) and Deep Research (Phase 2)

## Add This Section

```markdown
## PHASE 1.5: Research Hypothesis Formation

### Why This Matters
Research without hypotheses produces encyclopedic outputs. Research WITH hypotheses produces actionable insights.

### Step 1.5.1: Generate Business Hypotheses

Based on gathered information, generate testable hypotheses:

**Market Hypotheses (generate 2-3):**
```
H-M1: "[SERVICE] demand in [LOCATION] is [growing/stable/declining] because..."
H-M2: "The primary [SERVICE] customer in this market is [DEMOGRAPHIC] because..."
H-M3: "Price sensitivity in this market is [high/medium/low] because..."
```

**Competitive Hypotheses (generate 2-3):**
```
H-C1: "[COMPANY]'s main competitive advantage is [X] because..."
H-C2: "The biggest competitive threat is [COMPETITOR TYPE] because..."
H-C3: "Market differentiation opportunity exists in [AREA] because..."
```

**Growth Hypotheses (generate 2-3):**
```
H-G1: "The highest-ROI marketing channel for [SERVICE] is [CHANNEL] because..."
H-G2: "[COMPANY] can achieve [X]% growth by [STRATEGY] because..."
H-G3: "The primary barrier to growth is [BARRIER] because..."
```

### Step 1.5.2: Assign Prior Probabilities

For each hypothesis:
```yaml
hypothesis:
  id: "H-M1"
  statement: "[The hypothesis]"
  prior_probability: 0.XX  # Your initial estimate
  prior_reasoning: "Based on [initial observations]"
  confirming_evidence: ["What would prove this true"]
  disconfirming_evidence: ["What would prove this false"]
  test_queries: ["Search queries to test this"]
```

### Step 1.5.3: Update Configuration File

Add hypotheses to `New_question_dynamic.md`:

```yaml
# Add to INPUT VARIABLES section:

hypotheses:
  market:
    - id: "H-M1"
      statement: "[Statement]"
      prior: 0.XX
      status: "testing"  # testing | confirmed | disconfirmed | inconclusive
  competitive:
    - id: "H-C1"
      statement: "[Statement]"
      prior: 0.XX
      status: "testing"
  growth:
    - id: "H-G1"
      statement: "[Statement]"
      prior: 0.XX
      status: "testing"
```

### Step 1.5.4: Research Directive

Instruct all research agents:
```
HYPOTHESIS-DRIVEN RESEARCH:
Your research must explicitly address these hypotheses:
[LIST HYPOTHESES]

For each hypothesis, gather:
1. Evidence that SUPPORTS it (with citations)
2. Evidence that CONTRADICTS it (with citations)
3. Your updated probability estimate
4. Confidence level in your assessment

Do NOT just gather information. Test these specific beliefs.
```

### Step 1.5.5: Hypothesis Tracking in PROGRESS.md

Add to progress tracker:
```markdown
### Hypothesis Status
| ID | Statement | Prior | Current | Status | Key Evidence |
|----|-----------|-------|---------|--------|--------------|
| H-M1 | [Statement] | 0.XX | 0.XX | Testing | [Brief] |
| H-C1 | [Statement] | 0.XX | 0.XX | Confirmed | [Brief] |
| H-G1 | [Statement] | 0.XX | 0.XX | Disconfirmed | [Brief] |
```
```

---

# Implementation 3: Restore GoT Controller (P0)

## Location in V3
Replace the brief GoT section in **Phase 2** with the full V2 implementation

## Current V3 Problem
V3 only has this minimal GoT description:
```
**Understanding Graph of Thoughts (GoT):**
- **Thoughts = Nodes**: Each research finding is a node
- **Edges = Dependencies**: Connect related findings
- **Transformations**: Generate, Aggregate, Refine operations
- **Scoring**: Every thought evaluated 0-10 for quality
- **Pruning**: Low-scoring branches abandoned
```

This is insufficient for actual implementation.

## Replace With Full GoT Controller

```markdown
### Step 2.2: Initialize GoT Controller

**Create GoT State File:** `/RESEARCH/[FOLDER]/got_state.json`

```json
{
  "metadata": {
    "company": "[NAME]",
    "short_name": "[SHORT]",
    "services": {
      "primary": "[SERVICE1]",
      "secondary": "[SERVICE2 or NONE]"
    },
    "industry": "[INDUSTRY]",
    "model": "[B2B/B2C]",
    "intensity_tier": "[TIER]",
    "created": "[TIMESTAMP]"
  },
  "hypotheses": [
    // Copied from Phase 1.5
  ],
  "nodes": {
    "n1": {
      "id": "n1",
      "text": "Root: Research [COMPANY] [SERVICES]",
      "type": "root",
      "depth": 0,
      "score": 0,
      "status": "active"
    }
  },
  "edges": [],
  "frontier": ["n1"],
  "budget": {
    "total_agents": 30,
    "deployed": 0,
    "remaining": 30,
    "time_budget_hours": 4
  },
  "checkpoints": []
}
```

### Step 2.3: GoT Transformation Operations

**Generate(k):** Create k new research branches
```
Task: "GoT Generate - Node [ID] Branch [k/total]"

Parent thought: "[PARENT_NODE_TEXT]"
Research angle: [SPECIFIC_ANGLE]

Execute:
1. WebSearch for "[TOPIC] [ANGLE]" - find 5+ sources
2. Score each source quality (A-E rating)
3. WebFetch top 3 sources for full content
4. Synthesize findings (200-400 words)
5. Update hypothesis probabilities if relevant
6. Self-score your output (0-10)

Return:
{
  "node_id": "[NEW_ID]",
  "parent_id": "[PARENT_ID]",
  "text": "[SYNTHESIZED_FINDINGS]",
  "sources": ["url1", "url2", "url3"],
  "source_ratings": {"url1": "B", "url2": "A", "url3": "C"},
  "hypothesis_updates": [{"id": "H-M1", "new_prob": 0.XX, "reasoning": "..."}],
  "score": X.X,
  "operation": "Generate"
}
```

**Aggregate(k):** Merge k thoughts into stronger synthesis
```
Task: "GoT Aggregate - Nodes [ID1, ID2, ID3]"

Combine these research findings:
[NODE_1_TEXT] (Score: X.X)
[NODE_2_TEXT] (Score: X.X)
[NODE_3_TEXT] (Score: X.X)

Create ONE unified synthesis that:
- Preserves all important claims with citations
- Resolves contradictions (apply Contradiction Triage)
- Maintains source attribution
- Updates hypothesis probabilities
- Achieves higher quality than any input

Return aggregated node with self-score.
```

**Refine(1):** Improve existing thought quality
```
Task: "GoT Refine - Node [ID]"

Current thought: "[NODE_TEXT]"
Current score: [SCORE]

Improve by:
1. Verify all claims with additional searches
2. Add missing context or nuance
3. Strengthen weak arguments
4. Fix citation gaps
5. Enhance clarity

Do NOT add major new points - only refine existing content.
Return refined thought with updated score.
```

**RedTeam(1):** Find counter-evidence (NEW - from V2 feedback)
```
Task: "GoT Red Team - Node [ID]"

Emerging conclusions: "[AGGREGATED_FINDINGS]"

Find evidence AGAINST these conclusions:
1. Contradicting data
2. Failed case studies
3. Expert disagreements
4. Methodological weaknesses
5. Edge cases
6. Alternative explanations

Present counterarguments at their STRONGEST.
```

### Step 2.4: GoT Traversal Strategy

```
ITERATION LOOP:

repeat until COMPLETE {
    1. SELECT frontier nodes (top 3 by score)
    
    2. For each selected node, CHOOSE transformation:
       - If depth < 2: Generate(3) to explore
       - If score < 7.0: Refine(1) to improve
       - If multiple good nodes: Aggregate(k)
       - If depth 3+ AND aggregate > 8.0: RedTeam(1)
    
    3. DEPLOY transformation agents
    
    4. UPDATE got_state.json:
       - Add new nodes
       - Create edges
       - Update scores
       - Update hypothesis probabilities
       - Update frontier
    
    5. PRUNE: KeepBestN(5) per depth level
    
    6. CHECKPOINT at depth 2:
       - Pause and review all findings
       - Identify gaps and overlaps
       - Redirect agents as needed
       - Update hypotheses
    
    7. EXIT when:
       - Best score > 9.0 AND depth >= 3
       - OR time budget exhausted
       - OR all hypotheses resolved
}
```

### Step 2.5: Save GoT State After Each Iteration

```bash
# Update got_state.json after every transformation
# This enables:
# - Progress recovery if interrupted
# - Audit trail of research decisions
# - Debugging poor results
```
```

---

# Implementation 4: Contradiction Triage Protocol (P1)

## Location in V3
Add to **Phase 2: Deep Research**, within the research agent instructions

## Add This Section

```markdown
### Contradiction Handling Protocol

When research agents find conflicting information:

**Step 1: Classify the Conflict**

| Type | Definition | Example |
|------|------------|---------|
| **Data** | Numbers disagree | "Market size is $5B" vs "$8B" |
| **Interpretation** | Same data, different conclusions | "Growth is slowing" vs "Growth is accelerating" |
| **Methodological** | Different research methods | Survey vs. observed behavior |
| **Temporal** | Information from different time periods | 2022 data vs 2024 data |

**Step 2: Apply Resolution Method**

| Conflict Type | Resolution |
|---------------|------------|
| **Data** | Find PRIMARY source; use most recent; note range |
| **Interpretation** | Present both views with evidence strength; don't pick winner |
| **Methodological** | Prefer direct measurement > surveys > expert opinion |
| **Temporal** | Use most recent; note if trend changed |

**Step 3: Document in Research Output**

```markdown
### Conflicting Information Note

**Topic:** [What the conflict is about]
**Source A:** [Claim] (Source, Date, Rating)
**Source B:** [Claim] (Source, Date, Rating)
**Conflict Type:** [Data/Interpretation/Methodological/Temporal]
**Resolution:** [How we handled it]
**Confidence:** [High/Medium/Low]
**User Note:** [Any decision they may need to make]
```

**Step 4: Update Hypothesis Tracking**

If conflict affects a hypothesis:
- Note the conflicting evidence
- Adjust probability toward uncertainty (move toward 0.5)
- Flag for human review if critical
```

---

# Implementation 5: Implications Engine (P1)

## Location in V3
Add to **Phase 2: Deep Research**, at the end of each research section synthesis

## Add This Section

```markdown
### Implications Analysis ("So What?" Framework)

**EVERY major research section must end with implications analysis:**

```markdown
## Implications for [COMPANY]

### SO WHAT? (Significance)
[Why this finding matters for this specific business]

### NOW WHAT? (Action Items)
1. [Specific actionable recommendation]
2. [Specific actionable recommendation]
3. [Specific actionable recommendation]

### WHAT IF? (Scenarios)
- **If trend continues:** [Projected outcome]
- **If trend reverses:** [Projected outcome]
- **If no action taken:** [Projected outcome]

### COMPARED TO? (Benchmarks)
- Industry average: [X]
- Top performers: [Y]
- [COMPANY] current: [Z]
- Gap to close: [Z - Y]
```

**Apply to these research sections:**

| Section | Implications Focus |
|---------|-------------------|
| Market Analysis | Market opportunity size and timing |
| Personas | Acquisition strategy and messaging |
| Competitive | Differentiation and positioning |
| Funnels | Conversion optimization priorities |
| Marketing | Channel and budget allocation |
| Partnerships | Revenue opportunity and effort required |

**Website Mapping:**
The implications become the "Key Insights" and "Action Items" sections on each website page.
```

---

# Implementation 6: Enhanced Research Verification (P1)

## Location in V3
Enhance **Phase 3: Research Review** checklist

## Current V3 Problem
The verification checklist is good but missing critical quality checks.

## Add These Verification Items

```markdown
### Step 3.2: Enhanced Verification Checklist

**QUALITY VERIFICATION (Add to existing checklist):**

```yaml
hypothesis_verification:
  - [ ] All hypotheses from Phase 1.5 have been tested
  - [ ] Each hypothesis has CONFIRMING evidence documented
  - [ ] Each hypothesis has DISCONFIRMING evidence documented
  - [ ] Final probability estimates are justified
  - [ ] Hypothesis status updated (confirmed/disconfirmed/inconclusive)

contradiction_verification:
  - [ ] All identified contradictions are documented
  - [ ] Resolution method applied to each contradiction
  - [ ] Confidence levels assigned to conflicted claims
  - [ ] No unresolved critical contradictions

implications_verification:
  - [ ] Every major section has SO WHAT analysis
  - [ ] NOW WHAT includes specific action items
  - [ ] WHAT IF scenarios are realistic
  - [ ] COMPARED TO benchmarks are sourced

confidence_scoring:
  - [ ] Every major claim has confidence tag
  - [ ] HIGH confidence: 3+ corroborating sources
  - [ ] MEDIUM confidence: 1-2 sources, credible
  - [ ] LOW confidence: Single source or inference
  - [ ] SPECULATIVE: Clearly labeled as such

citation_audit:
  - [ ] Every factual claim has inline citation
  - [ ] Citation format: (Org, Year, "Title") URL
  - [ ] Source quality ratings (A-E) applied
  - [ ] No claims with only "various sources" attribution
  - [ ] Publication dates within last 2 years for market data
```

**NUMERICAL VERIFICATION:**

```yaml
calculation_checks:
  TAM_SAM_SOM:
    - [ ] TAM calculation methodology documented
    - [ ] SAM shows clear filtering criteria
    - [ ] SOM is realistic (typically 1-5% of SAM)
    - [ ] All numbers have sources
  
  LTV_CAC:
    - [ ] LTV formula clearly stated
    - [ ] Assumptions documented (churn, margin, etc.)
    - [ ] CAC by channel with sources
    - [ ] LTV:CAC ratio calculated and interpreted
  
  market_sizing:
    - [ ] Population/household numbers sourced (Census, etc.)
    - [ ] Penetration rates justified
    - [ ] Growth rates have time horizon
    - [ ] Currency and year specified

cross_reference_check:
  - [ ] Same number used consistently across all files
  - [ ] If number appears in multiple files, they match
  - [ ] Summary numbers equal sum of components
```

**GOT STATE VERIFICATION:**

```yaml
got_state_check:
  - [ ] got_state.json is complete and valid JSON
  - [ ] All nodes have scores assigned
  - [ ] Best path score exceeds 8.0
  - [ ] Red Team analysis completed (if depth 3+ reached)
  - [ ] Hypothesis probabilities updated
```
```

---

# Implementation 7: Red Team Agent (P2)

## Location in V3
Add to **Phase 2: Deploy 30 Research Agents** section

## Add This Section

```markdown
### Red Team Agent Deployment (MANDATORY)

**Deploy after initial research synthesis (depth 3+):**

```yaml
red_team_agents: 2 agents
  - Research Assumptions Challenger
  - Competitive Response Simulator

red_team_mandate:
  timing: "After aggregate scores exceed 8.0"
  output: "Must be included in final research as 'Risks & Counterarguments' section"
  website: "Displayed on Executive Summary page"
```

**Research Assumptions Challenger:**
```
Task: "Red Team - Challenge Research Assumptions"

Review all research findings and identify:

1. ASSUMPTIONS we're making:
   - What are we assuming about the market?
   - What are we assuming about customer behavior?
   - What are we assuming about competition?

2. EVIDENCE GAPS:
   - What claims have weak support?
   - What would change our conclusions if wrong?
   - What haven't we considered?

3. FAILURE MODES:
   - What could make these recommendations fail?
   - What market changes would invalidate this analysis?
   - What competitor actions could disrupt this?

Output: "Assumptions_and_Risks.md" in research folder
```

**Competitive Response Simulator:**
```
Task: "Red Team - Simulate Competitive Response"

Based on competitive intelligence gathered:

1. If [COMPANY] implements recommended strategies:
   - How will Competitor A likely respond?
   - How will Competitor B likely respond?
   - What defensive moves should we anticipate?

2. COUNTER-MOVES to prepare for:
   - Price competition scenarios
   - Service expansion scenarios
   - Marketing escalation scenarios

3. SUSTAINABLE ADVANTAGES:
   - What advantages are defensible?
   - What can be copied within 6 months?
   - What requires 2+ years to replicate?

Output: "Competitive_Response_Scenarios.md" in research folder
```

**Update folder structure:**
```
/RESEARCH/[SHORTNAME]_Analysis/
├── ...existing folders...
├── 08_Red_Team/                    ← NEW
│   ├── Assumptions_and_Risks.md
│   └── Competitive_Response_Scenarios.md
└── PROGRESS.md
```
```

---

# Implementation 8: Claim Confidence Scoring (P2)

## Location in V3
Add to **Phase 2** citation requirements and **Phase 3** verification

## Add This Section

```markdown
### Claim Confidence Scoring System

**Every factual claim must include a confidence tag:**

| Confidence | Criteria | Tag Format |
|------------|----------|------------|
| **HIGH** | 3+ corroborating A/B sources, large sample sizes, replicated | `[HIGH CONFIDENCE]` |
| **MEDIUM** | 1-2 credible sources, reasonable methodology | `[MEDIUM CONFIDENCE]` |
| **LOW** | Single source, small sample, or inference from adjacent data | `[LOW CONFIDENCE]` |
| **SPECULATIVE** | Expert opinion, theoretical, or extrapolated | `[SPECULATIVE]` |

**Format Examples:**

❌ **WRONG:**
> "The dry eye treatment market is growing rapidly."

✅ **RIGHT:**
> "The dry eye treatment market is projected to grow at 6.2% CAGR through 2028 [HIGH CONFIDENCE: 3 market reports agree] (Grand View Research, 2024; Market Research Future, 2024; Allied Market Research, 2024)"

❌ **WRONG:**
> "Customers prefer online booking."

✅ **RIGHT:**
> "68% of patients under 45 prefer online booking for medical appointments [MEDIUM CONFIDENCE: single survey, n=2,400] (Accenture Healthcare Consumer Survey, 2023)"

**Confidence Aggregation for Website:**

When multiple claims feed into a website stat:
- If ALL source claims are HIGH → Display as featured stat
- If ANY claims are LOW/SPECULATIVE → Add footnote or qualifier
- If SPECULATIVE → Don't display as fact; frame as "analysis suggests"
```

---

# Implementation 9: Question Complexity Classifier (P2)

## Location in V3
Add to **Phase 1: Information Gathering**, as Step 1.0 (before questions)

## Add This Section

```markdown
### Step 1.0: Project Complexity Assessment

**Before asking questions, classify the request:**

| Type | Characteristics | Process |
|------|-----------------|---------|
| **Type A: Quick** | Single service, single location, established market | Express workflow: 10 agents, 1 hour, Claude verification |
| **Type B: Standard** | Single service, multiple locations OR moderate complexity | Standard workflow: 20 agents, 3 hours, Codex preferred |
| **Type C: Comprehensive** | Multiple services OR competitive market OR strategic client | Full workflow: 30 agents, 6 hours, Codex required |
| **Type D: Enterprise** | Multi-service, multi-location, enterprise client | Extended workflow: 40+ agents, 12 hours, Codex + manual review |

**Quick Classification Questions:**
```
Before we begin, let me understand the scope:

1. How many services will we be analyzing? (1 / 2 / 3+)
2. How many locations does the business have? (1 / 2-5 / 6+)
3. Is this a highly competitive market? (Yes / No / Unsure)
4. What's the client relationship? (New / Existing / Strategic)
5. What's the timeline? (Rush / Standard / Flexible)
```

**Auto-Classification Logic:**
```python
score = 0
if services > 1: score += 1
if services > 2: score += 1
if locations > 1: score += 1
if locations > 5: score += 1
if competitive == "Yes": score += 1
if client == "Strategic": score += 1
if timeline == "Rush": score -= 1  # Reduces depth, not quality

if score <= 1: return "Type A: Quick"
if score <= 3: return "Type B: Standard"
if score <= 5: return "Type C: Comprehensive"
return "Type D: Enterprise"
```

**Process Adjustment by Type:**

| Type | Phases | Agents | Verification | Website Pages |
|------|--------|--------|--------------|---------------|
| A | 1,2,4,6 (skip 3,5 reviews) | 10-15 | Claude only | 4 core pages |
| B | All 6 | 20-25 | Codex preferred | 6 pages |
| C | All 6 + Red Team | 30 | Codex required | 7+ pages |
| D | All 6 + Red Team + Manual | 40+ | Codex + Human | 10+ pages |
```

---

# Implementation 10: Domain-Specific Overlays (P3)

## Location in V3
Create as separate files referenced by `New_question_dynamic.md`

## Healthcare Overlay
**File:** `/RESEARCH/OVERLAYS/healthcare.md`

```markdown
# Healthcare Research Overlay

## Industry-Specific Requirements

### Mandatory Data Points
- [ ] HIPAA compliance considerations for marketing
- [ ] State licensing requirements
- [ ] Insurance/reimbursement landscape
- [ ] Regulatory body guidelines (FDA if devices)
- [ ] Clinical evidence requirements for claims

### Source Requirements
- Peer-reviewed when claiming clinical efficacy
- CMS data for insurance/Medicare claims
- State health department for demographics
- PMID required for medical claims

### Persona Additions
- Insurance status (employer, Medicare, self-pay, Medicaid)
- Healthcare decision-making style (research-first, doctor-trusts, convenience-driven)
- Previous treatment history consideration
- Family health history relevance

### Marketing Constraints
- Cannot guarantee outcomes
- Must include appropriate disclaimers
- Testimonials require consent documentation
- Before/after photos have specific requirements

### Competitive Intelligence
- Check state medical board for providers
- Review health grades and similar rating sites
- Hospital affiliations matter
- Insurance network participation is competitive factor
```

## Retail/Service Overlay
**File:** `/RESEARCH/OVERLAYS/retail_service.md`

```markdown
# Retail/Service Research Overlay

## Industry-Specific Requirements

### Mandatory Data Points
- [ ] Foot traffic patterns (if physical location)
- [ ] Seasonal demand variations
- [ ] Local economic indicators
- [ ] Competitor pricing transparency
- [ ] Review site presence and ratings

### Source Requirements
- Yelp/Google Business data
- Local chamber of commerce
- Census Bureau for demographics
- Bureau of Labor Statistics for spending

### Persona Additions
- Shopping behavior (research vs. impulse)
- Price sensitivity indicators
- Brand loyalty factors
- Social proof importance

### Marketing Opportunities
- Local SEO critical
- Review generation programs
- Community involvement
- Seasonal promotion timing

### Competitive Intelligence
- Mystery shopping data valuable
- Social media engagement metrics
- Local advertising presence
- Community reputation factors
```

## B2B Overlay
**File:** `/RESEARCH/OVERLAYS/b2b.md`

```markdown
# B2B Research Overlay

## Industry-Specific Requirements

### Mandatory Data Points
- [ ] Decision-maker identification
- [ ] Buying committee composition
- [ ] Contract/RFP processes
- [ ] Budget cycles
- [ ] Procurement requirements

### Source Requirements
- LinkedIn for org structure
- Industry association data
- Trade publications
- Conference/event participation

### Persona Additions
- Role in buying decision (champion, influencer, blocker, decision-maker)
- KPIs they're measured on
- Career motivations
- Internal political considerations

### Funnel Differences
- Longer sales cycles
- Multiple touchpoints required
- Content marketing emphasis
- Relationship building critical

### Competitive Intelligence
- RFP history if available
- Case study analysis
- Partnership ecosystems
- Integration capabilities
```

## Update New_question_dynamic.md

```yaml
# Add to configuration:

overlay:
  primary: "[healthcare/retail_service/b2b/other]"
  secondary: "[if applicable]"
  file_path: "/RESEARCH/OVERLAYS/[overlay].md"
  
research_directive:
  load_overlay: true
  apply_requirements: true
```

---

# Implementation 11: Website-Research Data Validation (NEW)

## Location in V3
Add to **Phase 5: Website Verification**, after design compliance check

## Add This Section

```markdown
### Step 5.3: Research-to-Website Data Validation

**CRITICAL:** Every number on the website must trace back to research.

**Data Traceability Matrix:**

| Website Element | Source File | Source Line | Confidence | Last Updated |
|-----------------|-------------|-------------|------------|--------------|
| TAM Figure | 02_Market_Analysis/TAM.md | Line 47 | HIGH | [date] |
| Persona 1 Income | 03_Personas/Service1.md | Line 23 | MEDIUM | [date] |
| Competitor Count | 04_Competitive/Overview.md | Line 12 | HIGH | [date] |
| LTV:CAC Ratio | 05_Funnels/Economics.md | Line 89 | MEDIUM | [date] |

**Automated Validation Script:**

```python
# Create: /website/validate_data.py

import re
import json

def validate_website_data():
    """
    Cross-reference all numbers on website against research files.
    Flag any discrepancies.
    """
    
    website_numbers = extract_numbers_from_html('/website/')
    research_numbers = extract_numbers_from_research('/RESEARCH/')
    
    discrepancies = []
    
    for page, numbers in website_numbers.items():
        for number, context in numbers:
            if not find_in_research(number, context, research_numbers):
                discrepancies.append({
                    'page': page,
                    'number': number,
                    'context': context,
                    'status': 'NOT_FOUND_IN_RESEARCH'
                })
    
    return discrepancies

# Run before deployment
if __name__ == "__main__":
    issues = validate_website_data()
    if issues:
        print("DATA VALIDATION FAILED:")
        for issue in issues:
            print(f"  - {issue['page']}: {issue['number']} ({issue['context']})")
        exit(1)
    print("DATA VALIDATION PASSED")
```

**Manual Spot-Check Checklist:**

```yaml
executive_summary_page:
  - [ ] Market size matches 02_Market_Analysis
  - [ ] Growth rate matches and has same source
  - [ ] Opportunity statement reflects research conclusions

personas_page:
  - [ ] Persona count matches research
  - [ ] Demographics match exactly
  - [ ] LTV figures match 05_Funnels calculations
  - [ ] Headshot images loaded correctly

competitive_page:
  - [ ] Competitor names match research
  - [ ] Competitive positioning consistent
  - [ ] Differentiation claims supported by research

funnels_page:
  - [ ] Conversion rates match research
  - [ ] CAC figures by channel match
  - [ ] LTV:CAC interpretation consistent

marketing_page:
  - [ ] Channel recommendations match strategy
  - [ ] Budget allocations reflect research
  - [ ] Priority ranking consistent
```
```

---

# Implementation 12: Deployment Rollback Protocol (NEW)

## Location in V3
Add to **Phase 6: Deployment**, after verification

## Add This Section

```markdown
### Step 6.5: Deployment Verification & Rollback Protocol

**Pre-Deployment Checklist:**

```yaml
pre_deploy:
  - [ ] All Phase 5 verifications passed
  - [ ] Data validation script passed
  - [ ] Git commit includes all files
  - [ ] No sensitive data in repository (API keys, etc.)
  - [ ] .gitignore properly configured
  - [ ] README.md in repository root
```

**Post-Deployment Verification:**

```bash
# Immediately after Vercel deployment:

# 1. Verify site loads
curl -I https://[PROJECT].vercel.app
# Expected: HTTP 200

# 2. Check all pages load
for page in "" "executive-summary" "personas" "competitive" "marketing" "funnels" "partnerships"; do
  status=$(curl -s -o /dev/null -w "%{http_code}" "https://[PROJECT].vercel.app/$page.html")
  echo "$page: $status"
done

# 3. Verify images load
curl -I https://[PROJECT].vercel.app/assets/images/personas/persona1.png
# Expected: HTTP 200

# 4. Check for console errors (manual)
# Open browser DevTools → Console → Refresh → Check for errors
```

**Rollback Protocol:**

If post-deployment verification fails:

```bash
# Option 1: Vercel instant rollback
vercel rollback [deployment-url] --token $VERCEL_TOKEN

# Option 2: Redeploy previous commit
git revert HEAD
git push
# Vercel auto-deploys

# Option 3: Manual fix and redeploy
# Fix issue locally
git add .
git commit -m "Fix: [description of fix]"
git push
# Verify new deployment
```

**Incident Documentation:**

If rollback needed, document:
```markdown
## Deployment Incident Report

**Date:** [DATE]
**Project:** [PROJECT_NAME]
**Issue:** [What went wrong]
**Detection:** [How it was detected]
**Impact:** [User impact]
**Resolution:** [How it was fixed]
**Prevention:** [How to prevent in future]
```
```

---

# Updated Phase Structure Summary

After implementing all 12 additions, V3 becomes:

| Phase | Name | Key Additions |
|-------|------|---------------|
| **1.0** | Complexity Classification | 🆕 Type A/B/C/D routing |
| **1.1-1.4** | Information Gathering | ⬆️ + Intensity Tier assignment |
| **1.5** | Hypothesis Formation | 🆕 Testable hypotheses with priors |
| **2** | Deep Research | ⬆️ Full GoT Controller + Red Team + Contradiction Triage + Implications Engine |
| **3** | Research Review | ⬆️ Enhanced verification + Confidence scoring audit |
| **4** | Website Generation | Same |
| **5** | Website Verification | ⬆️ + Data traceability validation |
| **6** | Deployment | ⬆️ + Rollback protocol |

---

# Implementation Roadmap

## Week 1-2: Foundation (P0)
1. Add Phase 1.0: Complexity Classification
2. Add Phase 1.1-1.4: Intensity Tiers
3. Add Phase 1.5: Hypothesis Formation
4. Restore full GoT Controller from V2

## Week 3-4: Quality Frameworks (P1)
1. Add Contradiction Triage to Phase 2
2. Add Implications Engine to Phase 2
3. Enhance Phase 3 verification checklist
4. Create enhanced verification script

## Week 5-6: Depth & Validation (P2)
1. Add Red Team agents to Phase 2
2. Implement Claim Confidence scoring
3. Add Website-Research data validation (Phase 5)
4. Add Deployment rollback protocol (Phase 6)

## Week 7-8: Specialization (P3)
1. Create Healthcare overlay
2. Create Retail/Service overlay
3. Create B2B overlay
4. Update New_question_dynamic.md to load overlays
5. End-to-end testing with all improvements

---

# Quick Reference: Files to Modify

| File | Changes |
|------|---------|
| **Claude.md** (main file) | Add Phases 1.0, 1.5; Enhance Phases 2, 3, 5, 6 |
| **New_question_dynamic.md** | Add hypotheses section, overlay loading, intensity tier |
| **got_state.json** | New file - GoT state tracking |
| **/RESEARCH/OVERLAYS/** | New directory with healthcare.md, retail_service.md, b2b.md |
| **/website/validate_data.py** | New file - data traceability validation |

---

# Conclusion

V3 made the right architectural decision: an end-to-end workflow that takes user input through to a deployed website. This is significantly more valuable than V2's research-only output.

However, the research quality frameworks from V1/V2 feedback must still be integrated. The 12 implementations in this guide transform V3 from:

**Current:** A good workflow system that produces adequate research

**Target:** A world-class system that produces actionable, hypothesis-tested, confidence-scored research with verified website output

Key transformations:
- **From information to insight:** Hypothesis testing ensures conclusions, not just facts
- **From confidence to calibration:** Claim scoring lets users trust the right things
- **From hopeful to verified:** Data traceability ensures website accuracy
- **From deployed to reliable:** Rollback protocols enable confident shipping

Implementing these additions makes V3 the definitive marketing research and delivery system.

---

*— End of V3 Implementation Guide —*