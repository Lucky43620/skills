# Error handling

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR
- Le webclient Odoo distingue erreurs attendues (validation) et inattendues (bugs). 
- Les erreurs ne doivent pas piloter le flux normal de l’UI. 
- Utilise notifications, dialogues et messages de service pour les erreurs attendues. 
- Les erreurs inattendues doivent être loggées et remontées proprement. 
- `?debug=assets` aide à corréler erreurs JS et sources. 

## Quand l’utiliser
- Tu manipules des services JS (`rpc`, `notification`, `dialog`). 
- Tu codes des actions client ou des composants OWL. 
- Tu dois gérer des erreurs réseau ou de validation côté UI. 

## Concepts clés
- **Erreur attendue** : cas métier (données invalides, permissions). 
- **Erreur inattendue** : bug JS, crash, module manquant. 
- **Boundary OWL** : composant qui intercepte les erreurs descendantes. 
- **Service de notification** : feedback utilisateur sans `throw`. 

## API / Syntaxe
```javascript
/** @odoo-module **/
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
  setup() {
    this.notification = useService("notification");
  }

  async onClick() {
    try {
      await this.env.services.rpc("/my/route", { payload: 1 });
    } catch (error) {
      this.notification.add("Erreur réseau", { type: "danger" });
    }
  }
}
```

## Patterns recommandés
1) **Feedback utilisateur pour erreurs attendues**
→ `notification`/`dialog` au lieu de `throw`. 

2) **Capture locale + rethrow si critique**
```javascript
try { ... } catch (error) { log; throw error; }
```
→ permet d’enrichir le contexte sans masquer les bugs. 

3) **Distinguer validation UI vs serveur**
→ validation simple en UI, validation finale côté serveur. 

## Anti-patterns & pièges
- **Throw pour le contrôle de flux** → code fragile et UX pauvre. 
- **Masquer toutes les erreurs** → bugs silencieux. 
- **Promesses non gérées** → `Uncaught (in promise)` difficile à diagnostiquer. 

## Debug & troubleshooting
- Active `?debug=assets` pour retrouver les sources JS. 
- Inspecte le stack trace et les modules concernés. 
- Vérifie les erreurs RPC dans l’onglet réseau. 

## Exemples complets
### Exemple — Gestion d’erreur RPC
```
my_module/static/src/components/my_component.js
```
```javascript
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
  setup() {
    this.notification = useService("notification");
    this.rpc = useService("rpc");
  }

  async fetchData() {
    try {
      return await this.rpc("/my/route");
    } catch (error) {
      this.notification.add("Impossible de charger", { type: "warning" });
      return null;
    }
  }
}
```

## Checklist
- [ ] Erreurs attendues → notification/dialog. 
- [ ] Erreurs inattendues → log + rethrow si besoin. 
- [ ] Tests en `?debug=assets`. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi
- [Errors in JavaScript](errors_in_javascript.md)
- [Catching errors](catching_errors.md)
- [Error free control flow](error_free_control_flow.md)
- [Services](../services/index.md)
