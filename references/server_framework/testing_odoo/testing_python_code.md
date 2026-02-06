# Testing Python code

## TL;DR

- Tests unitaires/integ Python avec classes de test Odoo (TransactionCase/SavepointCase).
- Tester la logique business (models, constraints, workflows) sans UI.

## Patterns recommandés

- Préférer `SavepointCase` quand possible (plus rapide).
- Utiliser des données minimales (factory methods).
- Tester aussi les droits (users avec groupes).

## Exemples

```python
from odoo.tests.common import SavepointCase

class TestX(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.X = cls.env['x.model']

    def test_create(self):
        rec = self.X.create({'name': 'A'})
        self.assertEqual(rec.name, 'A')
```
