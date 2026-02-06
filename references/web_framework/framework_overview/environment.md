# Environment

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- L’environnement (`env`) OWL expose les services, la session et les contextes.
- Toujours passer par `env.services` pour accéder aux API du client.

## Quand l’utiliser

- Quand un composant a besoin d’ORM, d’actions, de notifications.
- Pour partager des infos via `env` dans des composants enfants.

## Concepts clés

- `env.services`: accès aux services (`orm`, `rpc`, `action`, `notification`).
- `env.session`: informations de session utilisateur.
- `env.config`: paramètres du client.

## API / Syntaxe

- Injection : `setup()` → `this.env` dans un composant OWL.
- Services : `this.env.services.orm.searchRead(...)`.

## Patterns recommandés

- Centraliser les appels RPC dans un service dédié.
- Utiliser `env` pour éviter les imports circulaires.

## Anti-patterns & pièges

- Stocker des états globaux hors `env`.
- Lire `window` pour obtenir des infos déjà disponibles dans `env`.

## Debug & troubleshooting

- Logguer `Object.keys(env.services)` pour voir les services disponibles.
- Vérifier la présence du service dans le registry.

## Exemples complets

```javascript
// my_module/static/src/js/my_component.js
/** @odoo-module **/

import { Component } from "@odoo/owl";

export class MyComponent extends Component {
    setup() {
        this.orm = this.env.services.orm;
    }

    async loadPartners() {
        return this.orm.searchRead("res.partner", [], ["name"]);
    }
}
```

## Checklist

- [ ] Les services sont injectés via `env`.
- [ ] Les accès session passent par `env.session`.
- [ ] Les appels RPC sont centralisés.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Services](../services/index.md)
- [Hooks](../hooks/index.md)
- [Error handling](../error_handling/index.md)
