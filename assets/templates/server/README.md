# Templates Server (Odoo v19)

Snippets serveur prêts à copier pour ORM, actions, contrôleurs, sécurité et rapports.

## Comment les utiliser
1) Copiez le fichier dans votre module (chemin dans le snippet). 
2) Ajoutez les XML/CSV dans la clé `data` du `__manifest__.py`. 
3) Redémarrez le serveur et mettez à jour le module. 

## Fichiers clés
- `orm_model.py` / `orm_constraints.py` : modèles, champs, contraintes. 
- `action_window.xml`, `action_server.xml`, `action_report.xml`, `action_url.xml` : actions. 
- `controller_http.py`, `controller_json.py`, `controller_jsonrpc.py` : contrôleurs. 
- `ir_model_access.csv`, `record_rules.xml` : sécurité. 
- `report_template.xml`, `report_action.xml` : QWeb report minimal. 

## Bonnes pratiques
- Utiliser `ensure_one()` et les recordsets multi. 
- Sécuriser avec ACL + record rules. 
- Garder les actions et rapports déclarés en XML versionnés. 
