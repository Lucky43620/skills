# How does it work

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/mobile.html

## TL;DR

- Le web client expose des signaux d’environnement pour ajuster l’UI mobile.
- Les composants OWL réagissent via state/props et styles responsives.

## Quand l’utiliser

- Pour comprendre le flux d’adaptation du web client.
- Avant d’introduire un comportement conditionnel mobile.

## Concepts clés

- État UI piloté par `env` et services.
- Adaptation par CSS/SCSS plutôt que logique JS lourde.

## API / Syntaxe

- Utiliser les services existants (`ui`, `action`, `notification`).
- Ajouter des classes conditionnelles selon l’état.

## Patterns recommandés

- Gérer la logique de rendu dans un composant, pas dans un patch global.
- Réutiliser les templates QWeb existants avec des variantes CSS.

## Anti-patterns & pièges

- Forcer un reflow permanent en JS.
- Implémenter un “mode mobile” parallèle complet.

## Debug & troubleshooting

- Inspecter le DOM pour vérifier l’application des classes.
- Vérifier les media queries effectives.

## Exemples complets

```xml
<!-- my_module/static/src/xml/mobile_toggle.xml -->
<t t-name="my_module.MobileToggle" owl="1">
    <div t-att-class="state.compact ? 'o_mobile_compact' : ''">
        <t t-esc="props.label"/>
    </div>
</t>
```

```javascript
// my_module/static/src/js/mobile_toggle.js
/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class MobileToggle extends Component {
    setup() {
        this.state = useState({ compact: true });
    }
}
```

## Checklist

- [ ] La logique est localisée dans un composant.
- [ ] Les styles s’appuient sur des media queries.
- [ ] Pas de duplication de vues.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/mobile.html

## Vérifié vs doc

Lien officiel ajusté vers `mobile.html`, page cible indiquée par la doc Odoo 19.

## Voir aussi

- [QWeb templates](../qweb_templates/index.md)
- [Owl components](../owl_components/index.md)
- [Assets](../assets/index.md)
