# When to throw errors

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR
- `throw` uniquement pour des erreurs inattendues ou impossibles à récupérer. 
- Utilise `throw` pour signaler un bug ou une incohérence interne. 
- Les erreurs métier attendues doivent être gérées sans exception. 

## Quand l’utiliser
- Tu détectes un état impossible (ex: data corrupt). 
- Tu veux interrompre un flux parce que le système est dans un état critique. 

## Concepts clés
- **Erreur critique** : l’app ne peut pas continuer correctement. 
- **Erreur attendue** : validation ou problème utilisateur → pas de `throw`. 

## API / Syntaxe
```javascript
if (!this.env.services) {
  throw new Error("[MyModule] services not available");
}
```

## Patterns recommandés
1) **Throw explicite avec contexte**
```javascript
throw new Error(`[MyModule] Missing config: ${key}`);
```

2) **Rethrow après enrichissement**
```javascript
catch (error) {
  error.message = `[MyModule] ${error.message}`;
  throw error;
}
```

## Anti-patterns & pièges
- **Throw pour validation** → UX mauvaise. 
- **Throw sans contexte** → logs inutiles. 

## Debug & troubleshooting
- Vérifie la stack trace pour localiser l’état impossible. 
- Ajoute un test unitaire qui reproduit l’état critique. 

## Exemples complets
### Exemple — Guard critique
```
my_module/static/src/services/config.js
```
```javascript
/** @odoo-module **/
export function requireConfig(config, key) {
  if (!(key in config)) {
    throw new Error(`[config] missing ${key}`);
  }
  return config[key];
}
```

## Checklist
- [ ] `throw` réservé aux bugs/incohérences. 
- [ ] Message d’erreur explicite et contextualisé. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## Voir aussi
- [Avoid throwing errors as much as possible](avoid_throwing_errors_as_much_as_possible.md)
- [Error free control flow](error_free_control_flow.md)
- [Catching errors](catching_errors.md)
- [Errors in JavaScript](errors_in_javascript.md)
- [Error handling](index.md)
