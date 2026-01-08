# Concept Package — Deep Research to Website

This folder is a self-contained "concept package" that includes:
- its own SQLite DB (`knowledge/knowledge.db`)
- migrations + rules
- exports (JSON + Mermaid) for LLM consumption
- an agent playbook + CLAUDE controller

It also vendors the original process docs under `reference/template_deep_reserach/`.

## Commands
```bash
# Populate the DB with this concept map
python scripts/populate_knowledge.py

# Lint (must return empty sets)
python scripts/lint_db.py

# Export
python scripts/export_map.py default
```
