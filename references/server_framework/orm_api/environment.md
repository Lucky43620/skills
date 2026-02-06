# Environment (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/backend/orm.html#environment

## Définition
L'Environnement (`env`) stocke le contexte d'exécution :
- Utilisateur courant (`user`, `uid`).
- Curseur de base de données (`cr`).
- Contexte (`context`: langue, timezone, filtres...).
- Société active (`company`).

## Accès
Disponible sur tout recordset : `self.env`.

## Attributs
- `env.cr`: Le curseur (pour requêtes SQL directes `env.cr.execute(...)`).
- `env.uid`: ID de l'utilisateur courant.
- `env.user`: Recordset de l'utilisateur courant (`res.users`).
- `env.context`: Dictionnaire immuable (FrozenDict).
- `env.company`: Société active (Singleton `res.company`).
- `env.companies`: Sociétés activées (Recordset `res.company`).
- `env.lang`: Code langue courant (ex: `fr_FR`).

## Accès au Registre
`env['res.partner']` retourne un recordset vide du modèle `res.partner`.
C'est le point d'entrée pour les méthodes de recherche :
```python
partners = self.env['res.partner'].search([])
```

## Raccourcis Utiles
- `env.ref('module.xml_id')`: Retourne l'enregistrement correspondant à l'ID XML.
- `env.is_superuser()`: Vrai si mode superuser.
- `env.is_admin()`: Vrai si groupe Administration.
- `env.is_system()`: Vrai si groupe Settings.

## Modification de l'Environnement
Les recordsets sont immuables, mais on peut en créer des variants avec un environnement modifié :

### `with_context(**kargs)`
```python
# Ajoute/Modifie une clé de contexte
new_records = records.with_context(lang='en_US')
```

### `sudo()`
```python
# Passe en mode superuser (bypasse les droits d'accès et règles d'enregistrement)
admin_records = records.sudo()
```

### `with_company(company)`
```python
# Force la société active (pour règles multi-sociétés)
company_records = records.with_company(my_company)
```

### `with_user(user)`
```python
# Change l'utilisateur courant
other_user_records = records.with_user(other_user)
```
