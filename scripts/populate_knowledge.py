#!/usr/bin/env python3
"""
Populate the deep_resserach_to_website concept package knowledge river map.

This map is derived from the workflow docs vendored in:
  reference/template_deep_reserach/
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "knowledge" / "knowledge.db"

MAP_ID = "default"
ROOT_NODE_ID = "node_root"  # present in the template DB


def upsert_node(
    conn: sqlite3.Connection,
    *,
    node_id: str,
    label: str,
    short_def: str | None = None,
    why_important: str | None = None,
    deep_dive: str | None = None,
    example: str | None = None,
    eli5: str | None = None,
    tags: str | None = None,
) -> None:
    conn.execute(
        """
        INSERT INTO node (id, map_id, label, short_def, why_important, deep_dive, example, eli5, tags)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
          map_id=excluded.map_id,
          label=excluded.label,
          short_def=excluded.short_def,
          why_important=excluded.why_important,
          deep_dive=excluded.deep_dive,
          example=excluded.example,
          eli5=excluded.eli5,
          tags=excluded.tags
        """,
        (
            node_id,
            MAP_ID,
            label,
            short_def,
            why_important,
            deep_dive,
            example,
            eli5,
            tags,
        ),
    )


def insert_edge(
    conn: sqlite3.Connection,
    *,
    edge_id: str,
    from_node_id: str,
    to_node_id: str,
    rel_type_id: str,
    is_trunk: int,
    branch_order: int,
    notes: str | None = None,
) -> None:
    conn.execute(
        """
        INSERT INTO edge (id, map_id, from_node_id, to_node_id, rel_type_id, is_trunk, branch_order, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            edge_id,
            MAP_ID,
            from_node_id,
            to_node_id,
            rel_type_id,
            is_trunk,
            branch_order,
            notes,
        ),
    )


