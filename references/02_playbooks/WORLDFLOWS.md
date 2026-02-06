# Workflows — Recettes reproductibles

Ces workflows donnent un “chemin” standard pour répondre aux demandes.

## 1) Ajouter un nouveau modèle (backend)
1. Créer `models/<model>.py` (inherit `models.Model`)
2. Définir `_name`, fields, `_description`
3. Ajouter accès : `security/ir.model.access.csv`
4. Ajouter views : `views/<model>_views.xml`
5. Ajouter action + menu : `ir.actions.act_window` + `ir.ui.menu`
6. Déclarer fichiers dans `__manifest__.py` (`data`, `depends`)

➡️ Voir : `server_framework/orm_api/models.md`, `server_framework/security_in_odoo/access_rights.md`, `user_interface/view_architectures/form.md`, `server_framework/actions/window_actions_ir_actions_act_window.md`

## 2) Ajouter un composant OWL dans le backend
1. Déclarer assets dans `__manifest__.py` → bundle backend
2. Créer `static/src/...` (js + xml template)
3. Enregistrer dans la bonne registry (fields, views, services, systray…)
4. Écrire composant OWL (`setup()`, hooks, `useService`)
5. Tester avec `?debug=assets`

➡️ Voir : `web_framework/assets/`, `web_framework/owl_components/`, `web_framework/registries/`, `web_framework/services/`

## 3) Créer / modifier un report QWeb PDF
1. Créer template QWeb dans `report/<name>.xml`
2. Déclarer action `ir.actions.report`
3. Option : paperformat + fonts
4. Tester rendu HTML, puis PDF

➡️ Voir : `server_framework/qweb_reports/`

## 4) Sécurité
1. D’abord access rights (modèle)
2. Puis record rules (règles par enregistrements)
3. Puis sécurité champ (groups / field access)
4. Audit “pitfalls” (sudo, rules trop larges)

➡️ Voir : `server_framework/security_in_odoo/`
