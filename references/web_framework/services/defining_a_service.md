# Defining a service

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/services.html

## TL;DR

- Un service encapsule un comportement partagé (notifications, rpc, action, etc.).
- Déclaration via registry category `services` avec un `start(env)`.

## Concepts clés

- `start(env)` retourne l’API du service.
- Les services peuvent dépendre d’autres services (via env).

## Patterns recommandés

- Garder l’API du service petite et testable.
- Éviter le state global hors service.

## Exemples

```js
/** @odoo-module **/
import { registry } from "@web/core/registry";

export const myService = {
  start(env) {
    return {
      ping: () => env.services.notification.add("pong"),
    };
  },
};

registry.category("services").add("myService", myService);
```
