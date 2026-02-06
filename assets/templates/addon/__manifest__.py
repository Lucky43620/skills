# Template __manifest__.py (addon minimal)
{
    "name": "My Module",
    "version": "19.0.1.0.0",
    "category": "Custom",
    "summary": "Résumé",
    "depends": ["base", "web"],
    "data": [
        # "security/ir.model.access.csv",
        # "views/my_model_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # "my_module/static/src/**/*",
        ],
    },
    "installable": True,
    "application": False,
}
