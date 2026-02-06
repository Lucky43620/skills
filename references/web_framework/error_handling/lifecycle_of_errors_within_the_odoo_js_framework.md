# Lifecycle of errors within the Odoo JS framework

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR
- Les erreurs JS traversent plusieurs couches : composant → services → webclient. 
- OWL propage les erreurs vers des boundaries ou le root. 
- Les erreurs RPC remontent via le service `rpc` et peuvent être interceptées. 
- Toujours enrichir le contexte avant de remonter une erreur critique. 

## Quand l’utiliser
- Tu veux comprendre pourquoi une erreur casse tout l’écran. 
- Tu configures des boundaries OWL ou des handlers globaux. 

## Concepts clés
- **Boundary OWL** : intercepte les erreurs des enfants. 
- **Services** : lieux fréquents de propagation (rpc, notification). 
- **Webclient** : couche supérieure qui affiche un crash screen si non géré. 

## API / Syntaxe
```javascript
/** @odoo-module **/
import { ErrorDialog } from "@web/core/errors/error_dialog";
import { useService } from "@web/core/utils/hooks";

export class MyBoundary extends Component {
  setup() {
    this.dialog = useService("dialog");
  }

  onError(error) {
    this.dialog.add(ErrorDialog, { error });
  }
}
```

## Patterns recommandés
1) **Boundary local pour zones critiques**
→ évite que tout le webclient ne tombe. 

2) **Enrichir le contexte**
```javascript
error.message = `[MyFeature] ${error.message}`;
```

3) **Utiliser les services pour remonter proprement**
→ notification/dialog pour les erreurs attendues. 

## Anti-patterns & pièges
- **Catch global silencieux** → erreur perdue. 
- **Multiples boundaries imbriqués** → gestion incohérente. 

## Debug & troubleshooting
- Inspecte la console pour voir la couche qui a intercepté. 
- Vérifie si l’erreur vient d’un service (rpc) ou d’un composant. 
- Ajoute un identifiant de contexte dans les logs pour tracer le flux. 

## Exemples complets
### Exemple — Boundary locale sur un panneau
```
my_module/static/src/components/panel_with_boundary.js
```
```javascript
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ErrorDialog } from "@web/core/errors/error_dialog";

export class PanelWithBoundary extends Component {
  setup() {
    this.dialog = useService("dialog");
  }

  onError(error) {
    this.dialog.add(ErrorDialog, { error });
  }
}
```

## Checklist
- [ ] Boundary sur les zones critiques. 
- [ ] Contexte enrichi pour les erreurs critiques. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi
- [Catching errors](catching_errors.md)
- [Errors in JavaScript](errors_in_javascript.md)
- [Avoid throwing errors as much as possible](avoid_throwing_errors_as_much_as_possible.md)
- [When to throw errors](when_to_throw_errors.md)
- [Error handling](index.md)
