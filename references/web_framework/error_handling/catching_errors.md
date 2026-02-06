# Catching errors

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR
- Capture les erreurs au niveau le plus proche de la source. 
- Log + enrichissement du contexte avant propagation. 
- Utilise les services (notification, dialog) pour informer l’utilisateur. 
- Ne masque pas systématiquement les erreurs critiques. 

## Quand l’utiliser
- Toute interaction réseau (`rpc`) ou accès à un service. 
- Actions client et composants OWL avec effets de bord. 

## Concepts clés
- **Propagation contrôlée** : catch, log, puis rethrow si nécessaire. 
- **Boundary OWL** : composant de garde pour capturer les erreurs UI. 

## API / Syntaxe
```javascript
try {
  await this.rpc("/route");
} catch (error) {
  this.notification.add("Erreur RPC", { type: "danger" });
  throw error; // si critique
}
```

## Patterns recommandés
1) **Catch local et feedback**
```javascript
try { ... } catch (error) { this.notification.add("..."); }
```

2) **Contexte additionnel**
```javascript
catch (error) {
  error.message = `[MyComponent] ${error.message}`;
  throw error;
}
```

3) **Fallback**
```javascript
catch (error) { return []; }
```
→ utile si l’erreur est tolérable. 

## Anti-patterns & pièges
- **Catch vide** → erreur silencieuse. 
- **Catch global** → masque la source et rend le debug impossible. 

## Debug & troubleshooting
- Vérifie la console pour les erreurs `Uncaught (in promise)`. 
- Ajoute des logs structurés avec le nom du module. 
- Utilise `?debug=assets` pour remonter aux sources non minifiées. 

## Exemples complets
### Exemple — Service avec fallback
```
my_module/static/src/services/metrics_service.js
```
```javascript
/** @odoo-module **/
export async function fetchMetrics(rpc) {
  try {
    return await rpc("/metrics");
  } catch (error) {
    console.warn("[metrics] fallback", error);
    return { total: 0 };
  }
}
```

## Checklist
- [ ] Chaque `catch` fait quelque chose d’utile (log, feedback, fallback). 
- [ ] Les erreurs critiques sont rethrow. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi
- [Avoid throwing errors as much as possible](avoid_throwing_errors_as_much_as_possible.md)
- [Error free control flow](error_free_control_flow.md)
- [Errors in JavaScript](errors_in_javascript.md)
- [When to throw errors](when_to_throw_errors.md)
- [Error handling](index.md)
