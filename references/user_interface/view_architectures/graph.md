# Graph View Architecture

Graph views are used to visualize aggregated data over a number of records.

The root element is `<graph>`.

```xml
<graph string="Invoices Analysis" type="bar" stacked="1">
    <field name="partner_id"/>
    <field name="amount_total" type="measure"/>
</graph>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `type` | Chart type: `bar`, `line`, `pie`. | `bar` |
| `stacked` | Stack bars/lines (True/False). | `False` |
| `disable_linking` | Prevent clicking points to go to the list/form view. | `False` |
| `order` | Sorting order for the x-axis (e.g., `amount_total desc`). | `None` |

## Components

### `<field>`

Defines the dimensions (grouping) and measures of the chart.

**Attributes:**
*   `name`: The field to group by or measure.
*   `type`:
    *   `row`: (Default) Groups by this field (X-axis for Bar/Line).
    *   `col`: Groups using a second dimension (Legend/Color).
    *   `measure`: usage as value Y-axis.
*   `interval`: For Date/Datetime fields (`day`, `week`, `month`, `year`).
