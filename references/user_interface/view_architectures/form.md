# Form View Architecture

Form views are used to display the data from a single record. They are composed of regular HTML with additional semantic and structural components.

The root element of form views is `<form>`.

```xml
<form>
    ...
</form>
```

## Root Attributes

Optional attributes can be added to the root element `form` to customize the view:

| Attribute | Description | Default |
| :--- | :--- | :--- |
| `string` | The view title. Displayed only if opening an action with no name and target="new". | `''` |
| `create` | Disable/enable record creation on the view. | `True` |
| `edit` | Disable/enable record edition on the view. | `True` |
| `duplicate` | Disable/enable record duplication on the view through the Action dropdown. | `True` |
| `delete` | Disable/enable record deletion on the view through the Action dropdown. | `True` |
| `js_class` | The name of the JavaScript component the webclient will instantiate instead of the generic form view. | `''` |
| `focus_first_field` | Disable automatic focusing on the first field in the view. | `False` |

## Semantic Components

Semantic components tie into the Odoo system and allow interaction with it.

### `<field>`

The `field` element renders (and allows editing of, possibly) a single field of the current record.

**Attributes:**

*   `name` (Mandatory): The name of the field to render.
*   `widget`: The widget used to represent the field (e.g., `many2many_tags`, `statusbar`, `image`).
*   `string`: The label of the field. Overrides the model's string.
*   `help`: The tooltip displayed when hovering the field or its label.
*   `options`: Configuration options for the widget as a Python expression (dict). Common options for relational fields: `no_create`, `no_quick_create`, `no_open`, `no_create_edit`.
*   `readonly`: Python expression calculating whether the field is read-only.
*   `required`: Python expression calculating whether the field is required.
*   `invisible`: Python expression calculating whether the field is invisible.
*   `password`: If `True`, the field is displayed as a password (masked characters).
*   `nolabel`: If `True`, the field's label is hidden.

### `<button>`

Buttons allow triggering actions or object methods.

**Attributes:**

*   `type` (Mandatory usually):
    *   `object`: Calls a method on the model. `name` attribute must be the method name.
    *   `action`: Executes an action. `name` attribute must be the Action XMLID.
*   `name`: The method name or Action ID.
*   `string`: The button's text.
*   `icon`: Icon class (e.g., `fa-star`).
*   `class`: CSS class (e.g., `btn-primary`, `oe_stat_button`).
*   `context`: Context to pass to the method/action.
*   `invisible`: Visibility condition.
*   `confirm`: Confirmation message before execution.

### `<label>`

Displays a label for a specific field.

**Attributes:**
*   `for`: The name of the field this label is for.
*   `string`: The text content of the label.

## Structural Components

Structural components provide layout and visual organization.

### `<group>`

Used to define column layouts. By default, groups define 2 columns.

**Attributes:**
*   `string`: Title of the group.
*   `col`: Number of columns (default 2).
*   `colspan`: Number of columns taken by the group itself.

**Note:** Inside a group, a `<field>` usually takes 2 columns (1 for label, 1 for widget).

### `<notebook>` and `<page>`

Defines tabbed sections.

```xml
<notebook>
    <page string="General Info">
        ...
    </page>
    <page string="History">
        ...
    </page>
</notebook>
```

**Page Attributes:**
*   `string`: Tab title.
*   `invisible`: Visibility condition.
*   `autofocus`: Whether this page is focused by default.

### `<sheet>`

Used as a direct child of `<form>` for a nicer, responsive, paper-like layout.

```xml
<form>
    <sheet>
        <group>...</group>
    </sheet>
</form>
```

### `<header>`

Used usually at the top of the form (outside `<sheet>`) to display the status bar and workflow buttons.

```xml
<header>
    <button name="action_confirm" string="Confirm" type="object" class="btn-primary"/>
    <field name="state" widget="statusbar" statusbar_visible="draft,confirmed,done"/>
</header>
```

### `<footer>`

Used in dialogs (wizard forms) to display action buttons at the bottom.

```xml
<footer>
    <button name="action_do_it" string="Do It" type="object" class="btn-primary"/>
    <button string="Cancel" class="btn-secondary" special="cancel"/>
</footer>
```

### `<separator>`

Adds a horizontal separator line/title.

*   `string`: Title of the separator.

### `<newline>`

Forces a new row within a `<group>`.

### Button Box

A standard container for "smart buttons" (stat buttons), usually placed inside `<sheet>` at the top right.

```xml
<div class="oe_button_box" name="button_box">
    <button class="oe_stat_button" name="action_view_invoices" icon="fa-pencil-square-o" type="object">
        <field name="invoice_count" widget="statinfo" string="Invoices"/>
    </button>
</div>
```

### Title

Standard layout for the record title.

```xml
<div class="oe_title">
    <label for="name" class="oe_edit_only"/>
    <h1>
        <field name="name"/>
    </h1>
</div>
```
