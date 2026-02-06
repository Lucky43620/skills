# Playbook Debug — Odoo v19

## Backend (Python)
- Active **log SQL** (si pertinent), identifie les requêtes N+1, vérifie **prefetch** / **cache**.
- Vérifie les droits : règles d’accès, record rules, `sudo()` utilisé ou non.
- Sur `@api.onchange`: ne jamais appeler CRUD sur pseudo-record; préfère `update()`.

## Frontend (JS/Owl)
- Utilise `?debug=assets` pour assets non minifiés, `?debug=tests` pour les bundles de test. (voir doc “developer mode”) 
- Vérifie l’ordre de chargement des bundles, les dépendances, et l’enregistrement dans les registries.
- Pour patching: patch `setup()` d’un composant plutôt que son constructor.

## Erreurs fréquentes
- champ + méthode même nom (silencieusement écrasé)
- recordset multi, oubli de `ensure_one()`
- `sudo()` cachant un problème de règle d’accès
- assets mal déclarés dans `__manifest__.py`
