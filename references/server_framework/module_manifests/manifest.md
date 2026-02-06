# Manifest (__manifest__.py)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/module.html

## TL;DR

- Le fichier `__manifest__.py` décrit un module (métadonnées, dépendances, données, assets).
- Il contrôle l’installation, les dépendances et le chargement des données.

## Quand l’utiliser

- À la création ou mise à jour d’un module.
- Pour ajouter des assets, des données XML/CSV ou des dépendances.

## Concepts clés

- **`depends`** : modules requis.
- **`data`/`demo`** : fichiers chargés par Odoo.
- **`assets`** : bundles JS/SCSS/QWeb.
- **`installable`** : activation du module.

## API / Syntaxe

```python
# my_module/__manifest__.py
{
    "name": "My Module",
    "version": "1.0",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/my_model_views.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "my_module/static/src/js/my_widget.js",
        ],
        "web.assets_qweb": [
            "my_module/static/src/xml/my_widget.xml",
        ],
    },
    "installable": True,
}
```

## Patterns recommandés

- Séparer `data/` et `demo/`.
- Déclarer les assets par bundle (backend/frontend/tests).
- Garder `depends` minimal et explicite.

## Anti-patterns & pièges

- Oublier un fichier `data` → vues non chargées.
- Dépendances implicites via des imports Python.

## Debug & troubleshooting

- Vérifier les logs au démarrage pour les fichiers manquants.
- Contrôler l’ordre de chargement si un `xmlid` est introuvable.

## Exemples complets

```text
my_module/
  __manifest__.py
  models/
  views/
  security/
  static/src/
```

## Checklist

- [ ] `depends` complet et minimal.
- [ ] `data`/`demo` correctement déclarés.
- [ ] Assets ajoutés au bon bundle.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/module.html

## Voir aussi

- [Module manifests (index)](index.md)
- [Assets](../../web_framework/assets/index.md)
- [Data files](../data_files/index.md)
- [Security](../security_in_odoo/index.md)
