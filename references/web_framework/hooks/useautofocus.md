# useAutofocus

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/hooks.html#useautofocus
> Location: `@web/core/utils/hooks`

## Description
Place le focus sur un élément référencé par `t-ref="autofocus"` dès qu'il apparaît dans le DOM (si pas déjà affiché).

## Utilisation

```javascript
import { useAutofocus } from "@web/core/utils/hooks";

class Comp extends Component {
    setup() {
        this.inputRef = useAutofocus();
    }
    static template = "Comp";
}
```

```xml
<t t-name="Comp">
    <input t-ref="autofocus" type="text"/>
</t>
```
