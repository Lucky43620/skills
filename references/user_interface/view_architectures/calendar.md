# Calendar View Architecture

Calendar views display records as events on a daily, weekly, monthly, or yearly calendar.

The root element is `<calendar>`.

```xml
<calendar string="Meetings" date_start="start" date_stop="stop" color="partner_id">
    <field name="name"/>
    <field name="partner_id"/>
</calendar>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `date_start` | (Mandatory) Field for the event start date. | - |
| `date_stop` | Field for the event end date. | - |
| `date_delay` | Field for duration (alternative to date_stop). | - |
| `color` | Field used to colorize events (usually M2O or Selection). | - |
| `all_day` | Boolean field indicating all-day events. | - |
| `mode` | Default display mode: `day`, `week`, `month`, `year`. | `week` |
| `quick_create` | Enable click-and-drag creation. | `True` |
| `event_open_popup` | Open form in dialog instead of navigating. | `False` |
| `create_name_field` | Field to populate when typing in the quick create input. | `name` |

## Components

### `<field>`

Fields inside `<calendar>` are typically used for:
1.  **Display:** Shown on the event card/pill (e.g., `name`, `location`).
2.  **Filtering:** Used in the "Attributes" sidebar (if `avatar_field` or similar is used).
