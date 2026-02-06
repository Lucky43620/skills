# Setting Variables (QWeb)

## `t-set` and `t-value`
Defines a variable available in the current scope and its descendants.

### Syntax
```xml
<t t-set="my_var" t-value="record.amount * 0.2"/>
<!-- Use it later -->
<span t-out="my_var"/>
```

### Body Content (Capturing)
If `t-value` is omitted, the body of the element is rendered and assigned to the variable.

```xml
<t t-set="my_html_block">
    <div class="card">
        <h1>Title</h1>
    </div>
</t>

<!-- Output the captured block -->
<t t-out="my_html_block"/>
```

### Scope
Variables are scoped to the element they are defined on and its children. They do not leak upwards.
