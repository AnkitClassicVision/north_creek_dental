This is the final, consolidated **System Protocol (v4.0)**. It merges your new workflow requirements (Deployment, Website Generation, `New_question_dynamic.md` integration) with the structural improvements from the V3.0 audit (JSON-based state management and adversarial verification).

**Process Update:** I have inserted the **** tag in the Overview to visualize how data flows from the Markdown config into the Graph and finally to the Website.

You can copy and paste the code block below directly into your `Claude.md` file.

---

#Deep Research & Website Generation System (v4.0)##1. System Overview & Trigger**Trigger Phrase:** User says **"read claude.md"** or **"start research"**.
**Objective:** Execute an end-to-end workflow: Scoping → Deep Research (GoT) → Verification → Website Generation → Deployment.

##CRITICAL INSTRUCTION: DO NOT STOP UNTIL COMPLETE**Claude MUST continue working until the ENTIRE workflow is finished.**

```text
┌─────────────────────────────────────────────────────────────────────┐
│  DO NOT STOP until:                                                 │
│  ✓ All research files are generated & verified                      │
│  ✓ Website is generated, verified, and optimized                    │
│  ✓ GitHub Repository is created and pushed                          │
│  ✓ Vercel Deployment is live                                        │
│  ✓ Final Completion Summary is displayed                            │
│                                                                     │
│  ERROR HANDLING PROTOCOL:                                           │
│  1. If Context Limit approaches: Summarize state to file & CONTINUE.│
│  2. If Verification fails: Fix issues, Re-run test, & CONTINUE.     │
│  3. If Tools fail: Use fallback method & CONTINUE.                  │
│                                                                     │
│  THE ONLY ACCEPTABLE STOPPING POINT IS FULL DEPLOYMENT.             │
└─────────────────────────────────────────────────────────────────────┘

```

---

##2. MASTER WORKFLOW1. **PHASE 1: Information Gathering** (Update `New_question_dynamic.md`)
2. **PHASE 2: Deep Research** (Graph of Thoughts + JSON Persistence)
3. **PHASE 3: Research Review** (Adversarial + Codex Verification)
4. **PHASE 4: Website Generation** (Design System Implementation)
5. **PHASE 5: Website Verification** (Performance & Accuracy Check)
6. **PHASE 6: Deployment** (GitHub + Vercel)

---

##PHASE 1: Information Gathering & Configuration###Step 1.1: Intake InterviewWhen triggered, **IMMEDIATELY ASK** for:

1. **Business Name** (Full & Short/Abbreviation)
2. **Website URL** (for initial scraping)
3. **Primary Service** (The main revenue driver)
4. **Secondary Service** (Optional/None)

###Step 1.2: Location Extraction (Automated)*Action:* Use `WebFetch` or `Puppeteer` to scrape the provided URL.

* Search for `/contact`, `/locations`, or Footer.
* **Extract:** All physical addresses and phone numbers.
* **Calculate:** Service Radius (Miles/Drive-time).

###Step 1.3: Update Configuration File (CRITICAL)You must programmatically update the `New_question_dynamic.md` file. This file acts as the "Config Source" for the rest of the process.

**Action:** Read `New_question_dynamic.md`, find the YAML block, and replace variables:

```yaml
company:
  name: "[USER INPUT]"
  shortname: "[USER INPUT]"
  website: "[USER INPUT]"
  address: "[SCRAPED ADDRESSES]"

services:
  primary:
    name: "[USER INPUT]"
    subfolder: "03_Personas/Primary"
  secondary:
    name: "[USER INPUT]"
    subfolder: "03_Personas/Secondary"

research_focus:
  industry: "[DETECTED INDUSTRY]"
  model: "[B2B/B2C]"

```

###Step 1.4: User ConfirmationDisplay the extracted config. **Wait for "YES"** before triggering the Agent Swarm.

---

##PHASE 2: Deep Research (Graph of Thoughts)**Architecture:** Filesystem-based Graph.
**Root Path:** `/RESEARCH/[SHORTNAME]_[SERVICE]_Analysis/`

###Step 2.1: Initialize Graph StateCreate the directory structure and initialize the "Brain":

