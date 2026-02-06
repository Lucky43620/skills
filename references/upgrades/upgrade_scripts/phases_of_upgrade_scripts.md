# Phases of Upgrade Scripts

When migrating databases (e.g. via Odoo.sh or OpenUpgrade), scripts run in a specific order.

## 1. Pre-Migration (`pre-*.py`)
Runs **before** modules are loaded.
*   **Use case:** Rename tables/columns to preserve data before Odoo's schema synchronization drops them.
*   **Example:** Rename `account_invoice` to `account_move` to prepare for a merge.

```python
def migrate(cr, version):
    cr.execute('ALTER TABLE old_table RENAME TO new_table')
```

## 2. Schema Synchronization (Odoo Core)
Odoo loads models, compares to DB, creates new columns, updates types. **Data in dropped columns is lost here if not saved in Pre-Migration.**

## 3. Post-Migration (`post-*.py`)
Runs **after** modules are loaded.
*   **Use case:** Data transformation, recomputing fields, setting defaults for new columns.
*   **Example:** Copy data from the old renamed column to the new column.

```python
def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for record in env['my.model'].search([]):
        record.new_field = record.old_field_backup
```
