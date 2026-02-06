# Odoo UI Icons

Odoo 19 relies primarily on standard icon libraries but also introduces its own set for specific needs.

## FontAwesome 4
The standard library for most icons in Odoo is **FontAwesome 4**.
*   Usage: `<i class="fa fa-user"/>`
*   Reference: [FontAwesome 4.7 Cheatsheet](https://fontawesome.com/v4/icons/)

## Odoo Icons (`oi`)
Odoo includes a custom icon set for strict UI components that require a specific look not found in FontAwesome.
*   Usage: `<i class="oi oi-arrow-right"/>` (Note the `oi` class instead of `fa`).
*   Common icons: `oi-arrows-v`, `oi-checkbox-checked`, `oi-search`, `oi-view-kanban`.

## App Icons
Module icons (displayed in the main dashboard) are typically stored in `static/description/icon.png`. They should be:
*   PNG format.
*   Ideally flat usage of standard Odoo colors.
