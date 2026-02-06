# Owl Components (Web Framework)

**Odoo Web Library (Owl)** est le framework UI moderne d'Odoo (inspiré de React/Vue).
Tout le frontend v19 (et une partie du Point of Sale) est construit avec Owl.

## Sommaire

### 1. [Concepts de Base](owl_components/using_owl_components.md)
Comment créer un composant standard.
- `class MyComponent extends Component`
- `static template`
- `setup()` et `useState`

### 2. [Liste des Composants Génériques](owl_components/reference_list.md)
Ne réinventez pas la roue ! Odoo fournit déjà :
- `Dropdown`, `CheckBox`, `Pager`
- `Notebook` (Onglets), `ActionSwiper`
- `SelectMenu` (Select avancé)

### 3. [Bonnes Pratiques](owl_components/best_practices.md)
- Pas de `constructor` (utiliser `setup`).
- Conventions de nommage (`addon.Component`).
- Conformité ES2019.

### 4. [Hooks & Réactivité](../hooks/index.md)
*(Voir la section dédiée Hooks)*
- `useODooEnv`, `useService`
- `onWillStart`, `onMounted`
- `useRef`, `useState`

## Snippet Rapide

```javascript
/* @odoo-module */
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class MyCounter extends Component {
    static template = "my_module.MyCounter";
    setup() {
        this.state = useState({ count: 0 });
        this.notification = useService("notification");
    }
    increment() {
        this.state.count++;
        this.notification.add("Compteur incrémenté !", { type: "info" });
    }
}

registry.category("actions").add("my_module.action_counter", MyCounter);
```
