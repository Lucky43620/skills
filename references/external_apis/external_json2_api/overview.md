# External JSON-2 API — Overview

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/external_api.html

## TL;DR

- Nouveau en v19 : endpoint `/json/2` pour interagir avec des modèles Odoo via HTTP.
- Les modèles/champs/méthodes disponibles dépendent de la base et sont consultables via une page `/doc`.

## Concepts clés

- Approche orientée intégration (moins de friction que XML-RPC/JSON-RPC historique).
- Gestion des droits : API key, ACL, record rules.

## Patterns recommandés

- Créer un utilisateur “intégration” avec droits minimaux.
- Limiter aux modèles nécessaires, ajouter record rules spécifiques si besoin.

## Pièges fréquents

- Donner des droits trop larges à l’utilisateur API.
- Supposer que toutes les méthodes sont exposées (dépend du serveur et de la conf).

## Exemples

```bash
# Exemple pseudo (à adapter selon doc)
curl -X POST https://<host>/json/2 -H 'Content-Type: application/json' -d '{...}'
```
