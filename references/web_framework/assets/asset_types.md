# Asset Types

Odoo manages different types of assets bundles.

## Key Bundles

### `web.assets_backend`
*   **Target:** The main Odoo backend (internal user interface).
*   **Content:** Core framework (Owl, Services, Registry), Views, Widgets.
*   **Usage:** Add your backend JS/SCSS here.

### `web.assets_frontend`
*   **Target:** Public website, portal, e-commerce.
*   **Content:** Website snippets, public-facing logic.
*   **Usage:** Add website-specific styles and scripts here.

### `web.assets_common` (Deprecated/Merged)
*   Historically contained shared libraries (jQuery, Underscore), but v19 mostly includes these in backend/frontend bundles directly.

### `web.report_assets_common` / `web.report_assets_pdf`
*   **Target:** QWeb PDF reports (wkhtmltopdf).
*   **Usage:** CSS for print layouts. **Note:** Advanced JS doesn't work well in PDF generation.

## How to Register
In `__manifest__.py`:
```python
'assets': {
    'web.assets_backend': [
        'my_module/static/src/scss/style.scss',
        'my_module/static/src/js/widget.js',
    ],
}
```
