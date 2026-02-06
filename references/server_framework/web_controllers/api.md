# API (Web Controllers)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/http.html

## TL;DR

- Odoo implémente JSON-RPC 2 over HTTP (avec spécificités).
- Le routing utilise le path HTTP; le champ `method` JSON-RPC est ignoré.

## Concepts clés

- Payload JSON-RPC : id/jsonrpc/method/params (selon implémentation).
- Authentification via session / user (selon auth).

## Pièges fréquents

- Supposer compat parfaite avec spec JSON-RPC (il y a des différences).
