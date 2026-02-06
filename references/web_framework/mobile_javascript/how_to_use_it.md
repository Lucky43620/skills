# How to use it

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/mobile.html

## TL;DR

- Privilégier des composants adaptatifs et des styles responsives.
- Encapsuler les variations mobile dans un composant ou service dédié.

## Quand l’utiliser

- Quand une interaction doit être simplifiée sur mobile.
- Pour adapter des vues list/form à un écran réduit.

## Concepts clés

- Composants OWL réutilisables.
- Hooks pour suivre l’état UI (scroll, focus, etc.).

## API / Syntaxe

- `Component` OWL + classes CSS conditionnelles.
- `@odoo-module` pour modules JS.

## Patterns recommandés

- Créer un composant `Card` qui s’adapte via props.
- Utiliser une classe `o_mobile_*` pour piloter les styles.

## Anti-patterns & pièges

- Gérer des tailles en JS plutôt que CSS.
- Ajouter des assets mobile dans un bundle backend global.

## Debug & troubleshooting

- Tester le responsive mode du navigateur.
- Vérifier le chargement de `scss` dans le bundle backend.

## Exemples complets

```javascript
// my_module/static/src/js/responsive_card.js
/** @odoo-module **/

import { Component } from "@odoo/owl";

export class ResponsiveCard extends Component {
    static props = { title: String };
}
```

```xml
<!-- my_module/static/src/xml/responsive_card.xml -->
<t t-name="my_module.ResponsiveCard" owl="1">
    <div class="o_responsive_card">
        <h3><t t-esc="props.title"/></h3>
        <t t-slot="default"/>
    </div>
</t>
```

```scss
/* my_module/static/src/scss/responsive_card.scss */
.o_responsive_card {
    padding: 16px;
}
@media (max-width: 768px) {
    .o_responsive_card {
        padding: 8px;
    }
}
```

## Checklist

- [ ] Composant unique avec props adaptatives.
- [ ] Styles responsives dans `scss`.
- [ ] Pas de duplication de logique.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/mobile.html

## Vérifié vs doc

Lien officiel corrigé vers `mobile.html` conformément à la doc Odoo 19.

## Voir aussi

- [Owl components](../owl_components/index.md)
- [Hooks](../hooks/index.md)
- [Assets](../assets/index.md)
