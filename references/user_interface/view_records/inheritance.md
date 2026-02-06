# View Inheritance

Inheritance allows for customizing delivered views. It makes it possible to add content as modules are installed or to deliver different displays according to action.

## Generic Structure

```xml
<record id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
    <field name="name">NAME</field>
    <field name="model">MODEL</field>
    <field name="inherit_id" ref="PARENT_VIEW_REFERENCE"/>
    <field name="mode">MODE</field>
    <field name="arch" type="xml">
        <xpath expr="XPATH" position="POSITION">
            <CONTENT/>
        </xpath>
        <!-- OR -->
        <NODE ATTRIBUTES="VALUES" position="POSITION">
            <CONTENT/>
        </NODE>
    </field>
</record>
```

## Key Fields

*   `inherit_id`: Reference to the parent view being modified.
*   `mode`:
    *   `extension` (default): Modifies the parent view in place.
    *   `primary`: Creates a new view based on the parent view (inheritance specs applied), but detached from it for lookup purposes (can be selected as a specific view for an action).

## Inheritance Specs

Inheritance specs consist of an element locator and a modification position.

### Locators

1.  `xpath`: Generic XPath expression.
    *   `<xpath expr="//field[@name='description']" ...>`
2.  `field`: Shortcut for `//field[@name='...']`.
    *   `<field name="description" ...>`
3.  `node`: Matching by name and attributes.

### Positions

The `position` attribute determines where the new content is placed relative to the matched node:

*   `inside` (default): Appended as the last child of the matched node.
*   `after`: Inserted after the matched node.
*   `before`: Inserted before the matched node.
*   `replace`: Replaces the matched node.
*   `attributes`: Modifies the attributes of the matched node. Use `<attribute name="attr_name">value</attribute>` inside.

**Example: Modifying Attributes**
```xml
<field name="name" position="attributes">
    <attribute name="required">1</attribute>
    <attribute name="string">New Label</attribute>
</field>
```

**Example: XPath**
```xml
<xpath expr="//page[@name='general']" position="after">
    <page string="New Tab">...</page>
</xpath>
```
