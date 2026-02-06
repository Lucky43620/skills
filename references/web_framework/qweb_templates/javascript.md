# Javascript Expressions (QWeb)

In Client-Side QWeb (Owl), expressions are Javascript.

## Scope
The scope is the component's state and props, plus anything passed in `t-set`.

## Syntax
Standard JS expression syntax.

```xml
<div t-if="props.total > 100">
    <span t-out="props.total.toFixed(2)"/>
</div>

<!-- String concatenation -->
<div t-att-class="'btn btn-' + (isActive ? 'primary' : 'secondary')">
    Click Me
</div>
```

## Helpers
Unlike Python, there are very few global helpers. Most logic should be computed in the Component's `setup()` or `getters` and passed to the template.
