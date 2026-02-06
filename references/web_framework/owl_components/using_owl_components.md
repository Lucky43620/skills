# Using Owl components (Odoo)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/owl_components.html

## TL;DR

- Les composants OWL sont la base du webclient : classes + template QWeb, `setup()` pour initialiser.
- L’accès aux services se fait via `useService()` et aux hooks via `@web/core/utils/hooks`.
- On enregistre l’intégration via registries (fields, views, systray, etc.).

## Concepts clés

- Cycle de vie : `setup()`, hooks, état local, props, events.
- Templates : XML dans assets, nommage stable et unique.
- Environment Odoo : `env` (services, config, bus…).

## Patterns recommandés

- Séparer logique (JS) et template (XML), organiser par feature.
- Éviter le state global; préférer services ou store.
- Pour modifications : patcher `setup()` plutôt qu’un constructor.

## Pièges fréquents

- Template non chargé (xml pas dans bundle).
- Utiliser des APIs OWL sans passer par conventions Odoo (services/registries).

## Exemples

```js
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class Hello extends Component {
  setup() {
    this.notification = useService("notification");
  }
  sayHi() {
    this.notification.add("Salut !");
  }
}
Hello.template = "my_addon.Hello";
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">
  <t t-name="my_addon.Hello">
    <button type="button" t-on-click="sayHi">Hello</button>
  </t>
</templates>
```

## Voir aussi

- ../services/using_a_service.md
- ../registries/reference_list.md
- ../hooks/usebus.md