```bash
mkdir -p /RESEARCH/[SHORTNAME]_Analysis/00_Admin
echo '{ "nodes": [], "frontier": [] }' > /RESEARCH/[SHORTNAME]_Analysis/00_Admin/graph_state.json

```

###Step 2.2: Deploy Research Agents (The Swarm)Deploy agents to populate the folders. **Agents must write JSON Nodes first**, then synthesize Markdown.

**The Agent Roster (30 Agents):**

| Group | Focus | Output Target |
| --- | --- | --- |
| **Foundation** (5) | Demographics, Local Economics, Industry Trends | `02_Market_Analysis/` |
| **Competitive** (5) | Direct/Indirect Competitors, Pricing, SWOT | `04_Competitive_Intelligence/` |
| **Personas** (6) | Psychographics, Pain Points. *Gen Headshots via nanobanana* | `03_Personas/` |
| **Funnels** (5) | CAC, LTV, Unit Economics, Conversion Math | `05_Funnels_Economics/` |
| **Strategy** (5) | Channels, Messaging, Budgeting | `06_Marketing_Strategy/` |
| **Partners** (4) | Strategic Alliances, Local Outreach | `07_Partnerships/` |

**Agent Rules:**

1. **No Wall of Text:** Agents append atomic facts to `00_Admin/findings.jsonl`.
2. **Reference:** Agents must read `New_question_dynamic.md` for scope.
3. **Synthesis:** Once data is mined, create the Markdown files in the respective folders.

###Step 2.3: Progress TrackingUpdate `/RESEARCH/[SHORTNAME]_Analysis/PROGRESS.md` after every agent completes.

---

##PHASE 3: Research Review (Adversarial)**Do not proceed until this phase passes.**

###Step 3.1: The "Red Team" CheckBefore finalizing research, spawn a **Devil's Advocate Agent**.

* **Task:** Pick top 3 strategic claims (e.g., "Market is growing 10%").
* **Action:** Perform negative search ("Market stagnation," "Risks").
* **Output:** If claims survive, mark as `Verified`. If debunked, update the research file.

###Step 3.2: Codex/Claude VerificationUse `Codex Skill` (or fallback to Claude) to audit:

1. **Completeness:** Are all 7 folders populated?
2. **Citations:** Do all facts have `(Source, Year)`?
3. **Math:** Is `LTV > CAC`? Are market sizes realistic?

*If Audit Fails:* Fix issues → Re-run Audit → **CONTINUE.**

---

##PHASE 4: Website Generation**Input:** Confirmed Research from Phase 3.
**Directives:** Read `prompt for website.md` and `deisgn_elements.txt`.

###Step 4.1: Structure GenerationCreate `/website/` structure:

```text
/website/
├── index.html (Landing)
├── executive-summary.html
├── personas.html
├── competitive.html
├── marketing.html
├── funnels.html
├── partnerships.html
└── assets/ (css, js, images)

```

###Step 4.2: Content MappingMap research data to HTML using `website_map_master_template_old.md`.

* *Personas MD* → `personas.html` (Cards)
* *Funnel Math* → `funnels.html` (Tables/Charts)

###Step 4.3: Design System Implementation ("Ethereal Clarity")* **Visuals:** Aurora animated background (GPU optimized).
* **UI:** Glassmorphism cards (Max 5 backdrop-filters).
* **Typography:** Playfair Display (Headers) + Inter (Body).
* **Icons:** Lucide SVG only (No Emojis).

---

##PHASE 5: Website Verification###Step 5.1: Technical Audit1. **Performance:** Are Critical CSS inlined? Images lazy-loaded?
2. **Responsiveness:** Does it work on Mobile?
3. **Motion:** Is `@media (prefers-reduced-motion)` implemented?

###Step 5.2: Content Audit1. **Accuracy:** Does the website data match `/RESEARCH/` files exactly?
2. **Links:** Are all navigation links functional?

*If Verification Fails:* Fix code → Re-verify → **CONTINUE.**

---

##PHASE 6: Deployment (Go Live)###Step 6.1: Git OperationsUse `github-operations-manager`:

1. Initialize Repo: `[SHORTNAME]-growth-system`.
2. Commit all files (Research + Website).
3. Push to main branch.

