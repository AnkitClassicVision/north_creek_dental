# Codex Review Remediation Plan

## Document Metadata
| Field | Value |
|-------|-------|
| **Created** | December 14, 2025 |
| **Source** | Codex Review (gpt-5.2) |
| **Current Status** | **PASS** |
| **Target Status** | PASS |

---

## Remediation Tasks

### TASK 1: Fix New_question_dynamic.md Update Markers
**Priority:** HIGH
**Files:** `Claude.md:250`, `New_question_dynamic.md:13`

**Problem:** Claude.md instructs updating between `# BEGIN INPUT VARIABLES ... # END INPUT VARIABLES` markers that don't exist in New_question_dynamic.md.

**Pass Criteria:**
- [x] New_question_dynamic.md contains `# BEGIN INPUT VARIABLES` marker before the yaml block
- [x] New_question_dynamic.md contains `# END INPUT VARIABLES` marker after the yaml block
- [x] Claude.md Step 1.3 references these markers correctly
- [x] Grep verification: `grep -c "BEGIN INPUT VARIABLES" New_question_dynamic.md` returns 1

**Status:** ✅ COMPLETE

---

### TASK 2: Fix Invalid YAML Examples
**Priority:** HIGH
**Files:** `Claude.md:262`, `New_question_dynamic.md:19`

**Problem:** Address pattern `address: "[...]" and "[...]"` is invalid YAML syntax.

**Pass Criteria:**
- [x] Address field uses valid YAML list syntax: `addresses: ["addr1", "addr2"]`
- [x] All YAML blocks in Claude.md pass `yamllint` or similar validation
- [x] Pattern is consistent across both files
- [x] Grep verification: `grep -c '".*" and "' Claude.md` returns 0

**Status:** ✅ COMPLETE

---

### TASK 3: Fix Agent Budgeting Conflicts
**Priority:** HIGH
**Files:** `Claude.md:559`, `Claude.md:868`

**Problem:** GoT state sets `total_agents: 30`, but Phase 2 agent allocation totals 32.

**Pass Criteria:**
- [x] GoT state `total_agents` matches the sum of Phase 2 agent allocation
- [x] OR tier-based scaling is explicitly documented
- [x] Budget numbers are consistent throughout the document
- [x] Grep verification: Sum of agents in allocation = total_agents value

**Status:** ✅ COMPLETE (tier-based scaling documented)

---

### TASK 4: Fix Deployment Verification Snippet
**Priority:** HIGH
**Files:** `Claude.md:1502`, `Claude.md:1508`

**Problem:** Page loop checks `/.html` due to empty string; image paths don't match conventions.

**Pass Criteria:**
- [x] Page array contains only valid page names (no empty strings)
- [x] Image path pattern matches earlier persona image conventions
- [x] Verification script is syntactically correct bash
- [x] All file paths are consistent with earlier definitions

**Status:** ✅ COMPLETE

---

### TASK 5: Clarify GoT Scoring Scale
**Priority:** MEDIUM
**Files:** `Claude.md:595`, `Claude.md:607`

**Problem:** Rubric says 0–10 but formula likely yields 0–20; dimension ranges undefined.

**Pass Criteria:**
- [x] Each scoring dimension has explicit range (e.g., 0-5 or 0-10)
- [x] Formula produces result in documented range
- [x] Example calculation demonstrates correct scoring
- [x] Grep verification: Dimension ranges are specified

**Status:** ✅ COMPLETE (dimensions 0-5, weighted sum * 2 = 0-10)

---

### TASK 6: Add Missing Planned Deliverables
**Priority:** MEDIUM
**Files:** `Claude.md`, `IMPLEMENTATION_PLAN.md:276,399,371,697`

**Problem:** Data Traceability Matrix, "Derived-Only Rule", GoT state verification checklist, overlay auto-detection not in Claude.md.

**Pass Criteria:**
- [x] Data Traceability Matrix template exists in Claude.md
- [x] "Derived-Only Rule" or equivalent wording present
- [x] GoT state verification checklist in Phase 3
- [x] Overlay auto-detection logic documented
- [x] Grep verification: `grep -c "Data Traceability\|Derived-Only" Claude.md` returns 2+

