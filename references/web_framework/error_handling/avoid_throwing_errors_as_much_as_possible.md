# Avoid throwing errors as much as possible

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR
- `throw` doit être réservé aux erreurs inattendues. 
- Pour une validation UX, préfère `notification`, `dialog` ou un message inline. 
- Un `throw` stoppe la chaîne de rendu et peut casser le cycle OWL. 
- Les erreurs attendues doivent être gérées localement. 

## Quand l’utiliser
- Tu construis un formulaire ou un flow utilisateur. 
- Tu veux empêcher une action sans casser l’application. 

## Concepts clés
- **Erreur attendue** : feedback utilisateur → pas de `throw`. 
- **Erreur inattendue** : bug → `throw` pour remonter correctement. 

## API / Syntaxe
```javascript
/** @odoo-module **/
import { useService } from "@web/core/utils/hooks";

const notification = useService("notification");
notification.add("Champs obligatoires manquants", { type: "warning" });
```

## Patterns recommandés
1) **Validation UI sans exception**
```javascript
if (!this.state.name) {
  this.notification.add("Nom requis", { type: "danger" });
  return;
}
```

2) **Résultat explicite plutôt que `throw`**
```javascript
return { ok: false, reason: "missing" };
```

3) **Dialog pour les erreurs bloquantes**
```javascript
this.dialog.add(ConfirmationDialog, { body: "Action impossible" });
```

## Anti-patterns & pièges
- **`throw` pour contrôler le flux** → stack trace polluée. 
- **`throw` dans un handler UI** → composant cassé et re-render incohérent. 

## Debug & troubleshooting
- Inspecte les stack traces pour trouver le `throw` d’origine. 
- Remplace les `throw` non critiques par un feedback UI. 
- Vérifie les handlers async pour éviter les `Uncaught (in promise)`. 

## Exemples complets
### Exemple — Validation de formulaire
```
my_module/static/src/components/customer_form.js
```
```javascript
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class CustomerForm extends Component {
  setup() {
    this.notification = useService("notification");
  }

  onSubmit() {
    if (!this.state.email) {
      this.notification.add("Email requis", { type: "warning" });
      return;
    }
    // suite normale
  }
}
```

## Checklist
- [ ] Les erreurs attendues ne font pas de `throw`. 
- [ ] Les messages utilisateur sont clairs et actionnables. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi
- [Errors in JavaScript](errors_in_javascript.md)
- [When to throw errors](when_to_throw_errors.md)
- [Catching errors](catching_errors.md)
- [Error free control flow](error_free_control_flow.md)
- [Error handling](index.md)
