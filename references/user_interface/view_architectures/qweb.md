# QWeb Views (`ir.ui.view` type='qweb')

QWeb views are used for Reports, Website pages, and Snippets. Unlike Form/List views, they are pure HTML templates.

## Structure
```xml
<record id="my_view" model="ir.ui.view">
    <field name="name">My View</field>
    <field name="type">qweb</field>
    <field name="key">my_module.my_key</field>
    <field name="arch" type="xml">
        <t t-name="my_module.my_key">
            <div>
                <h1>Hello</h1>
            </div>
        </t>
    </field>
</record>
```

## Key Fields
*   **key:** Unique identifier (like an External ID) used to look up the view.
*   **inherit_id:** Parent view ID (for extending/patching).
*   **priority:** Determines load order if multiple views map to the same resource.

## Usage
*   **Reports:** The layout of the PDF.
*   **Website:** The layout of the page.
*   **Client Actions:** Can utilize `qweb` templates for rendering.
