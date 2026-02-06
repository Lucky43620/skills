# Services (Web Framework)

Les services sont des singletons persistants qui gèrent l'état global et les interactions avec le serveur ou le navigateur.

## Sommaire

### 1. [Utiliser un Service](services/using_a_service.md)
Comment consommer un service existant dans un composant avec `useService`.
```javascript
const notifications = useService("notification");
```

### 2. [Liste des Services Standards](services/reference_list.md)
Référence des services intégrés :
- `orm`: Appels Python.
- `action`: Navigation et fenêtres.
- `rpc`: Requêtes HTTP/JSON.
- `user`: Contexte utilisateur.
- `router`, `hotkey`, `cookie`, `title`...

### 3. [Créer un Service](services/defining_a_service.md)
Comment définir votre propre service global.
- `registry.category("services").add(...)`
- Gestion des dépendances (`start(env, { otherService })`).
