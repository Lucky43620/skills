# Conditionals (QWeb)

## `t-if`
Renders the element only if the expression evaluates to truthy.

```xml
<div t-if="record.state == 'done'">
    Locked
</div>
```

## `t-elif` and `t-else`
Used for multi-branch logic. Must be placed on immediate following siblings.

```xml
<span t-if="val > 10">High</span>
<span t-elif="val > 5">Medium</span>
<span t-else="">Low</span>
```

## Helpers
Remember that Python rules apply for truthiness in server-side QWeb, and JS rules in client-side QWeb.
*   **Python:** `None`, `False`, `[]`, `""`, `0` are falsy.
*   **JS:** `undefined`, `null`, `false`, `""`, `0` are falsy.
