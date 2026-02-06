# usePager

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/hooks.html#usepager
> Location: `@web/search/pager_hook`

## Description
Affiche et configure le **Pager** du Control Panel d'une vue.
Met à jour `env.config` avec les props du pager.

## Utilisation

```javascript
import { usePager } from "@web/search/pager_hook";
import { useState } from "@odoo/owl";

class CustomView extends Component {
    setup() {
        this.state = useState({ offset: 0, limit: 80, total: 50 });

        usePager(() => {
            return {
                offset: this.state.offset,
                limit: this.state.limit,
                total: this.state.total,
                onUpdate: (newState) => {
                    Object.assign(this.state, newState);
                },
            };
        });
    }
}
```
