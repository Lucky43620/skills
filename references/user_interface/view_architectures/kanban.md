# Kanban View Architecture

Kanban views display records as "cards", useful for workflow visualization or simple catalogs.

The root element is `<kanban>`.

```xml
<kanban>
    <templates>
        ...
    </templates>
</kanban>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `default_group_by` | Field to group by default. | `''` |
| `default_order` | Order of records. | `''` |
| `class` | CSS class for the root element. | `''` |
| `group_create` | Allow adding new columns (groups). | `True` |
| `group_delete` | Allow deleting columns. | `True` |
| `group_edit` | Allow editing columns. | `True` |
| `records_draggable` | Allow dragging records between columns. | `True` |
| `quick_create` | Enable quick creation (inline) in columns. | `True` |
| `highlight_color` | Field name (integer) for the left-border color of the card. | `''` |
| `examples` | Load predefined column examples (registry key). | `''` |
| `sample_message` | Message to show when empty. | `''` |
| `limit` | Records per page/column. | `40` |

## Templates

Kanban views use **QWeb** templates to define the card structure. The main template is `card`.

```xml
<templates>
    <t t-name="card">
        <div class="oe_kanban_global_click">
            <field name="name"/>
            ...
        </div>
    </t>
    
    <!-- Optional Menu Template -->
    <t t-name="menu">
        <a role="menuitem" type="edit" class="dropdown-item">Edit</a>
        <a role="menuitem" type="delete" class="dropdown-item">Delete</a>
        <ul class="oe_kanban_colorpicker" data-field="color"/>
    </t>
</templates>
```

### `<field>` inside Templates

Used to render field values.

**Attributes:**
*   `name`: Field name.
*   `widget`: Widget to use.
*   `display`: `full` to show label and value (deprecated?). Usually just renders the value.

**Note:** If you need raw values for logic (e.g., `t-if`), accessing the field directly might require the field to be present in the view but not necessarily rendered. You can put `<field name="my_field"/>` outside the `<templates>` tag or inside it without rendering it if it's just for fetching.

Wait, in Odoo 16+ / Owl Kanban:
Fields used in the template must be declared.
Inside `t-name="card"`, `<field name="foo"/>` renders the field using its widget/formatter.
To use raw values in expressions, use `record.field_name.raw_value` or `record.field_name.value`. Note that in modern Odoo (Owl), it's often just `record.field_name.value` or utilizing the field node directly.

## Components

### `<progressbar>`

Displays a progress bar on top of columns (e.g., for sales pipeline).

```xml
<progressbar field="activity_state" colors='{"planned": "success", "today": "warning", "overdue": "danger"}'/>
```

**Attributes:**
*   `field`: The field to base the progress on (usually a Selection or Status).
*   `colors`: JSON mapping values to colors (success, warning, danger, info, muted).
*   `sum_field`: Field to sum up (e.g., `expected_revenue`) alongside the count.
