-- Lint queries (run these before committing / exporting)

-- No-single-child rule violations (exactly 1 child):
SELECT from_node_id, COUNT(*) AS child_count
FROM edge
GROUP BY from_node_id
HAVING child_count = 1;

-- Depth violations (if you populate depth_hint):
SELECT e.id, e.from_node_id, e.to_node_id, e.depth_hint, m.max_depth
FROM edge e
JOIN map m ON m.id = e.map_id
WHERE e.depth_hint IS NOT NULL AND e.depth_hint > m.max_depth;

-- Duplicate sibling order (optional):
SELECT map_id, from_node_id, branch_order, COUNT(*) AS n
FROM edge
WHERE branch_order IS NOT NULL
GROUP BY map_id, from_node_id, branch_order
HAVING n > 1;
