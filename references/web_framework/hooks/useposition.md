# usePosition

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/hooks.html#useposition
> Location: `@web/core/position_hook`

## Description
Positionne un élément HTML ("popper", souvent un menu ou tooltip) relativement à un autre élément ("reference").
Gère le repositionnement automatique au scroll ou resize.

**Important** : Utilisez `t-ref` pour cibler les éléments.

## Utilisation

```javascript
import { usePosition } from "@web/core/position_hook";
import { useRef } from "@odoo/owl";

class DropMenu extends Component {
    static template = xml`
        <button t-ref="toggler">Toggle Menu</button>
        <div t-ref="menu">Contenu Menu</div>
    `;

    setup() {
        const toggler = useRef("toggler");

        usePosition(
            () => toggler.el, // Fonction retournant l'élément référence
            {
                popper: "menu", // Nom du t-ref de l'élément à positionner
                position: "bottom-start", // "top", "bottom", "right", "left" + "-start", "-middle", "-end", "-fit"
            }
        );
    }
}
```

## Options
- **popper**: String (nom du t-ref). Défaut "popper".
- **position**: String (ex: `bottom-start`, `right-middle`).
- **onPositioned**: Callback `(el, solution) => void`.
