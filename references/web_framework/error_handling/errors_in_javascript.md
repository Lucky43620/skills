# Errors in JavaScript

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR

- Distinguer erreurs attendues (validation) et erreurs inattendues (bugs).
- Les erreurs attendues se gèrent via UI (`notification`, `dialog`) plutôt que `throw`.
- Les erreurs inattendues doivent être loggées et remontées pour éviter les états incohérents.

## Quand l’utiliser

- Quand tu crées des composants OWL, actions client ou services JS.
- Quand tu dois décider entre feedback UX et exception technique.

## Concepts clés

- **Erreur attendue** : flux métier normal, feedback utilisateur.
- **Erreur inattendue** : bug, état impossible, module manquant.
- **Propagation** : du composant vers le webclient via services/boundaries.

## API / Syntaxe

```javascript
/** @odoo-module **/
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
  setup() {
    this.notification = useService("notification");
  }

  async onSave() {
    try {
      await this.env.services.rpc("/my/route");
    } catch (error) {
      this.notification.add("Erreur réseau", { type: "danger" });
    }
  }
}
```

## Patterns recommandés

1) **Erreur attendue = feedback UI**
```javascript
if (!this.state.name) {
  this.notification.add("Nom requis", { type: "warning" });
  return;
}
```

2) **Erreur inattendue = log + rethrow**
```javascript
catch (error) {
  console.error("[MyModule]", error);
  throw error;
}
```

3) **Retour explicite plutôt que `throw`**
```javascript
return { ok: false, reason: "missing_name" };
```

## Anti-patterns & pièges

- Utiliser `throw` pour piloter le flux UI.
- Catch global silencieux qui masque les bugs.
- Ignorer les promesses rejetées (`Uncaught (in promise)`).

## Debug & troubleshooting

- Inspecter la console et la stack trace.
- Tester avec `?debug=assets` pour lire les sources non minifiées.
- Ajouter un contexte dans les messages d’erreur.

## Exemples complets

### Exemple — Validation UI + rethrow conditionnel
```
my_module/static/src/components/my_form.js
```
```javascript
/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MyForm extends Component {
  setup() {
    this.notification = useService("notification");
  }

  async onSubmit() {
    if (!this.state.email) {
      this.notification.add("Email requis", { type: "warning" });
      return;
    }
    try {
      await this.env.services.rpc("/my/submit", this.state);
    } catch (error) {
      console.error("[my_form]", error);
      throw error;
    }
  }
}
```

## Checklist

- [ ] Erreurs attendues traitées par feedback UI.
- [ ] Erreurs inattendues loggées et rethrow si critique.
- [ ] Pas de `catch` silencieux.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi

- [Avoid throwing errors as much as possible](avoid_throwing_errors_as_much_as_possible.md)
- [Catching errors](catching_errors.md)
- [When to throw errors](when_to_throw_errors.md)
- [Error free control flow](error_free_control_flow.md)