def reset_map_content(conn: sqlite3.Connection) -> None:
    conn.execute("PRAGMA foreign_keys = ON")

    # Clear edges, and all nodes except the root node present in the template DB.
    conn.execute("DELETE FROM edge WHERE map_id = ?", (MAP_ID,))
    conn.execute("DELETE FROM node WHERE map_id = ? AND id != ?", (MAP_ID, ROOT_NODE_ID))

    # Update map metadata (keep map_id stable as `default` for export convenience).
    conn.execute(
        """
        UPDATE map
        SET name = ?, description = ?, root_node_id = ?, max_depth = 5, max_children = 4
        WHERE id = ?
        """,
        (
            "deep_resserach_to_website",
            "End-to-end workflow: classify → scope → hypothesize → deep research (GoT) → verify → generate website → verify → deploy.",
            ROOT_NODE_ID,
            MAP_ID,
        ),
    )


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        reset_map_content(conn)

        # ------------------------------------------------------------------
        # Nodes
        # ------------------------------------------------------------------
        upsert_node(
            conn,
            node_id=ROOT_NODE_ID,
            label="Deep Research → Website",
            short_def="System for turning a research request into a deployed, research-backed website.",
            why_important="Creates a repeatable, verifiable pipeline from ambiguity to a live site with strong UX, accurate claims, and clear artifacts.",
            deep_dive=(
                "Trunk phases (0→6): Complexity classification → Information gathering → Research intensity → Hypothesis formation → Deep research (GoT) → Research review → Website generation → Website verification → Deployment.\n"
                "Source-of-truth workflow docs are vendored in `reference/template_deep_reserach/`."
            ),
            example="Use `reference/template_deep_reserach/New_question_dynamic.md` to scope inputs, then follow the phase workflow to produce `/RESEARCH` + `/website` artifacts.",
            eli5="Figure out what to learn, double-check it, then build a website from it and put it live.",
            tags="root,workflow,deep-research,website",
        )

        # Root branches (avoid single-child root)
        upsert_node(
            conn,
            node_id="reference_materials",
            label="Reference Materials",
            short_def="Vendored source docs that define the workflow and templates.",
            why_important="Keeps the concept grounded in the actual process docs and prevents drift.",
            deep_dive="See `reference/template_deep_reserach/` for the full spec, prompts, and overlays.",
            example="Open `reference/template_deep_reserach/Claude.md` for the complete phase-by-phase workflow.",
            eli5="The original instructions and templates.",
            tags="reference,source",
        )

        upsert_node(
            conn,
            node_id="artifacts_folder_structure",
            label="Artifacts & Folder Structure",
            short_def="The files and folders the workflow expects and produces.",
            why_important="Makes work auditable and enables deterministic handoff from research → website → deployment.",
            deep_dive="Key artifacts include the input YAML, `/RESEARCH` outputs (including evidence ledger), and `/website` build output.",
            example="Keep persona images in `/RESEARCH/images/` and copy into `/website/assets/images/` as needed.",
            eli5="Where everything goes.",
            tags="artifacts,folders",
        )

        # Reference materials
        upsert_node(
            conn,
            node_id="ref_workflow_spec",
            label="Workflow Spec (Claude.md)",
            short_def="End-to-end phase workflow: classification → research → website → deploy.",
            why_important="Defines the phases, gates, and stop rules for the system.",
            deep_dive="Source: `reference/template_deep_reserach/Claude.md`.",
            example="Follow the trunk phases 0–6 and do not stop until COMPLETE or BLOCKED.",
            eli5="The master playbook.",
            tags="reference,workflow",
        )

        upsert_node(
            conn,
            node_id="ref_research_request_template",
            label="Research Request Template (New_question_dynamic.md)",
            short_def="YAML input template + dynamic folder contract for research.",
            why_important="Standardizes inputs (company/services/market) so research agents and website generation stay consistent.",
            deep_dive="Source: `reference/template_deep_reserach/New_question_dynamic.md`.",
            example="Fill in `company.name`, `company.website`, and `services.primary.name` before starting research.",
            eli5="The form you fill out to start.",
            tags="reference,inputs",
        )

        upsert_node(
            conn,
            node_id="ref_website_creation_prompt",
            label="Website Creation Prompt",
            short_def="Instructions for generating the website from research artifacts.",
            why_important="Prevents mismatches between research outputs and website pages, and enforces consistent UI rules.",
            deep_dive="Source: `reference/template_deep_reserach/prompt for website.md`.",
            example="Use `website_map_master_template_old.md` for page structure and `deisgn_elements.txt` for Ethereal Clarity design.",
            eli5="How to build the site from the research.",
            tags="reference,website",
        )

        # Artifacts & folders
        upsert_node(
            conn,
            node_id="artifact_input_variables",
            label="Input Variables (YAML)",
            short_def="Standardized YAML inputs for the research request.",
            why_important="Inputs drive folder structure, agent allocation, and website data binding.",
            deep_dive="Defined in `reference/template_deep_reserach/New_question_dynamic.md` between the INPUT VARIABLES markers.",
            example="Include `company.website` and service names so logo extraction and page generation can proceed.",
            eli5="The details you provide up front.",
            tags="artifacts,inputs,yaml",
        )

        upsert_node(
            conn,
            node_id="artifact_research_folder",
            label="Research Output Folder (/RESEARCH)",
            short_def="Research artifacts: summaries, raw notes, evidence ledger, and images.",
            why_important="Preserves traceability from claims to sources and supports downstream website generation.",
            deep_dive="Includes an evidence ledger (claims + sources) and generated persona images under `/RESEARCH/images/`.",
            example="Save the company logo to `/RESEARCH/images/[COMPANY_SHORTNAME]_logo.png`.",
            eli5="The research binder.",
            tags="artifacts,research",
        )

        upsert_node(
            conn,
            node_id="artifact_website_folder",
            label="Website Output Folder (/website)",
            short_def="Static website generated from research outputs and templates.",
            why_important="Turns synthesized research into a clear, navigable deliverable that can be deployed.",
            deep_dive="Website pages follow the template map and embed research outputs (personas, competitive analysis, funnels, marketing, partnerships).",
            example="Copy persona headshots from `/RESEARCH/images/` into `/website/assets/images/personas/`.",
            eli5="The final site files.",
            tags="artifacts,website",
        )

        # Trunk phases
        upsert_node(
            conn,
            node_id="phase0_complexity",
            label="Phase 0 — Complexity Classification",
            short_def="Classify the request (A/B/C/D) to route effort and tooling.",
            why_important="Prevents over-engineering simple lookups and under-resourcing high-stakes investigations.",
            deep_dive="Types: A (Lookup), B (Synthesis), C (Analysis), D (Investigation).",
            example="Type A: one authoritative source; Type D: novel/high-stakes, requires red team and deeper verification.",
            eli5="Decide how big the job is before starting.",
            tags="phase,classification",
        )

        upsert_node(
            conn,
            node_id="phase1_info_gathering",
            label="Phase 1 — Information Gathering",
            short_def="Collect required inputs and update the request template.",
            why_important="Bad inputs cascade into bad research and broken websites; gather and confirm early.",
            deep_dive="Includes business name, shortname, website URL, addresses, services, and research focus.",
            example="If hours/timezone are unclear, ask explicitly and record the assumption.",
            eli5="Get the details you need.",
            tags="phase,inputs",
        )

        upsert_node(
            conn,
            node_id="phase1_1_intensity",
            label="Phase 1.1 — Research Intensity",
            short_def="Pick intensity tier (Express/Standard/Comprehensive/Enterprise).",
            why_important="Sets time budget, number of agents, and verification depth.",
            deep_dive="Tier choice should reflect service count, location count, market complexity, and stakes.",
            example="Enterprise tier uses more searches, deeper verification, and stronger evidence requirements.",
            eli5="How deep are we going?",
            tags="phase,budget",
        )

        upsert_node(
            conn,
            node_id="phase1_5_hypotheses",
            label="Phase 1.5 — Hypothesis Formation",
            short_def="Draft testable market/competitive/growth hypotheses with priors.",
            why_important="Keeps research focused and makes verification measurable.",
            deep_dive="Hypotheses should have confirming/disconfirming evidence and test queries.",
            example="Create 6–9 hypotheses with 0.xx priors and track status in PROGRESS.",
            eli5="Make educated guesses to test.",
            tags="phase,hypotheses",
        )

        upsert_node(
            conn,
            node_id="phase2_deep_research",
            label="Phase 2 — Deep Research (GoT)",
            short_def="Run Graph of Thoughts research with evidence ledger and red teaming.",
            why_important="Produces higher-quality synthesis by exploring multiple paths and filtering weak sources.",
            deep_dive="Use GoT nodes/edges, scoring, pruning, and an evidence ledger with independence groups.",
            example="Generate → Aggregate → Refine → RedTeam loops until budget or saturation stop condition.",
            eli5="Research widely, then narrow to what’s true.",
            tags="phase,research,got",
        )

        upsert_node(
            conn,
            node_id="phase3_research_review",
            label="Phase 3 — Research Review",
            short_def="Verify claims, citations, and reasoning; fix until PASS.",
            why_important="Prevents incorrect claims from reaching the website and deployment.",
            deep_dive="Run checklists, validate sources, and resolve contradictions before moving forward.",
            example="If verification fails, patch the research outputs and rerun the checklist.",
            eli5="Double-check the work.",
            tags="phase,verification",
        )

        upsert_node(
            conn,
            node_id="phase4_website_generation",
            label="Phase 4 — Website Generation",
            short_def="Bind research outputs into the website structure and design system.",
            why_important="Turns research into a readable deliverable with consistent IA and premium UX.",
            deep_dive="Use the website map template, enforce Ethereal Clarity styling, and replace emojis with Lucide icons.",
            example="Create the full page set and ensure navigation is consistent across pages.",
            eli5="Build the site from the research.",
            tags="phase,website",
        )

        upsert_node(
            conn,
            node_id="phase5_website_verification",
            label="Phase 5 — Website Verification",
            short_def="Review each page for design compliance, data accuracy, navigation, and performance.",
            why_important="Catches broken links, missing assets, inconsistent styling, and performance regressions before deploy.",
            deep_dive="Includes page-by-page checks, Core Web Vitals targets, and asset sizing rules.",
            example="Verify no emojis remain; ensure all images have width/height attributes to avoid CLS.",
            eli5="Make sure the site is correct and fast.",
            tags="phase,qa",
        )

        upsert_node(
            conn,
            node_id="phase6_deployment",
            label="Phase 6 — Deployment",
            short_def="Push to GitHub and deploy to Vercel; verify live.",
            why_important="Completes the workflow with a shareable, live URL and auditable history.",
            deep_dive="If blocked externally, create BLOCKERS.md with exact error + next step.",
            example="Deploy to Vercel, then check all pages load and assets resolve on the live domain.",
            eli5="Put it on the internet.",
            tags="phase,deployment",
        )

        # Phase 0 details
        upsert_node(
            conn,
            node_id="phase0_type_routing",
            label="Type Routing (A/B/C/D)",
            short_def="Routing logic for which phases to execute by request type.",
            why_important="Aligns effort to complexity and stakes.",
            deep_dive="Defined in `reference/template_deep_reserach/Claude.md` under Phase 0.",
            example="Type A may skip most phases; Type C/D runs full 0–6 workflow.",
            eli5="Different jobs get different processes.",
            tags="phase0,routing",
        )

        upsert_node(
            conn,
            node_id="phase0_classification_prompt",
            label="Classification Prompt",
            short_def="Copy-paste prompt for classifying the request.",
            why_important="Standardizes how complexity is evaluated.",
            deep_dive="Includes service count, locations, market complexity, relationship, and stakes.",
            example="Answer the 5 evaluation questions, then choose A/B/C/D with reasoning.",
            eli5="A checklist to label the job.",
            tags="phase0,prompt",
        )

        # Phase 1 details
        upsert_node(
            conn,
            node_id="phase1_required_questions",
            label="Required Questions",
            short_def="The minimum questions to ask before starting research.",
            why_important="Ensures the research and website are scoped correctly.",
            deep_dive="Includes company name, short name, website, addresses, services, and research focus.",
            example="If multiple locations exist, record all addresses as a YAML list.",
            eli5="What you need to ask first.",
            tags="phase1,inputs",
        )

        upsert_node(
            conn,
            node_id="phase1_logo_extraction",
            label="Logo Extraction",
            short_def="Extract and store the company logo for research and website use.",
            why_important="The logo is required for a coherent website header/footer and branding.",
            deep_dive="Save to `/RESEARCH/images/[COMPANY_SHORTNAME]_logo.png` and copy to the website assets folder.",
            example="Prefer SVG or transparent PNG when available.",
            eli5="Grab the company logo.",
            tags="phase1,assets",
        )

        # Phase 1.1 details
        upsert_node(
            conn,
            node_id="phase1_1_tier_table",
            label="Intensity Tiers",
            short_def="Express/Standard/Comprehensive/Enterprise tier definitions.",
            why_important="Determines how much research and verification to do.",
            deep_dive="Tiering considers service count, location count, market complexity, and client value.",
            example="Use Enterprise tier for strategic, high-stakes decisions.",
            eli5="Pick a depth level.",
            tags="phase1_1,tier",
        )

        upsert_node(
            conn,
            node_id="phase1_1_skill_plan",
            label="Skill Allocation Plan",
            short_def="Which tools/skills to use per phase (research, verification, images, deployment).",
            why_important="Ensures the right tool is used for the job and verification is independent.",
            deep_dive="Primary patterns: Perplexity for research, Codex for verification, Nanobanana for images, Vercel for deploy.",
            example="Use Codex at Phase 3/5 for audit-style verification before proceeding.",
            eli5="Use the right tool at the right time.",
            tags="phase1_1,skills",
        )

        # Phase 1.5 details
        upsert_node(
            conn,
            node_id="phase1_5_hypothesis_templates",
            label="Hypothesis Templates",
            short_def="Templates for market, competitive, and growth hypotheses (H-M/H-C/H-G).",
            why_important="Keeps hypotheses testable and structured.",
            deep_dive="Include confirming + disconfirming evidence requirements and test queries.",
            example="Write 2–3 hypotheses per category with a 0.xx prior probability.",
            eli5="Reusable hypothesis shapes.",
            tags="phase1_5,templates",
        )

        upsert_node(
            conn,
            node_id="phase1_5_tracking",
            label="Priors, Tests, and Tracking",
            short_def="How to assign priors and track hypothesis status through research.",
            why_important="Prevents “hand-wavy” conclusions and forces explicit uncertainty management.",
            deep_dive="Track status in PROGRESS with links to evidence ledger entries.",
            example="Mark hypotheses as Confirmed, Disconfirmed, or Inconclusive with citations.",
            eli5="Keep score as you learn.",
            tags="phase1_5,tracking",
        )

        # Phase 2 details
        upsert_node(
            conn,
            node_id="phase2_got_controller",
            label="GoT Controller",
            short_def="Graph of Thoughts controller: nodes/edges, scoring, pruning, and traversal.",
            why_important="Coordinates parallel research paths and filters low-quality sources and claims.",
            deep_dive="Includes Generate/Aggregate/Refine/RedTeam transformations and a budget-based stop condition.",
            example="Prune candidates below a threshold score and keep best-per-depth.",
            eli5="A system for managing lots of research threads.",
            tags="phase2,got",
        )

        upsert_node(
            conn,
            node_id="phase2_evidence_ledger",
            label="Evidence Ledger & Claim Confidence",
            short_def="Track claims, sources, independence groups, and confidence (C1/C2/C3).",
            why_important="Enables audits and prevents weakly-supported claims from leaking into outputs.",
            deep_dive="Maintain a ledger with citations and independence grouping; score and verify claims before synthesis.",
            example="Mark a claim as C3 only with multiple independent, high-authority sources.",
            eli5="A spreadsheet of what you think is true and why.",
            tags="phase2,evidence",
        )

        upsert_node(
            conn,
            node_id="phase2_red_team_overlays",
            label="Red Team + Domain Overlays",
            short_def="Negative searches and domain-specific constraints for regulated topics.",
            why_important="Finds counterevidence and enforces safer claims in regulated domains.",
            deep_dive="Use `reference/template_deep_reserach/DOMAIN_OVERLAYS/` for domain-specific sources and “when in doubt” guidance.",
            example="Healthcare overlay should bias toward PubMed/CDC/state boards over blogs.",
            eli5="Try to prove yourself wrong, with domain rules.",
            tags="phase2,red-team,overlays",
        )

        # Phase 3 details
        upsert_node(
            conn,
            node_id="phase3_verification_checklist",
            label="Verification Checklist",
            short_def="Checklist for research correctness before website generation.",
            why_important="Prevents compounding errors downstream.",
            deep_dive="Validate citations, resolve contradictions, and ensure deliverables exist before moving to Phase 4.",
            example="If any checklist item fails, update research artifacts and re-run the review.",
            eli5="A list of checks before you continue.",
            tags="phase3,checklist",
        )

        upsert_node(
            conn,
            node_id="phase3_fix_loop",
            label="Fix-Until-PASS Loop",
            short_def="Iterate until the research review gate passes.",
            why_important="Ensures the system doesn’t advance with known errors.",
            deep_dive="If context limits or blockers happen, summarize state to file and continue or declare BLOCKED.",
            example="When a claim fails verification, downgrade confidence or find better sources and update the ledger.",
            eli5="Keep fixing until it’s good.",
            tags="phase3,loop",
        )

        # Phase 4 details
        upsert_node(
            conn,
            node_id="phase4_site_structure",
            label="Website Map & Pages",
            short_def="Information architecture and page list for the generated website.",
            why_important="Keeps content organized and navigable across the deliverable.",
            deep_dive="Source: `reference/template_deep_reserach/website_map_master_template_old.md`.",
            example="Typical pages: Home, Executive Summary, Personas, Competitive, Funnels, Marketing, Partnerships.",
            eli5="What pages to build and what goes on them.",
            tags="phase4,ia",
        )

        upsert_node(
            conn,
            node_id="phase4_data_binding",
            label="Research-to-Website Data Binding",
            short_def="Rules for mapping research artifacts into website content.",
            why_important="Prevents stale or mismatched data and supports traceability.",
            deep_dive="Use a content map (e.g., content_map.json) so every page section points back to a research source file.",
            example="If a persona card exists on the site, it must map to a persona definition in the research outputs.",
            eli5="Connect the research to the site content.",
            tags="phase4,data-binding",
        )

        upsert_node(
            conn,
            node_id="phase4_design_system",
            label="Design System (Ethereal Clarity)",
            short_def="Glass cards + aurora background + premium typography + Lucide icons (no emojis).",
            why_important="Ensures a consistent, high-quality aesthetic across all pages.",
            deep_dive="Source: `reference/template_deep_reserach/deisgn_elements.txt` (note filename spelling).",
            example="Use Playfair Display for headings and Inter for body; use Lucide SVG icons with thin stroke.",
            eli5="The look and feel rules.",
            tags="phase4,design",
        )

        # Phase 5 details
        upsert_node(
            conn,
            node_id="phase5_design_review",
            label="Design Compliance Review",
            short_def="Page-by-page check against the design system.",
            why_important="Prevents UI drift and “almost finished” deliverables.",
            deep_dive="Confirm aurora background, glassmorphism, typography, no pure black/white, and Lucide icons only.",
            example="Replace every emoji with a Lucide SVG.",
            eli5="Make it match the design rules.",
            tags="phase5,design",
        )

        upsert_node(
            conn,
            node_id="phase5_data_nav_review",
            label="Data Accuracy & Navigation Review",
            short_def="Validate content matches research and all links work.",
            why_important="Incorrect or broken pages undermine credibility.",
            deep_dive="Verify persona/competitive/funnel data, and ensure consistent nav/footer across pages.",
            example="Check active nav indicator and that every page is reachable.",
            eli5="Make sure it’s correct and clickable.",
            tags="phase5,data,nav",
        )

        upsert_node(
            conn,
            node_id="phase5_performance",
            label="Performance Optimization (Core Web Vitals)",
            short_def="Meet LCP/FID/CLS targets and keep page weight low.",
            why_important="Fast pages improve UX and credibility; avoid regressions with CLS-safe images and deferred assets.",
            deep_dive="Targets: LCP < 2.5s, FID < 100ms, CLS < 0.1, total weight < 1.5MB.",
            example="Include width/height on all images; lazy-load below-fold images; defer non-critical JS.",
            eli5="Make it load quickly.",
            tags="phase5,performance",
        )

        # Phase 6 details
        upsert_node(
            conn,
            node_id="phase6_github",
            label="GitHub Repo + Push",
            short_def="Create repo, commit artifacts, and push history.",
            why_important="Enables collaboration, review, and traceability for deployment.",
            deep_dive="Repo should include the website output and any required build/verification scripts.",
            example="Commit with clear messages per phase or per deliverable set.",
            eli5="Put it in version control.",
            tags="phase6,git",
        )

        upsert_node(
            conn,
            node_id="phase6_vercel",
            label="Vercel Deploy + Live Verification",
            short_def="Deploy and confirm the live site works end-to-end.",
            why_important="Ensures the deliverable is actually reachable and correct in production.",
            deep_dive="Verify all pages load, assets resolve, and performance is acceptable on the live URL.",
            example="If deployment fails, create BLOCKERS.md with the exact error and next steps.",
            eli5="Ship it and check it.",
            tags="phase6,vercel",
        )

        # ------------------------------------------------------------------
        # Edges
        # ------------------------------------------------------------------
        # Root → trunk start + root branches
        insert_edge(
            conn,
            edge_id="edge_root__phase0",
            from_node_id=ROOT_NODE_ID,
            to_node_id="phase0_complexity",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_root__reference_materials",
            from_node_id=ROOT_NODE_ID,
            to_node_id="reference_materials",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_root__artifacts_folder_structure",
            from_node_id=ROOT_NODE_ID,
            to_node_id="artifacts_folder_structure",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        # Reference materials children
        insert_edge(
            conn,
            edge_id="edge_reference_materials__ref_workflow_spec",
            from_node_id="reference_materials",
            to_node_id="ref_workflow_spec",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_reference_materials__ref_research_request_template",
            from_node_id="reference_materials",
            to_node_id="ref_research_request_template",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_reference_materials__ref_website_creation_prompt",
            from_node_id="reference_materials",
            to_node_id="ref_website_creation_prompt",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        # Artifacts children
        insert_edge(
            conn,
            edge_id="edge_artifacts_folder_structure__artifact_input_variables",
            from_node_id="artifacts_folder_structure",
            to_node_id="artifact_input_variables",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_artifacts_folder_structure__artifact_research_folder",
            from_node_id="artifacts_folder_structure",
            to_node_id="artifact_research_folder",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_artifacts_folder_structure__artifact_website_folder",
            from_node_id="artifacts_folder_structure",
            to_node_id="artifact_website_folder",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        # Trunk: phase 0 → 6
        insert_edge(
            conn,
            edge_id="edge_phase0__phase1",
            from_node_id="phase0_complexity",
            to_node_id="phase1_info_gathering",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase0__phase0_type_routing",
            from_node_id="phase0_complexity",
            to_node_id="phase0_type_routing",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase0__phase0_classification_prompt",
            from_node_id="phase0_complexity",
            to_node_id="phase0_classification_prompt",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        insert_edge(
            conn,
            edge_id="edge_phase1__phase1_1",
            from_node_id="phase1_info_gathering",
            to_node_id="phase1_1_intensity",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase1__phase1_required_questions",
            from_node_id="phase1_info_gathering",
            to_node_id="phase1_required_questions",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase1__phase1_logo_extraction",
            from_node_id="phase1_info_gathering",
            to_node_id="phase1_logo_extraction",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        insert_edge(
            conn,
            edge_id="edge_phase1_1__phase1_5",
            from_node_id="phase1_1_intensity",
            to_node_id="phase1_5_hypotheses",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase1_1__tier_table",
            from_node_id="phase1_1_intensity",
            to_node_id="phase1_1_tier_table",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase1_1__skill_plan",
            from_node_id="phase1_1_intensity",
            to_node_id="phase1_1_skill_plan",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        insert_edge(
            conn,
            edge_id="edge_phase1_5__phase2",
            from_node_id="phase1_5_hypotheses",
            to_node_id="phase2_deep_research",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase1_5__hypothesis_templates",
            from_node_id="phase1_5_hypotheses",
            to_node_id="phase1_5_hypothesis_templates",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase1_5__tracking",
            from_node_id="phase1_5_hypotheses",
            to_node_id="phase1_5_tracking",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        insert_edge(
            conn,
            edge_id="edge_phase2__phase3",
            from_node_id="phase2_deep_research",
            to_node_id="phase3_research_review",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase2__got_controller",
            from_node_id="phase2_deep_research",
            to_node_id="phase2_got_controller",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase2__evidence_ledger",
            from_node_id="phase2_deep_research",
            to_node_id="phase2_evidence_ledger",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )
        insert_edge(
            conn,
            edge_id="edge_phase2__red_team_overlays",
            from_node_id="phase2_deep_research",
            to_node_id="phase2_red_team_overlays",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=4,
        )

        insert_edge(
            conn,
            edge_id="edge_phase3__phase4",
            from_node_id="phase3_research_review",
            to_node_id="phase4_website_generation",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase3__verification_checklist",
            from_node_id="phase3_research_review",
            to_node_id="phase3_verification_checklist",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase3__fix_loop",
            from_node_id="phase3_research_review",
            to_node_id="phase3_fix_loop",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )

        insert_edge(
            conn,
            edge_id="edge_phase4__phase5",
            from_node_id="phase4_website_generation",
            to_node_id="phase5_website_verification",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase4__site_structure",
            from_node_id="phase4_website_generation",
            to_node_id="phase4_site_structure",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase4__data_binding",
            from_node_id="phase4_website_generation",
            to_node_id="phase4_data_binding",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )
        insert_edge(
            conn,
            edge_id="edge_phase4__design_system",
            from_node_id="phase4_website_generation",
            to_node_id="phase4_design_system",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=4,
        )

        insert_edge(
            conn,
            edge_id="edge_phase5__phase6",
            from_node_id="phase5_website_verification",
            to_node_id="phase6_deployment",
            rel_type_id="rel_precedes",
            is_trunk=1,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase5__design_review",
            from_node_id="phase5_website_verification",
            to_node_id="phase5_design_review",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )
        insert_edge(
            conn,
            edge_id="edge_phase5__data_nav_review",
            from_node_id="phase5_website_verification",
            to_node_id="phase5_data_nav_review",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=3,
        )
        insert_edge(
            conn,
            edge_id="edge_phase5__performance",
            from_node_id="phase5_website_verification",
            to_node_id="phase5_performance",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=4,
        )

        insert_edge(
            conn,
            edge_id="edge_phase6__github",
            from_node_id="phase6_deployment",
            to_node_id="phase6_github",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=1,
        )
        insert_edge(
            conn,
            edge_id="edge_phase6__vercel",
            from_node_id="phase6_deployment",
            to_node_id="phase6_vercel",
            rel_type_id="rel_part_of",
            is_trunk=0,
            branch_order=2,
        )

        conn.commit()
        print("Populated knowledge DB:", DB_PATH)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

