# Attributes (QWeb)

## `t-att-` (Dynamic Attributes)
Adds or sets an HTML attribute dynamically.

```xml
<!-- If my_id is 5 -->
<div t-att-id="my_id">...</div>
<!-- Result: <div id="5">...</div> -->
```

## `t-attf-` (Format String)
Interpolates values directly into a string string using `{{ }}`.

```xml
<div t-attf-class="btn btn-{{ style_color }}">...</div>
<!-- If style_color is 'primary' -->
<!-- Result: <div class="btn btn-primary">...</div> -->
```

## `t-att` (Mapping)
Accepts a dictionary/object and unpacks it as attributes.

```xml
<div t-att="{'data-id': 1, 'class': 'active'}"/>
<!-- Result: <div data-id="1" class="active"/> -->
```

## Class Lists
If you pass a list to `class`, Odoo joins them with spaces.
```xml
<div t-att-class="['a', 'b']"/>
<!-- <div class="a b"/> -->
```
