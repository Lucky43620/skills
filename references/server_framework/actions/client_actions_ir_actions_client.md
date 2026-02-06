# Client Actions (ir.actions.client)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## TL;DR

- Une `client action` déclenche une logique côté web client (JS) via un `tag`.
- Elle est utile pour lancer des écrans custom OWL ou des flux UI spécifiques.

## Quand l’utiliser

- Pour afficher un écran custom qui ne correspond pas à une vue standard.
- Pour intégrer un tableau de bord JS, un wizard OWL ou une expérience dédiée.

## Concepts clés

- **`tag`** : identifiant utilisé côté JS pour résoudre l’action dans un `registry`.
- **`params`/`context`** : données passées à l’action pour initialiser l’UI.
- **Registry actions** : côté JS, l’action est déclarée via `registry.category("actions")`.

## API / Syntaxe

```xml
<!-- my_module/views/actions.xml -->
<record id="action_my_client" model="ir.actions.client">
  <field name="name">Dashboard</field>
  <field name="tag">my_module.dashboard</field>
  <field name="params">{"default_period": "month"}</field>
</record>
```

```javascript
// my_module/static/src/js/dashboard_action.js
/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class DashboardAction extends Component {}
DashboardAction.template = "my_module.Dashboard";

registry.category("actions").add("my_module.dashboard", DashboardAction);
```

## Patterns recommandés

- Définir un composant OWL dédié avec un template QWeb.
- Passer les options via `params` et `context`, pas via globals.
- Déclarer les assets JS/XML dans `web.assets_backend` et `web.assets_qweb`.

## Anti-patterns & pièges

- `tag` manquant ou mal orthographié → action introuvable.
- Oublier d’ajouter le template QWeb dans `web.assets_qweb`.

## Debug & troubleshooting

- Tester en `?debug=assets` pour voir si le module JS est chargé.
- Vérifier la présence de l’action dans la base (menu/action).

## Exemples complets

```python
# my_module/__manifest__.py
{
    "name": "My Module",
    "assets": {
        "web.assets_backend": [
            "my_module/static/src/js/dashboard_action.js",
        ],
        "web.assets_qweb": [
            "my_module/static/src/xml/dashboard_action.xml",
        ],
    },
    "data": [
        "views/actions.xml",
    ],
}
```

```xml
<!-- my_module/static/src/xml/dashboard_action.xml -->
<t t-name="my_module.Dashboard" owl="1">
  <div class="o_my_dashboard">Dashboard</div>
</t>
```

## Checklist

- [ ] `ir.actions.client` possède un `tag` unique.
- [ ] Le module JS est déclaré dans `web.assets_backend`.
- [ ] Le template QWeb est dans `web.assets_qweb`.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## Voir aussi

- [Actions (index)](index.md)
- [JS client actions](../../web_framework/javascript_reference/client_actions.md)
- [Assets](../../web_framework/assets/index.md)
- [Owl components](../../web_framework/owl_components/index.md)
