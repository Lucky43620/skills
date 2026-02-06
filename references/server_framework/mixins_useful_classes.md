# Server framework — Mixins and Useful Classes

## Quand utiliser
Quand tu utilises des mixins Odoo (messaging/website/others) ou classes utilitaires dans des modules standard.

## Ce que tu dois demander/valider avant de coder
- Version Odoo: 19
- Community/Enterprise (si ça change l’UI/le module)
- Module(s) concernés + dépendances
- Où s’exécute la feature (backend / web / ui / api / cli)
- Contexte fonctionnel (ex: écran, modèle, flux)

## Checklist d’implémentation
1. Localiser les fichiers existants (ou créer un addon minimal).
2. Appliquer le pattern recommandé (ci-dessous).
3. Brancher via `__manifest__.py` (data/assets/depends).
4. Vérifier sécurité/perf si impact.
5. Tester (manuel + test auto si possible).

## Patterns & snippets
- Voir `assets/templates/server/mixin_notes.md`

## Pièges fréquents
- Mélanger concepts backend/frontend (ex: QWeb report vs QWeb template web).
- Oublier de déclarer l’asset ou la vue dans le manifest.
- Oublier droits (access + record rules).
- Patcher au mauvais endroit (JS) ou sur un cycle de vie inadapté.

## Lien doc officielle
https://www.odoo.com/documentation/19.0/fr/developer/reference/backend/mixins.html
