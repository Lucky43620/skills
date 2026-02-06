# Pivot View Architecture

Pivot views are used to visualize aggregated data as a pivot table (cross-tabulation).

The root element is `<pivot>`.

```xml
<pivot string="Sales Analysis" disable_linking="True" display_quantity="true">
    <field name="date_order" type="row" interval="month"/>
    <field name="team_id" type="col"/>
    <field name="amount_total" type="measure"/>
</pivot>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `disable_linking` | Prevent clicking cells to go to the list view. | `False` |
| `display_quantity` | Display the "Count" measure by default. | `True` |
| `default_order` | Default sorting (e.g., `amount_total desc`). | `None` |

## Components

### `<field>`

Defines the rows, columns, and measures.

**Attributes:**
*   `name`: The field to use.
*   `type`:
    *   `row`: Group by this field on rows (Left axis).
    *   `col`: Group by this field on columns (Top axis).
    *   `measure`: Calculate statistics on this field.
*   `interval`: For Date/Datetime fields (`day`, `week`, `month`, `quarter`, `year`).
*   `invisible`: Hide this field by default (can be enabled via "Measures").
