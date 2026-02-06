# Domains

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Les domaines filtrent les enregistrements côté serveur.
- Côté JS, ils se manipulent en liste de tuples.

## Quand l’utiliser

- Pour filtrer une vue ou un searchRead.
- Pour construire un filtre dynamique côté client.

## Concepts clés

- Un domaine est une liste de conditions (`["field", "operator", value]`).
- Vous pouvez combiner avec des opérateurs logiques (`"|"`, `"&"`, `"!"`).

## API / Syntaxe

- Exemple simple : `[["is_company", "=", true]]`.
- ORM JS : `orm.searchRead(model, domain, fields)`.

## Patterns recommandés

- Factoriser des domaines communs dans des helpers.
- Utiliser des opérateurs logiques explicites pour la lisibilité.

## Anti-patterns & pièges

- Construire un domaine en concaténant des strings.
- Mélanger des types (dates vs strings).

## Debug & troubleshooting

- Logger le domaine final avant un appel ORM.
- Tester le domaine dans un filtre de vue.

## Exemples complets

```javascript
// my_module/static/src/js/domain_helpers.js
/** @odoo-module **/

export function activeCompaniesDomain() {
    return ["&", ["is_company", "=", true], ["active", "=", true]];
}
```

```javascript
// usage
const partners = await this.env.services.orm.searchRead(
    "res.partner",
    activeCompaniesDomain(),
    ["name", "vat"]
);
```

## Checklist

- [ ] Les domaines sont des listes, pas des strings.
- [ ] Les opérateurs logiques sont explicites.
- [ ] Les types de valeurs sont cohérents.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [ORM API](../../server_framework/orm_api.md)
- [Services](../services.md)
- [QWeb templates](../qweb_templates.md)
