# ORM API Overview

The **ORM (Object-Relational Mapping)** is the core of Odoo backend development. It maps Python classes (Models) to PostgreSQL database tables.

## Key Concepts
*   **Models:** Python classes inheriting `odoo.models.Model`. Each class = one table.
*   **Fields:** Attributes of the class (Char, Integer, Many2one). Define columns.
*   **Recordsets:** The primary data structure. Methods usually operate on a *set* of records (self), not just one.
*   **Environment (`self.env`):** Access to DB cursor, current user, context, and other models.

## Basic Usage
```python
# Create
partner = self.env['res.partner'].create({'name': 'John'})

# Search
partners = self.env['res.partner'].search([('is_company', '=', True)])

# Update
partners.write({'active': True})

# Delete
partners.unlink()
```

## Conventions
*   `_name`: Technical name (e.g. `sale.order`).
*   `_description`: User-friendly name.
*   `_order`: Default sorting.
*   `_rec_name`: Field to display in Many2zones (default: `name`).
