# Powerbox (Odoo Editor)

The **Powerbox** is the command palette that appears when you type `/` in the Odoo HTML Editor (Wysiwyg).

## Adding Commands
You register commands in the `html_field_commands` category.

```javascript
import { registry } from "@web/core/registry";

registry.category("html_field_commands").add("my_command", {
    name: "Insert Quote",
    icon: "fa-quote-left",
    description: "Insert a blockquote",
    run: (editor) => {
        editor.execCommand("insertHtml", "<blockquote>Quote</blockquote>");
    },
});
```

## Categories
Commands can be grouped (e.g., 'Format', 'Structure', 'Widgets').
