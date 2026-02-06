# CSV data files (Data Files)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/data.html

## TL;DR

- CSV utile pour gros volumes de données statiques (ex: pays/états), via import au chargement module.
- Nécessite colonnes/entêtes correspondant aux champs, avec références aux xmlids pour relations.

## Patterns recommandés

- Mettre les CSV dans `data/` et référencer dans manifest.
- Utiliser des xmlids stables pour relations (ex: `base.fr`).

## Pièges fréquents

- Encodage/quoting incorrect → import échoue.
- Références relationnelles introuvables → lignes ignorées/erreurs.

## Exemples

```csv
id,name
x_tag_demo,Demo
```
