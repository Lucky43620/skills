# Patching a component

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/patching_code.html

## TL;DR

- Cas fréquent : ajouter un comportement ou un handler à un composant existant.
- Toujours préserver l’appel à `super.setup()` ou logique originale quand applicable.

## Exemples

```js
/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { SomeComponent } from "@web/...";

patch(SomeComponent.prototype, "my_addon.patch", {
  setup() {
    this._super(...arguments);
    // custom init
  },
});
```
