# Advanced Output (QWeb)

## `t-cache`
Caches the rendered output of a template part.
**Key:** The cache key expression.

```xml
<div t-cache="record.id, record.write_date">
    <!-- Complex computation is cached per record+date -->
    <t t-out="record.very_complex_computation()"/>
</div>
```

## `t-nocache`
Excludes a part from the cache (e.g., for user-specific data inside a cached block).

```xml
<div t-cache="...">
    Most content...
    <span t-nocache="The user name is dynamic">
        <t t-out="user.name"/>
    </span>
</div>
```

## `t-translation`
Controls translation behavior.
*   `off`: Disables translation for the content.
*   `on`: Forces translation (default).
