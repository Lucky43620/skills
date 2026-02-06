# Introduction

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le framework web Odoo fournit un client JS modulaire (assets, registries, services) pour composer des vues et actions. 
- Basez-vous sur la structure `static/src` et les bundles d’assets pour charger votre code côté client. 

## Quand l’utiliser

- Quand vous devez étendre le client web (vues, widgets, services, actions). 
- Quand vous avez besoin d’un point d’extension stable plutôt que de patcher du core. 

## Concepts clés

- `assets`: bundles déclarés dans le manifeste, chargés par le web client. 
- `registries`: points d’extension (vues, champs, actions, systray, services). 
- `services`: singletons injectés via l’environnement OWL. 

## API / Syntaxe

- Déclarer un module JS : `/** @odoo-module **/`. 
- Ajouter un asset dans `__manifest__.py` via `assets`. 

## Patterns recommandés

- Créer un module dans `my_module/static/src/...` et l’ajouter à `web.assets_backend`. 
- Utiliser un `registry` dédié (ex: `views`, `fields`, `actions`) pour enregistrer des extensions. 

## Anti-patterns & pièges

- Patcher un composant sans justification → privilégier un registry ou un service. 
- Charger du JS via `web.assets_common` si l’usage est strictement back-office. 

## Debug & troubleshooting

- Activer le mode debug pour inspecter les assets et voir les modules chargés. 
- Vérifier l’ordre de chargement des bundles si un module ne s’enregistre pas. 

## Exemples complets

```python
# my_module/__manifest__.py
{
    "name": "My Module",
    "assets": {
        "web.assets_backend": [
            "my_module/static/src/js/my_action.js",
        ],
    },
}
```

```javascript
// my_module/static/src/js/my_action.js
/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("actions").add("my_module.action", (env) => {
    return {
        type: "ir.actions.client",
        tag: "my_module.action",
    };
});
```

## Checklist

- [ ] Le module JS est dans `static/src`.
- [ ] L’asset est déclaré dans le manifeste.
- [ ] L’extension passe par un `registry` ou un `service`.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Structure du code](code_structure.md)
- [Registres](../registries/index.md)
- [Services](../services/index.md)
- [Assets](../assets/index.md)
