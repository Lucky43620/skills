# Loops (QWeb frontend)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/qweb.html

## TL;DR

- Boucles via `t-foreach` + `t-as` + `t-key`.
- Toujours fournir un `t-key` stable pour éviter des glitchs DOM.

## Exemples

```xml
<t t-foreach="props.items" t-as="item" t-key="item.id">
  <div><t t-esc="item.name"/></div>
</t>
```
