# Router — Mots-clés → Fichier de référence

Objectif : aider l’agent à choisir **rapidement** la bonne page du skill.

## Server framework (backend)
- **model, fields, recordset, @api, compute, constraint** → `server_framework/orm_api/`
- **XML data, noupdate, ir.model.data, <record>, <function>, csv** → `server_framework/data_files/`
- **ir.actions.\***, act_window, server action, cron → `server_framework/actions/`
- **report, qweb report, paperformat, wkhtmltopdf** → `server_framework/qweb_reports/`
- **__manifest__.py, depends, data, assets** → `server_framework/module_manifests/`
- **ir.model.access.csv, record rules, groups, sudo** → `server_framework/security_in_odoo/`
- **profiling, perf, prefetch, cache, SQL** → `server_framework/performance/`
- **SavepointCase, HttpCase, JS tests** → `server_framework/testing_odoo/`
- **http.route, controller, jsonrpc** → `server_framework/web_controllers/`
- **mail.thread, website mixin** → `server_framework/mixins_useful_classes/`

## Web framework (frontend)
- **assets, bundles, web.assets_backend, debug=assets/tests** → `web_framework/assets/`
- **@odoo-module, module system, imports, registries** → `web_framework/javascript_modules/` et `web_framework/registries/`
- **Owl component, hooks, env, useService** → `web_framework/owl_components/`, `web_framework/hooks/`, `web_framework/services/`
- **patch, monkey patch, override, extend** → `web_framework/patching_code/`
- **qweb templates (frontend), t-if, t-foreach** → `web_framework/qweb_templates/`
- **JS errors, error boundaries** → `web_framework/error_handling/`
- **unit tests JS** → `web_framework/javascript_unit_testing/`

## UI (views)
- **architecture XML (form/tree/kanban/search/graph/pivot…)** → `user_interface/view_architectures/`
- **view records, inheritance, xpath** → `user_interface/view_records/`
- **scss, !default, inheritance** → `user_interface/scss_inheritance/`
- **icons** → `user_interface/ui_icons/`

## CLI / Upgrades / APIs externes
- **odoo-bin, scaffold, db dump/load, module install** → `cli/`
- **upgrade scripts/utils** → `upgrades/`
- **/json/2, json2, external api** → `external_apis/external_json2_api/`
- **XML-RPC / JSON-RPC** → `external_apis/external_rpc_api/`
- **Extract API** → `external_apis/extract_api/`
