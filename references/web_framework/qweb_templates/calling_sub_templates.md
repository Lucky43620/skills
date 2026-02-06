# Calling Sub-templates (QWeb)

## `t-call`
Invokes another template by its XML ID.

```xml
<t t-call="module_name.other_template_id"/>
```

## Passing Variables
Variables defined inside the `t-call` body (using `t-set`) are passed to the sub-template.

```xml
<t t-call="web.layout">
    <t t-set="title">My Custom Page</t>
    <div>
        Page Content...
    </div>
</t>
```

## `t-out="0"` (The Body)
In the *called* template, the content defined inside the `t-call` tag (like "Page Content..." above) is injected where `t-out="0"` is placed.

```xml
<!-- web.layout template definition -->
<html>
    <title><t t-out="title"/></title>
    <body>
        <t t-out="0"/> <!-- Content is injected here -->
    </body>
</html>
```
