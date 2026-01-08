# Agent Knowledge Playbook (Claude/Gemini CLI)

## Objective
Maintain a constrained "river map" in `knowledge/knowledge.db` so it is:
- easy to traverse (trunk + branches)
- chunked (2–3 children recommended; max 4)
- never finalized with exactly 1 child under any node

## Required Workflow
1) Read `map` + `root_node_id`.
2) Add children in chunks (2–3; max 4).
3) Mark trunk edges with `is_trunk = 1` (or use `precedes` relationship consistently).
4) Run lint queries before finalizing (`knowledge/migrations/004_lint_queries.sql` must return empty sets).
5) Export JSON + Mermaid to `knowledge/exports/`.

## Change Requests (Drift-Control Loop)
If the user asks to **change/update** this concept/map, treat it as a change request (not “new content”).

Rules:
- Do **not** append ad-hoc exceptions into `CLAUDE.md` or other controller files.
- Make the change in the **data structures** (nodes/edges/DB) and regenerate exports so the portable JSON/Mermaid stays the source of truth.

Process:
1) Restate the change as acceptance criteria (what must be true after the change).
2) Identify impacted nodes/edges and constraints (max children, depth, no-single-child).
3) Implement via the package’s DB write path (populate script or SQL patch).
4) Lint until clean.
5) Export, then verify the exports reflect the change and the trunk still makes sense.

## Canonical Queries
Root:
```sql
SELECT root_node_id, max_depth, max_children FROM map WHERE id = ?;
```

Children:
```sql
SELECT e.to_node_id, rt.name AS rel, e.is_trunk, e.branch_order
FROM edge e
JOIN rel_type rt ON rt.id = e.rel_type_id
WHERE e.from_node_id = ?
ORDER BY e.is_trunk DESC, e.branch_order ASC;
```

Lint (must be empty):
```sql
SELECT from_node_id, COUNT(*) AS child_count
FROM edge
GROUP BY from_node_id
HAVING child_count = 1;
```
