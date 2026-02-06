# Python interpreter

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Certaines expressions front réutilisent la syntaxe Python (ex: domaines).
- Comprendre les opérateurs et littéraux aide à écrire des filtres lisibles.

## Quand l’utiliser

- Pour exprimer des domaines ou contextes complexes côté client.
- Pour diagnostiquer une expression évaluée côté serveur.

## Concepts clés

- Les expressions suivent les conventions Python (`True`, `False`, `None`).
- Les listes/tuples sont utilisés pour les domaines.

## API / Syntaxe

- Exemple : `[('field', '=', True)]`.
- Opérateurs logiques avec `"|"`, `"&"`, `"!"` en domaine.

## Patterns recommandés

- Préférer des helpers JS qui produisent des structures de domaine.
- Documenter les expressions avec des commentaires.

## Anti-patterns & pièges

- Mélanger des booléens JS (`true/false`) et Python (`True/False`).
- Générer des expressions via concaténation de strings.

## Debug & troubleshooting

- Vérifier la syntaxe dans le shell Odoo.
- Utiliser des domaines simples puis enrichir progressivement.

## Exemples complets

```javascript
// my_module/static/src/js/domain_helpers.js
/** @odoo-module **/

export const activeDomain = [["active", "=", true]];
```

## Checklist

- [ ] Les booléens sont cohérents.
- [ ] Les domaines sont des listes.
- [ ] Les valeurs sont typées correctement.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Domains](domains.md)
- [Context](context.md)
- [ORM API](../../server_framework/orm_api.md)