**Status:** ✅ COMPLETE

---

### TASK 7: Fix IMPLEMENTATION_PLAN.md Status Contradictions
**Priority:** MEDIUM
**Files:** `IMPLEMENTATION_PLAN.md:10`, `IMPLEMENTATION_PLAN.md:868`

**Problem:** Metadata says "Planning Phase" but later says "COMPLETE".

**Pass Criteria:**
- [x] Status field in metadata table says "COMPLETE" (or "Implementation Complete")
- [x] All execution checkboxes are marked [x] instead of [ ]
- [x] No conflicting status indicators
- [x] Grep verification: `grep "Planning Phase" IMPLEMENTATION_PLAN.md` returns nothing

**Status:** ✅ COMPLETE

---

### TASK 8: Normalize Skill/Tool Terminology
**Priority:** LOW
**Files:** `Claude.md:96`, `Claude.md:110`, `Claude.md:125`, `Claude.md:144`

**Problem:** `vercel` vs `vercel_skill`, "Full 7-phase process" doesn't match 9-phase structure.

**Pass Criteria:**
- [x] Consistent skill naming (either all `vercel` or all `vercel_skill`)
- [x] Phase count references match actual structure (9 phases: 0, 1, 1.1, 1.5, 2, 3, 4, 5, 6)
- [x] All skill references use same naming convention
- [x] Grep verification: `grep -c "vercel_skill" Claude.md` returns 0 OR all references use it

**Status:** ✅ COMPLETE (normalized to `vercel`, phases 0-6)

---

### TASK 9: Fix content_map.json Path Ambiguity
**Priority:** LOW
**Files:** `Claude.md:1253`, `Claude.md:483`

**Problem:** Source file paths don't clearly align to `03_research/` structure.

**Pass Criteria:**
- [x] content_map.json example shows paths relative to research root
- [x] Comment or note clarifies path convention
- [x] Paths are consistent with folder structure defined earlier
- [x] Example includes `03_research/` prefix OR explicitly states "relative to 03_research/"

**Status:** ✅ COMPLETE

---

### TASK 10: Enhance Domain Overlays
**Priority:** LOW
**Files:** `DOMAIN_OVERLAYS/*.md`

**Problem:** Missing paywall-free fallback sources and "when in doubt" guidance.

**Pass Criteria:**
- [x] Each overlay has "Fallback Sources" section with free alternatives
- [x] Each overlay has "When in Doubt" guidance for regulated claims
- [x] Legal: mentions court sites, Google Scholar
- [x] Financial: mentions EDGAR, FRED, regulator sites
- [x] Healthcare: mentions PubMed, CDC, state licensing boards

**Status:** ✅ COMPLETE

---

## Verification Commands

```bash
# Task 1: Check markers exist
grep -c "BEGIN INPUT VARIABLES" New_question_dynamic.md

# Task 2: Check invalid YAML pattern removed
grep -c '".*" and "' Claude.md New_question_dynamic.md

# Task 3: Check agent counts
grep -n "total_agents" Claude.md
grep -n "market_foundation:" Claude.md

# Task 4: Check deployment snippet
grep -A5 "pages=(" Claude.md

# Task 5: Check scoring dimensions
grep -n "dimension" Claude.md | grep -i "range\|score"

# Task 6: Check missing deliverables
grep -c "Data Traceability\|Derived-Only\|auto-detect" Claude.md

# Task 7: Check status consistency
grep "Status.*Planning" IMPLEMENTATION_PLAN.md

# Task 8: Check terminology
grep -c "vercel_skill" Claude.md
grep -c "7-phase" Claude.md

# Task 9: Check path clarity
grep -B2 -A2 "source_file" Claude.md

# Task 10: Check overlay enhancements
grep -c "Fallback\|When in Doubt" DOMAIN_OVERLAYS/*.md
```

---

## Final Verification

After all tasks complete, run Codex review again:
```bash
codex exec "Review Claude.md, IMPLEMENTATION_PLAN.md, and DOMAIN_OVERLAYS/ for the issues previously identified. Confirm PASS or identify remaining issues."
```

**Target:** Overall Assessment = PASS

---

*End of Remediation Plan*
