# Map View Architecture

Map views are used to visualize records on a map. They require the record to contain an address or coordinates.

The root element is `<map>`.

```xml
<map res_partner="partner_id" default_order="date_begin" routing="true">
    <field name="partner_id"/>
    <field name="name"/>
</map>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `res_partner` | (Mandatory) Many2one field to `res.partner` for address/cols. | - |
| `routing` | Enable routing between points. | `False` |
| `default_order` | Sorting order of the list side-panel. | - |
| `hide_name` | Hide the name on the marker. | `False` |
| `hide_address` | Hide the address on the marker. | `False` |
| `hide_title` | Hide the top title bar. | `False` |

## Components

### `<field>`

Fields inside `<map>` are used for the marker popup or the side-panel list item.
*   `name`: Displayed in the marker/list.
*   `string`: Label.
