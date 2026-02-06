# Bus

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le bus permet des notifications temps réel (chatter, updates).
- Utilisez le service bus plutôt qu’un polling maison.

## Quand l’utiliser

- Pour réagir à des événements serveur (notifications).
- Pour synchroniser des vues en temps réel.

## Concepts clés

- `bus_service`: service côté client pour s’abonner aux canaux.
- Canaux typiques : base sur `db`, `uid`, `channel`.

## API / Syntaxe

- Souscription via service (`env.services.bus_service`).
- Handler : fonction appelée à la réception.

## Patterns recommandés

- Centraliser la souscription dans un service.
- Nettoyer les handlers lors du `destroy` du composant.

## Anti-patterns & pièges

- S’abonner dans chaque composant sans cleanup.
- Utiliser le bus pour des données volumineuses.

## Debug & troubleshooting

- Vérifier que les canaux sont bien enregistrés.
- Logger les payloads reçus.

## Exemples complets

```javascript
// my_module/static/src/js/bus_subscriber.js
/** @odoo-module **/

import { registry } from "@web/core/registry";

const busSubscriber = {
    start(env) {
        const bus = env.services.bus_service;
        bus.addChannel("my_module_channel");
        bus.onNotification((notifications) => {
            for (const { payload } of notifications) {
                env.services.notification.add(payload.message);
            }
        });
        return {};
    },
};

registry.category("services").add("my_module_bus", busSubscriber);
```

## Checklist

- [ ] Canaux explicitement déclarés.
- [ ] Handlers nettoyés si nécessaire.
- [ ] Pas d’abus pour des payloads lourds.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Services](../services/index.md)
- [Hooks](../hooks/index.md)
- [Error handling](../error_handling/index.md)
