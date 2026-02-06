# Recordsets (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/backend/orm.html#recordsets

## Définition
Un **Recordset** est une collection ordonnée d'enregistrements du même modèle.
Même un enregistrement seul (`self.partner_id`) est un recordset de taille 1 (Singleton).

## Opérations sur les Ensembles
Les recordsets supportent les opérations python standards :
- **Union**: `res = r1 | r2`
- **Intersection**: `res = r1 & r2`
- **Différence**: `res = r1 - r2`

## Itération
L'itération est standard.
```python
for record in records:
    print(record.name) # record est un Singleton
```

## Singleton
Si un recordset contient exactement 1 enregistrement, on peut accéder directement à ses champs.
`record.name`
Si 0 ou >1 enregistrements -> Erreur (sauf pour comparaison d'égalité).

Pour s'assurer d'avoir un singleton :
`record.ensure_one()` (Lève une erreur si vide ou multiple).

## Cache et Prefetching
Odoo utilise un cache intelligent.
- Accéder à un champ (`rec.name`) charge ce champ pour **tous** les enregistrements du recordset "prefetch" (souvent ceux de la boucle).
- Evite le problème "N+1 queries".

## Méthodes de Recordset (High Level)
- `ids`: Liste des IDs Python (`[1, 2, 3]`).
- `env`: Accès à l'environnement (`self.env`).
- `exists()`: Retourne un sous-ensemble des enregistrements qui existent encore en DB.
- `sudo()`: Retourne une copie du recordset avec droits admin (ou autre user).
- `with_context(**kwargs)`: Retourne une copie avec un contexte modifié.
- `with_company(company)`: Retourne une copie avec le contexte de société forcé.
