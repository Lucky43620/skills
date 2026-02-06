# Controllers (Web Controllers)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/http.html

## TL;DR

- Les controllers exposent des routes HTTP via `@http.route`.
- Types courants : `http` (HTML/texte) et `jsonrpc` (RPC JSON-RPC 2 over HTTP).

## Concepts clés

- Paramètres route : path, type, auth (public/user), methods, csrf, website.
- `request` donne accès à env/params/session.

## Patterns recommandés

- Limiter les routes publiques; valider entrées; éviter de renvoyer des données sensibles.
- Pour API : préférer `type='jsonrpc'` + format stable.

## Pièges fréquents

- Exposer des méthodes de modèle via controller sans ACL.
- Oublier CSRF pour routes `http` qui modifient des données.

## Exemples

```python
from odoo import http
from odoo.http import request

class MyController(http.Controller):

  @http.route('/my/page', type='http', auth='user')
  def page(self, **kw):
    return request.render('my_addon.template', {})
```

## Voir aussi

- `assets/templates/server/controller_http.py`
- `assets/templates/server/controller_jsonrpc.py`
