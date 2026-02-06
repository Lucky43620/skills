# useBus

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/hooks.html#usebus
> Location: `@web/core/utils/hooks`

## Description
Ajoute un écouteur d'événement sur un bus et le retire automatiquement quand le composant est démonté ("unmounted").
C'est la méthode recommandée pour écouter le `env.bus` sans fuite de mémoire.

## Utilisation

```javascript
import { useBus } from "@web/core/utils/hooks";

class MyComponent extends Component {
    setup() {
        useBus(this.env.bus, "some-event", (event) => {
            console.log("Événement reçu :", event);
        });
    }
}
```

## API
`useBus(bus, eventName, callback)`
- **bus**: L'objet EventBus cible.
- **eventName**: Nom de l'événement.
- **callback**: Fonction à exécuter.
