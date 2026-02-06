# Using Owl Components

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/owl_components.html#using-owl-components

## TL;DR

Odoo utilise Owl (Odoo Web Library). Les composants sont des classes étendant `Component`.
Le template XML doit être défini séparément (pour la traduction) et référencé via `static template`.

## Structure Standard

**mon_composant.js**
```javascript
import { Component, useState } from "@odoo/owl";

export class MyComponent extends Component {
    static template = "my_addon.MyComponent";

    setup() {
        this.state = useState({ value: 1 });
    }

    increment() {
        this.state.value++;
    }
}
```

**mon_composant.xml**
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<templates xml:space="preserve">
    <t t-name="my_addon.MyComponent">
        <div t-on-click="increment">
            <t t-esc="state.value"/>
        </div>
    </t>
</templates>
```

## Convention de Nommage
Les noms de templates doivent suivre le format : `nom_addon.NomComposant`.
Exemple : `account.AgedReceivable`.

## Assets
Odoo charge automatiquement les fichiers JS/XML s'ils sont dans le bon bundle (souvent `web.assets_backend`).
