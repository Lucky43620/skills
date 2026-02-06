# Testing Framework (JS Unit Testing)

## TL;DR

- Tests unitaires JS pour valider composants/services sans passer par l’UI complète.
- En Odoo, les tests JS s’intègrent avec l’infrastructure de test frontend (selon doc v19).

## Patterns recommandés

- Tester les services de façon isolée (mock env).
- Tester les composants OWL avec des helpers de mount.

## Pièges fréquents

- Tests fragiles dépendants du DOM complet / timing.

## Exemples

```js
/** @odoo-module **/
// Exemple pseudo : adapter au framework de test Odoo v19
import { expect, test } from "@odoo/hoot";

test("my test", async () => {
  expect(true).toBe(true);
});
```
