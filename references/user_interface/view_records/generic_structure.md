# Generic View Structure

Basic views generally share the common minimal structure defined below.

```xml
<record id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
    <field name="name">NAME</field>
    <field name="model">MODEL</field>
    <field name="arch" type="xml">
        <VIEW_TYPE>
            <views/>
        </VIEW_TYPE>
    </field>
</record>
```

**Key Fields:**
*   `name`: A descriptive name for the view (e.g., `res.partner.view.form`).
*   `model`: The model this view applies to (e.g., `res.partner`).
*   `arch`: The view architecture field, containing the XML definition.

**View Types:**
*   `form`: Single record display/edit.
*   `list` (tree): Multiple records list.
*   `search`: Filters and search options.
*   `kanban`: Card-based visualization.
*   `graph`, `pivot`, `calendar`, `cohort`, `gantt`, `grid`, `map`: Other visualizations.
*   `qweb`: Reporting and Website templates.
