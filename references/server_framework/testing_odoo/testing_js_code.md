# Testing JS code

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/testing.html

## TL;DR

- Les tests JS valident le comportement du web client (OWL, services, widgets).
- Utiliser la base de tests Odoo (`hoot`) et les helpers dédiés.

## Quand l’utiliser

- Quand vous développez des composants OWL ou services JS.
- Quand une action client complexe doit être testée.

## Concepts clés

- **Tests unitaires JS** : exécutés côté navigateur.
- **Mock server** : simule des réponses RPC.
- **Fixtures** : DOM/registry isolés pour chaque test.

## API / Syntaxe

```javascript
// my_module/static/tests/my_component.test.js
/** @odoo-module **/

import { mount } from "@web/../tests/helpers/utils";
import { makeTestEnv } from "@web/../tests/helpers/mock_env";
import { MyComponent } from "../src/my_component";

test("my component renders", async () => {
  const env = await makeTestEnv();
  const component = await mount(MyComponent, { env });
  expect(component.el.querySelector(".o_my_component")).toBeTruthy();
});
```

## Patterns recommandés

- Utiliser les helpers de test fournis par Odoo.
- Mock des services pour isoler le test.
- Grouper les tests par feature.

## Anti-patterns & pièges

- Tests end-to-end trop lourds pour des cas simples.
- Coupler un test à des données de production.

## Debug & troubleshooting

- Lancer les tests en `?debug=tests`.
- Vérifier que les assets de test sont chargés.

## Exemples complets

```python
# my_module/__manifest__.py
{
    "name": "My Module",
    "assets": {
        "web.assets_tests": [
            "my_module/static/tests/**/*.js",
        ],
    },
}
```

## Checklist

- [ ] Tests JS placés dans `static/tests`.
- [ ] Bundle `web.assets_tests` déclaré.
- [ ] Utilisation des helpers Odoo.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/frontend/javascript_unit_testing.html

## Voir aussi

- [JavaScript unit testing](../../web_framework/javascript_unit_testing/index.md)
- [Testing Odoo (index)](index.md)
- [Mock server notes](../../assets/templates/tests/mock_server_notes.md)
