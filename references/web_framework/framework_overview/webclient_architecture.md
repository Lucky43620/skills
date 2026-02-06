# Webclient architecture

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le web client orchestre les actions, vues et services.
- Les `registries` sont les points d’extension principaux.

## Quand l’utiliser

- Pour comprendre comment une action déclenche une vue.
- Pour savoir où brancher un nouveau `client action`.

## Concepts clés

- `web client`: conteneur principal du backend web.
- `action manager`: exécute les `ir.actions.*`.
- `view manager`: rend les vues selon les modèles.

## API / Syntaxe

- Les actions clientes sont enregistrées dans `registry.category("actions")`.
- Les vues s’enregistrent dans `registry.category("views")`.

## Patterns recommandés

- Créer une action cliente dédiée plutôt qu’un patch global.
- Réutiliser les services `action`, `orm`, `notification`.

## Anti-patterns & pièges

- Injecter des dépendances hors `env.services`.
- Remplacer une vue core sans fallback.

## Debug & troubleshooting

- Utiliser le mode debug pour inspecter les actions exécutées.
- Logger la résolution de registry pour valider l’extension.

## Exemples complets

```javascript
// my_module/static/src/js/my_client_action.js
/** @odoo-module **/

import { registry } from "@web/core/registry";

const MyAction = (env) => ({
    type: "ir.actions.client",
    tag: "my_module.client_action",
});

registry.category("actions").add("my_module.client_action", MyAction);
```

## Checklist

- [ ] L’action cliente est enregistrée dans `actions`.
- [ ] Le tag est unique.
- [ ] La vue associée est déclarée si nécessaire.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Actions JS](../javascript_reference/client_actions.md)
- [Registres](../registries.md)
- [Services](../services.md)
