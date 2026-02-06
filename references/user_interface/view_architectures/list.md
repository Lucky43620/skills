# List View Architecture

List views (formerly known as Tree views) are used to view and edit multiple records.

The root element is `<list>`.

```xml
<list>
    ...
</list>
```

## Root Attributes

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `string` | The view title. | `''` |
| `create` | Disable/enable record creation. | `True` |
| `edit` | Disable/enable record editing. | `True` |
| `delete` | Disable/enable record deletion. | `True` |
| `import` | Disable/enable record import. | `True` |
| `export_xlsx` | Disable/enable record export. | `True` |
| `multi_edit` | Activate multi-editing (set to `1`). | `None` |
| `editable` | Make the list editable in-place ("top" or "bottom"). | `None` |
| `open_form_view` | Show a button to open the form view even if editable. | `False` |
| `default_order` | Overrides the model's `_order`. (e.g., "name desc, id"). | `None` |
| `decoration-{$name}` | Conditional row styling (bf, it, danger, info, etc.). | `None` |
| `limit` | Default size of a page. | `80` |

## Components

### `<field>`

Defines a column in the list.

**Attributes:**

*   `name`: Field name.
*   `string`: Column label.
*   `width`: Force a column width (e.g., `width="100px"`).
*   `optional`: Make the column optional (`show` or `hide`). User can toggle it.
*   `invisible`: Visibility condition (Python expression).
*   `column_invisible`: Hides the column entirely based on context/parent values (unlike `invisible` which is row-specific context).
*   `readonly`: Editability condition.
*   `widget`: Widget for the cell.
*   `sum`, `avg`: Displays an aggregation at the bottom. Value is the label (e.g., `sum="Total"`).
*   `decoration-{$name}`: Conditional cell styling (e.g., `decoration-danger="amount < 0"`).
*   `nolabel`: If True, no header is displayed (rarely used in lists).
*   `class`: CSS classes (e.g., `oe_edit_only`).

### `<button>`

Displays a button in a list row.

**Attributes:**

*   `name`: Method name or Action ID.
*   `type`: `object` or `action`.
*   `string`: Tooltip/Text.
*   `icon`: Icon class.
*   `title`: Tooltip (alternative to string).
*   `invisible`: Visibility condition.
*   `column_invisible`: Completely remove the button column.

### `<groupby>`

Used to define custom group headers when grouping by Many2one fields.

```xml
<groupby name="partner_id">
    <button name="action_edit" type="edit" string="Edit"/>
    <field name="city"/>
</groupby>
```

### `<control>` and `<create>`

Used in editable lists (especially X2many) to customize the "Add a line" behavior.

```xml
<control>
    <create string="Add a product" context="{'default_product_type': 'product'}"/>
    <create string="Add a service" context="{'default_product_type': 'service'}"/>
</control>
```

## Decorations

Decorations allow changing the style of a row or cell based on a Python expression.

*   `decoration-bf`: Bold font.
*   `decoration-it`: Italic font.
*   `decoration-danger`: Red text.
*   `decoration-info`: Light blue text.
*   `decoration-muted`: Light gray text.
*   `decoration-primary`: Purple/Primary color text.
*   `decoration-success`: Green text.
*   `decoration-warning`: Orange/Brown text.

Example:
```xml
<list decoration-danger="amount &lt; 0" decoration-info="state == 'draft'">
    <field name="name"/>
    <field name="amount"/>
    <field name="state"/>
</list>
```
