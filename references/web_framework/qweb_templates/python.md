# Python Expressions (QWeb)

In Server-Side QWeb (Python), expressions are evaluated in a sandboxed Python environment.

## Context
You have access to:
*   `user`: Current user record.
*   `res_company`: Current company.
*   `env`: The Environment.
*   `time`, `datetime`, `dateutil`: Standard libraries.

## Call Syntax
```xml
<span t-out="record.date_order.strftime('%Y-%m-%d')"/>
<span t-out="len(record.line_ids)"/>
```

## Assignation
```xml
<t t-set="total" t-value="sum(line.price_subtotal for line in record.order_line)"/>
```

## Security
For security reasons, you cannot import modules or access private methods (`_method`) from QWeb.
