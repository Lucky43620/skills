# useBus

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/hooks.html

## TL;DR

- Hook pour s’abonner à un bus (EventBus) et nettoyer automatiquement à l’unmount.
- Utile pour écouter events globaux ou de services.

## Patterns recommandés

- Émettre des événements documentés (noms stables) depuis un service.
- Désabonnement automatique via hook plutôt que gestion manuelle.

## Exemples

```js
/** @odoo-module **/
import { useBus } from "@web/core/utils/hooks";

setup() {
  useBus(this.env.bus, "MY_EVENT", (ev) => {
    // handle
  });
}
```
