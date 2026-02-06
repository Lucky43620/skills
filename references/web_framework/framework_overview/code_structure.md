# Code Structure

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#code-structure

## TL;DR

- Tout le code JS/CSS/Templates se trouve dans `web/static/src`.
- Les imports utilisent l'alias `@web`.

## Structure des dossiers (`web/static/src`)

- `core/` : Fonctionnalités bas niveau (bus, registry, user service, utils...).
- `fields/` : Tous les composants de champs (Char, Integer, Many2one...).
- `views/` : Composants des vues (Form, List, Kanban...).
- `search/` : Control panel, barre de recherche, panneau de recherche.
- `webclient/` : Code spécifique au client web (NavBar, UserMenu, ActionService).

## Imports

Tout fichier dans `web/static/src` peut être importé via le préfixe `@web`.

**Exemple :**
```javascript
import { memoize } from "@web/core/utils/functions";
```
