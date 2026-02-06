# Introduction (Web Framework)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#introduction

## TL;DR

- Le framework JS Odoo est une **SPA** (Single Page Application) qui tourne dans le navigateur (`/web`).
- Il utilise **Owl** (composants modernes) et des classes natives JS.
- Il gère l'état de l'URL et ne charge que le nécessaire (pas de rechargement complet).
- Utilisé par le backend (web client), le site web (public), et le point de vente (PoS).

## Concepts clés

- **Web Client** : L'application principale (backend) qui gère l'interface utilisateur.
- **Frontend vs Backend** : Dans l'écosystème Odoo, "backend" désigne souvent le Web Client (interface interne) et "frontend" le site web public. Ne pas confondre avec serveur/navigateur.
- **Owl** : Le système de composants actuel (similaire à Vue/React).
- **Widgets** : Terme désignant les anciens composants (Legacy).

## Patterns recommandés

- **Tout nouveau développement doit se faire en Owl.**
- Ne pas confondre les termes : `frontend` = site web, `backend` = interface utilisateur interne, `server` = code python.

## Architecture Globale

Le client web est une enveloppe autour de :
- Une **NavBar**
- Un **ActionContainer** (affiche l'action courante : client action ou vue `act_window`).
- Un **MainComponentsContainer** (pour les composants globaux comme les dialogues, notifications).

La gestion des actions est centrale : le service `action` maintient une pile d'actions (breadcrumbs).