###Step 6.2: Vercel DeploymentUse `vercel` CLI or skill:

1. Deploy `/website` folder.
2. Target: **Production**.
3. Confirm URL is live (HTTP 200 OK).

---

##COMPLETION SUMMARY**Only display this when Vercel URL is live.**

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🚀 MISSION COMPLETE: SYSTEM DEPLOYED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

► Business: [BUSINESS NAME]
► Strategy: [PRIMARY SERVICE] Growth

1. RESEARCH ARTIFACTS
   Location: /RESEARCH/[FOLDER]/
   Status: Verified & Audited
   • Market Analysis: [COMPLETE]
   • Unit Economics: [COMPLETE]
   • Strategy: [COMPLETE]

2. DIGITAL ASSETS
   Location: /website/
   Design System: Ethereal Clarity
   Performance: Optimized (Aurora/Glassmorphism)

3. LIVE DEPLOYMENT
   📂 GitHub: https://github.com/[USER]/[SHORTNAME]-growth-system
   🌍 Vercel: https://[PROJECT].vercel.app

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```This is a comprehensive **Operational Manual and Architecture Report** for the Deep Research & Website Generation System (V5.0).

It is written specifically for a junior operator. It assumes **zero prior experience** with "Agentic AI" or "Graph of Thoughts." It explains *what* to do, *why* you are doing it, and *how* the system works under the hood.

---

#📘 Operational Manual: Deep Research System V5.0**To:** Junior Operations Team / Project Managers
**From:** Lead Architect
**Date:** October 26, 2025
**Subject:** Master Protocol for Autonomous Research & Website Deployment

---

##Part 1: Executive Summary (The "What" & "Why")###What is this system?This is not a chatbot. It is an **Autonomous Research Engine**. When you give it a business name, it doesn't just "chat" with you. It:

1. **Spawns 30+ "Agents"** (think of them as digital interns) to search the web simultaneously.
2. **Builds a "Knowledge Graph"** (a structured database of facts) instead of just writing paragraphs.
3. **Attacks itself** (The "Red Team") to prove its own research wrong, ensuring high accuracy.
4. **Writes code** to build a fully functional website based on that research.
5. **Deploys** that website to the internet (Vercel).

###Why do we use "Graph of Thoughts"?Most AIs think in a straight line (A → B → C). If they make a mistake at "A," the whole chain fails.
**We use a Graph.** We map facts like a spiderweb. If one path is a dead end, the system cuts it off ("Pruning") and tries another path. This mimics how a human expert solves complex problems.

---

##Part 2: The Architecture (The "Where")You need to understand where the work happens. We do not rely on the AI's "memory" (Context Window) because it forgets things. We rely on the **File System**.

###The "Brain" (JSON vs. Python)* **The JSON File (`graph_state.json`):** This is the **Filing Cabinet**. It stores every fact, number, and source URL. If it's not in this file, it doesn't exist.
* **The Python Scripts:** These are the **Workers**. They read the filing cabinet, update it, or organize it.

###The Directory StructureEvery project follows this **exact** layout. Do not deviate.

```text
/RESEARCH/[Project_Name]/
├── 00_Admin/
│   ├── graph_state.json       <-- The "Brain" (Tracks what we know)
│   ├── findings.jsonl         <-- The "Raw Data" (Every search result)
│   └── research_plan.md       <-- The Strategy Scope
├── 01_Raw_Nodes/              <-- Backup of individual agent outputs
├── 02_Market_Analysis/        <-- Final Reports on Market
├── 03_Personas/               <-- Final Reports on Customers
├── 04_Competitive/            <-- Final Reports on Competitors
├── 05_Funnels_Economics/      <-- Final Reports on Money/Math
├── 06_Marketing_Strategy/     <-- Final Reports on Strategy
├── 07_Partnerships/           <-- Final Reports on Partners
└── images/                    <-- Generated Headshots

