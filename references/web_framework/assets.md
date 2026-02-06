# Assets Management (Odoo v19)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

La gestion des assets (JS, CSS, XML/Templates) se fait entièrement via le fichier `__manifest__.py`.

## Bundles Principaux

| Bundle | Usage |
| :--- | :--- |
| **`web.assets_backend`** | Le plus utilisé. Chargé pour tout utilisateur connecté au backend (l'interface Odoo). Contient Owl, le webclient, les vues. |
| **`web.assets_frontend`** | Chargé sur le site web public (eCommerce, Portail). **Attention :** Owl n'est pas toujours entièrement disponible ou chargé différemment ici. |
| **`web.assets_common`** | (Déprécié/Rare) Bases communes. Évitez d'y toucher sauf nécessité absolue. |
| **`web.report_assets_common`** | Chargé dans les rapports PDF/HTML (QWeb Reports). |

## Déclaration dans `__manifest__.py`

```python
'assets': {
    'web.assets_backend': [
        # Inclure des fichiers JS/CSS/SCSS
        'my_module/static/src/scss/styles.scss',
        'my_module/static/src/js/component.js',
        'my_module/static/src/xml/component.xml',
        
        # Supprimer un fichier (cas d'héritage/remplacement)
        ('remove', 'other_module/static/src/main.js'),
        
        # Inclusion conditionnelle (rare)
        ('include', 'web.assets_api_request'),
    ],
    'web.assets_frontend': [
        'my_module/static/src/frontend.js',
    ],
},
```

## Règles Importantes (v19)

1. **Pas de `<script>` ou `<link>`** dans les vues XML (sauf cas très spécifiques). Tout passe par le manifest.
2. **Ordre de chargement** : Odoo respecte l'ordre de la liste. Si B dépend de A, placez A avant B.
3. **Lazy Loading** : Les assets backend sont chargés en bloc SPA (Single Page App).
4. **SCSS** : Odoo compile le SCSS (Sass). Vous avez accès aux variables Bootstrap et Odoo (`$o-brand-primary`, etc.).

## Debug Assets

Pour voir les fichiers non minifiés et débuguer le JS :
Ajoutez `?debug=assets` dans l'URL.
Exemple : `http://localhost:8069/web?debug=assets`
