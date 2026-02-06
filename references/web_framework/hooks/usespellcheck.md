# useSpellCheck

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/hooks.html#usespellcheck
> Location: `@web/core/utils/hooks`

## Description
Active la vérification orthographique sur un input/textarea au focus, et la retire au blur (évite les lignes rouges disgracieuses quand on ne tape pas).
Cible par défaut l'élément avec `t-ref="spellcheck"`.

## Utilisation

```javascript
import { useSpellCheck } from "@web/core/utils/hooks";

class Comp extends Component {
    setup() {
        this.simpleRef = useSpellCheck(); // Cible t-ref="spellcheck"
        this.customRef = useSpellCheck({ refName: "custom" }); // Cible t-ref="custom"
    }
}
```
