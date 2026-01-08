PRAGMA foreign_keys = ON;

CREATE TRIGGER IF NOT EXISTS enforce_max_children
BEFORE INSERT ON edge
BEGIN
  SELECT CASE
    WHEN (
      (SELECT COUNT(*) FROM edge WHERE from_node_id = NEW.from_node_id)
      >= (SELECT max_children FROM map WHERE id = NEW.map_id)
    )
    THEN RAISE(ABORT, 'max_children exceeded for from_node_id')
  END;
END;

CREATE TRIGGER IF NOT EXISTS node_updated_at
AFTER UPDATE ON node
BEGIN
  UPDATE node SET updated_at = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS edge_updated_at
AFTER UPDATE ON edge
BEGIN
  UPDATE edge SET updated_at = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS map_updated_at
AFTER UPDATE ON map
BEGIN
  UPDATE map SET updated_at = datetime('now') WHERE id = NEW.id;
END;
