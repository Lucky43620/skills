# Activity View Architecture

Activity views are linked to the `mail.activity` mixin and visualize next actions.

The root element is `<activity>`.

```xml
<activity string="Activities">
    <templates>
        <div t-name="activity-box">
            <field name="name" display="full"/>
            <field name="partner_id" muted="1" display="full"/>
        </div>
    </templates>
</activity>
```

## Structure

Activity views use QWeb templates (similar to Kanban) to define the content of the activity definition box.

*   Root: `<activity>`
*   Attribute `string`: View title.
*   Child `templates`: Contains QWeb templates.
