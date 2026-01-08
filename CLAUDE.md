# CLAUDE.md — Deep Research → Website (Concept River Map)

## Objective
Maintain a constrained "river map" for the **Deep Research → Website** system in `knowledge/knowledge.db`, then export JSON + Mermaid.

## Hard Rules
- Max children per node: 4 (DB enforces)
- Recommended children per node: 2–3
- No-single-child rule: every node must have 0 children OR >=2 children (lint must be clean)
- Max depth: 5 (design goal; use depth_hint if helpful)

## Files
- DB: `knowledge/knowledge.db`
- Migrations: `knowledge/migrations/`
- Lint: `knowledge/migrations/004_lint_queries.sql`
- Agent guidance: `prompts/agent_knowledge_playbook.md`
- Export: `scripts/export_map.py`
- Populate: `scripts/populate_knowledge.py`
- Source workflow docs: `reference/template_deep_reserach/`

## Process (must follow)
1) Keep the trunk as the 0→6 phases (classification → deployment) using `rel_precedes` edges and `is_trunk=1`.
2) Ensure every phase node has at least one additional (non-trunk) child, so it never has exactly 1 outgoing edge.
3) Prefer leaf detail nodes (0 children) unless you can add 2–3 children at once.
4) Update the DB via `python scripts/populate_knowledge.py`, then `python scripts/lint_db.py`, then export.

## Change Requests (No Drift)
When the user asks for changes/updates:
1) Restate the request as acceptance criteria.
2) Update the durable sources of truth (usually `scripts/populate_knowledge.py` and/or `reference/`).
3) Regenerate and verify:
   - `python scripts/populate_knowledge.py`
   - `python scripts/lint_db.py` (must pass)
   - `python scripts/export_map.py default`
4) Verify the exports reflect the change (prevents drift/context loss).

## DB write conventions
- map_id: "default"
- rel_type_id must be one of:
  - rel_precedes, rel_is_a, rel_part_of, rel_causes, rel_related

## Commands
```bash
python scripts/populate_knowledge.py
python scripts/lint_db.py
python scripts/export_map.py default
```
