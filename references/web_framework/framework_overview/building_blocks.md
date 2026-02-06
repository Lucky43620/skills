# Building blocks

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le client web est composé d’assets, de registries, de services et de composants OWL. 
- Vous assemblez ces briques pour créer vues, actions et widgets. 

## Quand l’utiliser

- Pour comprendre où brancher une extension (service, registry, patch, composant). 
- Pour structurer un module front sans “monkey patch” global. 

## Concepts clés

- `component`: unité UI OWL.
- `service`: logique métier côté client (state, RPC, navigation).
- `registry`: catalogue pour déclarer des extensions.

## API / Syntaxe

- Enregistrement : `registry.category("views").add("my_view", viewDefinition)`.
- Service : `registry.category("services").add("my_service", serviceFactory)`.

## Patterns recommandés

- Créer un composant OWL + template QWeb associé.
- Encapsuler une logique de navigation dans un `service`.

## Anti-patterns & pièges

- Ajouter du JS global dans un bundle sans module `@odoo-module`.
- Accéder à des globals non injectés par l’environnement OWL.

## Debug & troubleshooting

- Inspecter l’environnement OWL (`env`) pour voir les services disponibles.
- Vérifier que la catégorie de registry est correcte (views vs fields vs actions).

## Exemples complets

```javascript
// my_module/static/src/js/my_service.js
/** @odoo-module **/

import { registry } from "@web/core/registry";

const myService = {
    start(env) {
        return {
            hello() {
                env.services.notification.add("Bonjour !");
            },
        };
    },
};

registry.category("services").add("my_service", myService);
```

## Checklist

- [ ] Chaque extension est enregistrée dans le bon registry.
- [ ] Les services sont démarrés via `start`.
- [ ] Les composants ont un template associé.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Services](../services/index.md)
- [Registres](../registries/index.md)
- [Composants OWL](../owl_components/index.md)
- [QWeb templates](../qweb_templates/index.md)
