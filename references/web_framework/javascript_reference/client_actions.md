# Client Actions (`ir.actions.client`)

Client actions trigger the execution of arbitrary Javascript code (a Component) within the web client, without simply loading a view.

## Definition
1.  **Register:** Register your component in the `actions` registry.
2.  **Define:** Create an `ir.actions.client` record in XML.

## JS Side
```javascript
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class MyClientAction extends Component {
    static template = "my_module.template";
}

registry.category("actions").add("my_module.my_action_tag", MyClientAction);
```

## XML Side
```xml
<record id="action_my_client" model="ir.actions.client">
    <field name="name">My Dashboard</field>
    <field name="tag">my_module.my_action_tag</field>
</record>
```
