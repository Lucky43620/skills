# Snippet — Déclarer des assets dans __manifest__.py (Odoo v19)

```python
{
  "name": "My Addon",
  "assets": {
    "web.assets_backend": [
      "my_addon/static/src/**/*.js",
      "my_addon/static/src/**/*.xml",
      "my_addon/static/src/**/*.scss",
    ],
  },
}
```

Notes:
- Mettre l’entête `/** @odoo-module **/` dans les fichiers JS concernés.
- Tester avec `?debug=assets`.
