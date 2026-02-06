# Using a service

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/services.html

## TL;DR

- Dans un composant OWL, on récupère un service via `useService('name')`.
- Les services standards : rpc, orm, action, notification, dialog, etc. (selon env).

## Exemples

```js
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class X extends Component {
  setup() {
    this.orm = useService("orm");
  }
  async load() {
    const data = await this.orm.searchRead('res.partner', [], ['name']);
    ...
  }
}
```
