# Data Files (XML / CSV)

Data files allow you to load records (views, menus, demo data, configuration) into the database during module installation or upgrade.

## XML (`.xml`)
The most common format. versatile.

```xml
<odoo>
    <data noupdate="1">
        <record id="my_record_id" model="res.partner">
            <field name="name">My Partner</field>
            <field name="company_id" ref="base.main_company"/>
        </record>
    </data>
</odoo>
```

*   **`noupdate="1"`:** The record is created only once. Subsequent upgrades will **not** overwrite user changes.
*   **`ref`:** Reference an external ID (XML ID) from another module.

## CSV (`.csv`)
Best for loading large lists of simple records (e.g., access rights, country list).
**Filename matches model name:** `ir.model.access.csv`.

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,1,1,1
```

## Shortcuts
*   `<menuitem>`: Shortcut for `ir.ui.menu`.
*   `<template>`: Shortcut for `ir.ui.view` (QWeb).
*   `<report>`: Shortcut for `ir.actions.report`.
