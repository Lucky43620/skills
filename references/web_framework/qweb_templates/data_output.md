# Data Output (QWeb)

## `t-out` (Escaped)
Outputs the value of an expression, **escaping** HTML characters (security safe).
*   **Alias:** `t-esc` (deprecated in newer versions, prefer `t-out`).

```xml
<span t-out="record.name"/>
<!-- If name is "A&B", output is "A&amp;B" -->
```

## `t-raw` (Unescaped)
Outputs the raw value without escaping. **Danger:** Prone to XSS. Use only if you strictly trust the content.

```xml
<div t-raw="record.description_html"/>
```

## `t-field` (Field Formatting)
Specific to Odoo views. format the value according to the field type (Date, Float, Monetary).

```xml
<span t-field="record.date_order"/>
<span t-field="record.amount_total" t-options="{'widget': 'monetary', 'display_currency': currency}"/>
```
