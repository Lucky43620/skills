# Error free control flow

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR
- Les erreurs ne doivent pas servir à diriger la logique métier. 
- Préfère des retours explicites (`result`, `ok`, `reason`). 
- Rend le code plus lisible et testable. 

## Quand l’utiliser
- Tu écris des services, actions client, ou hooks. 
- Tu veux éviter des `try/catch` imbriqués. 

## Concepts clés
- **Résultat explicite** : objet `{ ok, data, error }`. 
- **Flux nominal** : chemin principal sans `throw`. 

## API / Syntaxe
```javascript
export function validate(data) {
  if (!data.name) {
    return { ok: false, reason: "missing_name" };
  }
  return { ok: true };
}
```

## Patterns recommandés
1) **Pattern Result**
```javascript
const result = await save();
if (!result.ok) { this.notification.add("Erreur"); }
```

2) **Validation séparée**
```javascript
const validation = validate(form);
if (!validation.ok) return;
```

3) **Fallbacks silencieux**
```javascript
const items = await fetch().catch(() => []);
```

## Anti-patterns & pièges
- **`throw` pour sortir d’une boucle** → opaque. 
- **Multiples `try/catch` imbriqués** → difficile à lire. 

## Debug & troubleshooting
- Remplace les `throw` non critiques par des retours explicites. 
- Ajoute des logs lorsque `ok=false`. 

## Exemples complets
### Exemple — Service qui retourne un `Result`
```
my_module/static/src/services/import_service.js
```
```javascript
/** @odoo-module **/
export async function importData(rpc, payload) {
  if (!payload.length) {
    return { ok: false, reason: "empty" };
  }
  const data = await rpc("/import", payload);
  return { ok: true, data };
}
```

## Checklist
- [ ] Les erreurs attendues utilisent un `Result` explicite. 
- [ ] Les `throw` sont réservés aux bugs. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi
- [Catching errors](catching_errors.md)
- [When to throw errors](when_to_throw_errors.md)
