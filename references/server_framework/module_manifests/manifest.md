# Manifest (`__manifest__.py`)

## TL;DR
The manifest describes the module to the Odoo server. It dictates dependencies, data loading order, and metadata.
**Critical:** `depends` controls load order. `data` order matters (top to bottom).

## Structure
A Python dictionary available in `__manifest__.py`.

```python
{
    'name': "My Module",
    'version': '1.0',
    'depends': ['base', 'sale'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # Data files to load (order matters!)
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # Application vs Technical
    'application': True,
    'installable': True,
    # License
    'license': 'LGPL-3',
}
```

## Key Keys
*   **name** (`str`): Module title.
*   **version** (`str`): Semantic versioning (e.g., `1.0`).
*   **depends** (`list`): List of module technical names. Odoo ensures these are loaded *before* your module.
*   **data** (`list`): Path to XML/CSV files relative to module root.
*   **demo** (`list`): Data loaded only if "Load Demo Data" is checked.
*   **assets** (`dict`): Bundle definitions (JS/CSS). **New in v15+**.
    ```python
    'assets': {
        'web.assets_backend': [
            'my_module/static/src/**/*',
        ],
    }
    ```
*   **license** (`str`): `LGPL-3`, `OEEL-1`, etc.

## Pitfalls
*   **Order Dependency:** If View B inherits from View A, the file containing View A *must* be loaded first in `data` (or in a module in `depends`).
*   **Comma Errors:** It's a Python dict. Missing commas cause Syntax Errors prevents server start.
*   **Cache:** Changes to manifest (like adding a file to `data`) require a server restart + module upgrade.
