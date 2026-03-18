# Build Plan: Structured System Documentation

## Overview
Create a professional documentation folder `docs/` with subcategories for DevOps, Technical Architecture, and Business Processes.

## Project Type
WEB (Django-based project)

## Success Criteria
- [ ] Structured `docs/` folder exists.
- [ ] All 7 core Markdown files created.
- [ ] Technical guide explains both Django and Antigravity Kit.
- [ ] User guide covers all main "clinic" features.

## Tech Stack
- Markdown
- Mermaid.js (for diagrams)

## File Structure
- `docs/`
  - `README.md`
  - `devops/`
    - `setup.md`
    - `deployment.md`
  - `technical/`
    - `architecture.md`
    - `database.md`
  - `business/`
    - `user-guide.md`
    - `processes.md`

## Task Breakdown

| Task ID | Name | Agent | Skills | Priority | Dependencies | INPUT→OUTPUT→VERIFY |
|---------|------|-------|--------|----------|--------------|----------------------|
| T1 | Folder Setup | `orchestrator` | `bash-linux` | P0 | None | Root folder → `docs/` subfolders → List folders |
| T2 | DevOps Docs | `devops-engineer` | `deployment-procedures` | P1 | T1 | Docker/Railway info → `setup.md`, `deployment.md` → Read content |
| T3 | Architecture Docs | `backend-specialist` | `architecture` | P1 | T1 | Django structure → `architecture.md` → Read content |
| T4 | Database Docs | `database-architect` | `database-design` | P1 | T1 | `clinic/models/` → `database.md` → Read content |
| T5 | User Guide | `documentation-writer` | `documentation-templates` | P1 | T1 | `clinic/templates/` & logic → `user-guide.md` → Read content |
| T6 | Business Processes | `documentation-writer` | `documentation-templates` | P1 | T5 | Views & Business logic → `processes.md` → Read content |
| T7 | Main Index | `documentation-writer` | `documentation-templates` | P1 | T2, T3, T4, T5, T6 | Subfiles list → `docs/README.md` → Verify all links |

## Phase X: Verification
- [ ] `python .agent/scripts/checklist.py .`
- [ ] Check links manually.
- [ ] Verify tone consistency (Professional & Helpful).
