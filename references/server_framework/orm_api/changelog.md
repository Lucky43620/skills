# Changelog (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Cette page sert de repère pour suivre les évolutions de l’ORM entre versions.
- Lors d’un upgrade, vérifier les signatures de méthodes, champs dépréciés et comportements de `compute`/`inverse`.

## Quand l’utiliser

- Pendant une migration vers Odoo 19.
- Quand une méthode ORM se comporte différemment après upgrade.

## Concepts clés

- **Compatibilité** : certaines API changent, d’où l’importance de relire les notes de version.
- **Dépréciations** : méthodes ou arguments retirés progressivement.

## API / Syntaxe

- Vérifier les signatures et usages dans les modèles :
```python
# Exemple générique : vérifier l’appel des méthodes ORM
records = self.env["res.partner"].search([])
```

## Patterns recommandés

- Rejouer les tests ORM après upgrade (`TransactionCase`).
- Comparer les méthodes critiques (`create`, `write`, `unlink`, `read`) avec la doc.

## Anti-patterns & pièges

- Supposer que des comportements implicites restent stables.
- Ignorer les warnings de dépréciation dans les logs.

## Debug & troubleshooting

- Activer les logs de `odoo` en debug pour voir les warnings.
- Isoler un cas minimal si un comportement ORM change.

## Exemples complets

```python
# my_module/tests/test_partner.py
from odoo.tests.common import TransactionCase

class TestPartner(TransactionCase):
    def test_create_partner(self):
        partner = self.env["res.partner"].create({"name": "Demo"})
        self.assertTrue(partner.id)
```

## Checklist

- [ ] Repasser sur les notes de version Odoo 19.
- [ ] Relire les méthodes ORM utilisées dans le module.
- [ ] Exécuter les tests ORM.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html
- https://www.odoo.com/documentation/19.0/developer/reference.html

## Voir aussi

- [Models](models.md)
- [Fields](fields.md)
- [Common ORM methods](common_orm_methods.md)
- [Testing Odoo](../testing_odoo/index.md)
