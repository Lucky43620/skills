# Gantt View Architecture

Gantt views are used for planning and resource allocation over time.

The root element is `<gantt>`.

```xml
<gantt
    date_start="start_date"
    date_stop="end_date"
    default_group_by="user_id"
    color="project_id">
</gantt>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `date_start` | (Mandatory) Start date field. | - |
| `date_stop` | (Mandatory) End date field. | - |
| `default_group_by` | Field to group rows by. | - |
| `color` | Field for task color. | - |
| `scales` | Allowed time scales: `day,week,month,year`. | `day,week,month` |
| `precision` | JSON object for snap precision. | - |
| `thumbnails` | JSON object mapping group values to image fields. | - |
| `plan` | Enable "Plan" button? | `True` |

## Components

### `<field>`

Fields are used for display in the task pill or popover.
