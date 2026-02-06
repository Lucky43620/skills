# Reference List (Registries)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/registries.html#reference-list

## Principaux Registres

| Category | Description |
| :--- | :--- |
| `services` | Services activés au démarrage (`env.services`). |
| `fields` | Composants de champs (Form/List/Kanban). |
| `views` | Composants de vues (Form, List...). |
| `main_components` | Composants globaux (Dialogs, Notifications, LoadingIndicator). |
| `systray` | Éléments de la barre supérieure droite (Messaging, UserMenu...). |
| `user_menuitems` | Items du menu utilisateur (Log out, Preferences...). |
| `formatters` | Fonctions de formatage de valeurs. |
| `parsers` | Fonctions de parsing de valeurs. |
| `effects` | Effets visuels (Rainbow man). |

---

## Détails Spécifiques

### Main Components Registry
Pour ajouter des composants "top level" (vivants au dessus de tout).
Le `MainComponentsContainer` affiche cette liste.

```javascript
registry.category("main_components").add("LoadingIndicator", {
    Component: LoadingIndicator,
    props: {}
});
```

### Systray Registry
Items à droite de la navbar.
Objet attendu :
- `Component` : Classe du composant (doit être un `<li>`).
- `props` : (Optionnel).
- `isDisplayed(env)` : (Optionnel) Fonction retournant un booléen.

```javascript
registry.category("systray").add("my_item", {
    Component: MySystrayItem,
    isDisplayed: (env) => env.debug,
}, { sequence: 50 });
```

### User Menu Registry (%user_menuitems%)
Items dans le menu déroulant de l'utilisateur.
Fonction prenant `env` et retournant :
- `description` : Texte affiché.
- `callback` : Fonction exécutée au clic.
- `hide` : Booléen.
- `sequence` : Ordre (Défaut 100).

```javascript
registry.category("user_menuitems").add("log_out", (env) => {
    return {
        description: env._t("Log out"),
        callback: () => { browser.location.href = "/web/session/logout"; },
        sequence: 100,
    };
});
```
