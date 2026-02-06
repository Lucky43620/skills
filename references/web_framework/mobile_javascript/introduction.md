# Introduction (Mobile JavaScript)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/mobile.html

## TL;DR

- Odoo fournit un cadre pour adapter l’UI et les interactions sur mobile.
- Utilisez les hooks et services existants avant de créer du code spécifique mobile.

## Quand l’utiliser

- Quand une vue doit rester utilisable sur écran réduit.
- Pour ajouter une interaction mobile (gestes, format compact).

## Concepts clés

- Détection d’environnement via services du client.
- Approche progressive : même code, rendu adaptatif.

## API / Syntaxe

- Utiliser les hooks OWL (`useDevice`, `useRef` selon les besoins).
- Styles via SCSS responsive dans `static/src/scss`.

## Patterns recommandés

- Garder la logique dans les services, adapter le rendu via props.
- Utiliser des classes CSS conditionnelles pour mobile.

## Anti-patterns & pièges

- Dupliquer un composant complet pour mobile.
- Ajouter un code spécifique mobile sans fallback desktop.

## Debug & troubleshooting

- Tester en mode responsive du navigateur.
- Vérifier les bundles mobile/desktop pour éviter les collisions CSS.

## Exemples complets

```javascript
// my_module/static/src/js/mobile_card.js
/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class MobileCard extends Component {
    setup() {
        this.state = useState({ compact: true });
    }
}
```

```scss
/* my_module/static/src/scss/mobile_card.scss */
@media (max-width: 768px) {
    .o_mobile_card {
        padding: 8px;
    }
}
```

## Checklist

- [ ] Le rendu s’adapte sans logique dupliquée.
- [ ] Les styles sont responsives.
- [ ] Les tests couvrent desktop et mobile.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/mobile.html

## Vérifié vs doc

La page officielle Odoo 19 renvoie désormais vers `mobile.html` pour cette rubrique, lien mis à jour ici.

## Voir aussi

- [Hooks](../hooks.md)
- [Assets](../assets.md)
- [Owl components](../owl_components.md)
