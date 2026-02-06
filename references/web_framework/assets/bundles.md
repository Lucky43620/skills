# Bundles

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html#bundles

## TL;DR

Les assets sont groupés en **bundles** déclarés dans le `__manifest__.py`.
Supporte les globs (`**/*`) et différentes opérations (`append`, `prepend`, `before`, `after`, `remove`, `replace`, `include`).

## Bundles Standards

| Bundle | Contenu / Usage |
| :--- | :--- |
| `web.assets_common` | Socle commun (WebClient + Website + PoS). Contient `boot.js`. |
| `web.assets_backend` | Spécifique au WebClient (Views, Action Manager). |
| `web.assets_frontend` | Spécifique au Website public (eCommerce, Portail). |
| `web.assets_unit_tests` | Tests JS, mocks et helpers. |

## Déclaration (`__manifest__.py`)

```python
'assets': {
    'web.assets_backend': [
        'my_addon/static/src/scss/style.scss',
        'my_addon/static/src/js/**/*',
    ],
},
```

## Opérations

Par défaut, une chaîne de caractères est un `append` à la fin.
Pour plus de contrôle, utilisez des tuples :

- `('prepend', 'path')` : Ajoute au début.
- `('before', 'target', 'path')` : Insère `path` juste avant `target`.
- `('after', 'target', 'path')` : Insère `path` juste après `target`.
- `('remove', 'target')` : Supprime le fichier `target` du bundle (si ajouté par un autre module).
- `('replace', 'target', 'path')` : Remplace `target` par `path`.
- `('include', 'bundle_name')` : Inclut tout un autre bundle (sous-bundle).

**Exemple "Remove" :**
```python
'web.assets_common': [
    ('remove', 'web/static/src/js/boot.js'),
],
```

## Ordre de Chargement

1. Liste vide générée.
2. `ir.asset` (sequence < 16) appliqués.
3. Assets des manifestes (dans l'ordre des dépendances de modules).
    * *Note : Si un fichier est déjà présent, une directive d'ajout (append) ne fait rien (unicité).*
4. `ir.asset` (sequence >= 16) appliqués.
