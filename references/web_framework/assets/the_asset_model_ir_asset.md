# The Asset Model (`ir.asset`)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html#the-asset-model-ir-asset

## TL;DR

Modèle `ir.asset` permettant de déclarer des assets **dynamiquement** en base de données (ou via XML `data` records) plutôt que dans le `__manifest__.py`.

## Champs Clés

- `name`: Nom (identification).
- `bundle`: Bundle cible (ex: `web.assets_frontend`).
- `path`: Chemin (relatif, glob, URL) ou bundle name (si include).
- `directive`: `append`, `prepend`, `before`, `after`, `remove`, `replace`, `include`.
- `target`: Fichier cible (pour `before`, `after`, `replace`, `remove`).
- `active`: Active/Désactive l'asset.
- `sequence`: Ordre de chargement (Défaut 16).
    - `< 16` : Appliqué **avant** les manifestes.
    - `>= 16` : Appliqué **après** les manifestes.

## Cas d'usage
Principalement pour le **Website**, pour activer/désactiver des fichiers CSS/JS conditionnellement (ex: options de thème activables par l'utilisateur).

## Déclaration XML
Préférez la syntaxe raccourcie `<asset>` si disponible, sinon `<record model="ir.asset">`.

```xml
<record id="my_asset" model="ir.asset">
    <field name="name">My Custom Asset</field>
    <field name="bundle">web.assets_frontend</field>
    <field name="path">my_module/static/src/js/custom.js</field>
    <field name="sequence">10</field>
</record>
```
