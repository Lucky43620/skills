---
name: developing-odoo-v19
description: Skill encyclopédique Odoo v19 (développement). Couvre Server framework (ORM, data files, actions, reports, manifests, sécurité, perf, tests, controllers, mixins), Web framework (assets, modules JS, OWL, registries, services, hooks, patching, erreurs, QWeb frontend, unit tests), UI (vues, SCSS, icônes), modules standards (compta/paiement), CLI, upgrades, APIs externes (JSON-2, RPC, Extract).
---

# Odoo v19 — Developer Reference Skill (niveau “encyclopédie”)

## Objectif
Aider à **concevoir, coder, déboguer et maintenir** des développements Odoo v19, en suivant une structure proche de la documentation officielle (*Developer → Reference*).

> Point d’entrée : `references/00_reference_map.md`  
> Router rapide : `references/01_router_keywords.md`

## Quand utiliser ce skill
Utilise ce skill dès que la demande contient :
- Odoo **v19**
- backend : ORM, modèles, champs, contraintes, actions, data XML/CSV, rapports QWeb, contrôleurs, sécurité, tests
- frontend : assets, modules JS, OWL, registries, services, hooks, patching, erreurs, QWeb templates, tests JS
- UI : views (form/list/kanban/search/graph/pivot/…), héritage, SCSS, icons
- CLI / upgrades / API externes

## Promesse de qualité (règles)
1) **Toujours** rappeler le contexte : *Odoo v19* + backend/web/ui + Community/Enterprise si connu.
2) **Toujours** donner des **chemins de fichiers** concrets (structure de module) + snippets complets.
3) **Toujours** signaler les **pièges** et le **plan de test** (au minimum: scénario + debug=assets si JS).
4) **Toujours** appliquer les patterns Odoo (recordset multi, `ensure_one()`, services/registries, héritage par `xpath`).
5) Si ambigu, proposer **2 approches** (simple vs robuste) avec trade-offs.

## Routage (comment choisir la bonne référence)
- Ouvre `references/01_router_keywords.md` → trouve la section → utilise les fichiers de la rubrique.
- Si le besoin mélange backend + frontend, commence par **backend** (données + sécurité), puis UI, puis JS/Owl.

## Format de réponse recommandé
- **Résumé** (1-3 phrases)
- **Fichiers à créer/modifier** (liste avec chemins)
- **Code** (Python/XML/JS séparés)
- **Notes & pièges**
- **Tests / Debug**

## Bundles inclus (à réutiliser)
- Templates backend : `assets/templates/server/`
- Templates web : `assets/templates/web/`
- Template addon minimal : `assets/templates/addon/`

## Index
- La carte complète : `references/00_reference_map.md`
- Playbooks : `references/02_playbooks/`
