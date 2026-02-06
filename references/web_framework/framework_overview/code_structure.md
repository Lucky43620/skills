# Code structure

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Les modules front suivent une structure `static/src` pour JS, XML, SCSS.
- Les assets sont déclarés dans `__manifest__.py` par bundle.

## Quand l’utiliser

- Pour organiser un module front Odoo et éviter les imports implicites.
- Pour diagnostiquer un module non chargé.

## Concepts clés

- `static/src/js`: modules JS (`/** @odoo-module **/`).
- `static/src/xml`: templates QWeb/OWL.
- `static/src/scss`: styles du backend.

## API / Syntaxe

- Déclaration d’assets : `"web.assets_backend": [...]`.
- Template OWL : `t-name="my_module.MyComponent"`.

## Patterns recommandés

- Un fichier par composant (`.js` + `.xml` + `.scss`).
- Des chemins explicites dans le manifeste.

## Anti-patterns & pièges

- Mélanger JS backend et website dans le même bundle.
- Oublier d’ajouter un template XML au bundle correspondant.

## Debug & troubleshooting

- Vérifier le bundle dans le mode debug assets.
- Contrôler les imports relatifs avec `@web/` et `@odoo/`.

## Exemples complets

```text
my_module/
  static/src/
    js/my_component.js
    xml/my_component.xml
    scss/my_component.scss
```

```python
# my_module/__manifest__.py
{
    "assets": {
        "web.assets_backend": [
            "my_module/static/src/js/my_component.js",
            "my_module/static/src/xml/my_component.xml",
            "my_module/static/src/scss/my_component.scss",
        ],
    },
}
```

## Checklist

- [ ] `static/src` contient JS, XML, SCSS.
- [ ] Chaque fichier est référencé dans le bon bundle.
- [ ] Les templates OWL sont chargés avant l’usage.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Assets](../assets.md)
- [Modules JavaScript](../javascript_modules.md)
- [Owl components](../owl_components.md)