```

---

##Part 3: The Operator's Guide (The "How")Follow these steps exactly to run a project.

###Step 1: Trigger the SystemOpen your AI interface (Claude/Opus) and type **one** of these commands:

* `"read claude.md"`
* `"start research"`

###Step 2: The Intake InterviewThe AI will pause and ask you for 4 specific things. You must provide them clearly.

* **Example Input:**
* **Name:** "TechFlow Solutions" (Short: TFS)
* **Website:** "[www.techflow-example.com](https://www.google.com/search?q=https://www.techflow-example.com)"
* **Primary Service:** "Enterprise Cloud Migration"
* **Secondary Service:** "Cybersecurity Consulting"



###Step 3: Configuration Update (The "Handshake")The AI will automatically update a file called `New_question_dynamic.md`.

* **Junior Check:** Look at the file `New_question_dynamic.md`. Does line 15 show the business name you just gave? If yes, proceed. If no, tell the AI: *"You failed to update the config file. Please try again."*

###Step 4: Watch the "Swarm" (Phases 2 & 3)The AI will now launch 30 agents. You do not need to do anything, but you should monitor the `00_Admin/findings.jsonl` file.

* **Success Indicator:** You should see new lines of text appearing in that file every few seconds.
* **Red Team Check:** Look for logs that say "Devil's Advocate." This means the system is checking its own work.

###Step 5: Website Verification (Phase 5)Once the research is done, the AI will generate the website code in `/website/`.

* **Your Job:** Ask the AI: *"Please run the verification checklist."*
* It will check if the links work, if the images load, and if the design matches our "Ethereal Clarity" standard.

###Step 6: Go Live (Phase 6)The AI will attempt to push to GitHub and Vercel.

* **Success Indicator:** It will give you a URL like `https://techflow-growth.vercel.app`.
* **Click the link.** Does it open? If yes, the job is done.

---

##Part 4: The "Agent Swarm" (The "Who")We use three specific types of "Agents." It is critical you understand the difference so you can spot errors.

###Agent Type A: The Miner (The Researcher)**Job:** Go find facts. Do NOT write summaries.
**Output Style:** JSON Data.
**Correct Output Example:**

```json
{
  "type": "fact",
  "content": "The cloud migration market is growing at 15% CAGR.",
  "source": "https://gartner.com/cloud-report",
  "confidence": 9
}

```

**WRONG Output Example:**

> "I found some interesting articles about cloud migration. Gartner says it's growing fast..." (This is bad because it's unstructured text).

###Agent Type B: The Red Team (The Critic)**Job:** Prove the Miner wrong.
**Trigger:** It only looks at "High Confidence" facts (Score > 8).
**Action:** If the Miner says "X is safe," the Red Team searches "X safety failures."
**Why?** To prevent "Hallucinations" (AI making things up).

###Agent Type C: The Synthesis Agent (The Writer)**Job:** Read the JSON files and write the pretty Markdown reports.
**Rule:** It cannot add any new information. It can *only* use what the Miners found.
**Citation Rule:** Every paragraph must end with `(Source, Year)`.

---

##Part 5: Troubleshooting GuideEven the best systems fail. Here is how to fix common issues.

| **Issue** | **Diagnosis** | **The Fix** |
| --- | --- | --- |
| **"I forgot the context."** | The AI says it lost track of where it is. | Tell it: *"Check `PROGRESS.md` and `graph_state.json`. Resume from the last unchecked item."* |
| **"Verification Failed."** | The Website has broken links or bad code. | Do not proceed. Tell it: *"Read the error log. Fix the code in `/website/`. Re-run verification."* |
| **"No Citations Found."** | The reports have no sources. | This is a critical failure. Delete the report and command: *"Re-run Phase 6 Synthesis. Ensure every claim links to a URL from `findings.jsonl`."* |
| **"Deployment Error."** | Vercel fails to deploy. | Usually a token issue. Ask: *"Check your Vercel credentials. Try deploying manually using `vercel --prod`."* |

---

##Part 6: Final Deliverables ChecklistBefore you tell your boss (or client) the project is done, you must verify these 4 items exist:

1. [ ] **The Research Folder:** `/RESEARCH/[Shortname]_Analysis/` is full of Markdown files.
2. [ ] **The "Brain" Logs:** `00_Admin/findings.jsonl` has data in it.
3. [ ] **The Code:** `/website/` contains `index.html` and `assets/`.
4. [ ] **The Live Link:** A working Vercel URL.

**End of Manual.**