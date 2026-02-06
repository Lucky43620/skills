# Models (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/backend/orm.html#models

## AbstractModel
`odoo.models.AbstractModel`
Modèle abstrait utilisé pour partager du comportement. Ne crée pas de table en base.
Souvent utilisé pour les Mixins (ex: `mail.thread`, `image.mixin`).

```python
class MyMixin(models.AbstractModel):
    _name = 'my.mixin'
    _description = 'Description du Mixin'
```

## Model
`odoo.models.Model`
Modèle persistant standard. Crée une table en base (sauf si `_auto = False`).

```python
class MyModel(models.Model):
    _name = 'my.model'
    _description = 'Mon Modèle'
    _order = 'date desc, id'
```

### Attributs Clés
- `_name` (str): Identifiant unique (ex: `res.partner`). Requis.
- `_description` (str): Label convivial.
- `_inherit` (str/list): Modèle(s) parent(s) pour héritage/extension.
- `_rec_name` (str): Champ utilisé pour l'affichage (défaut: `name`).
- `_order` (str): Ordre de tri par défaut (défaut: `id`).
- `_check_company_auto` (bool): Active la validation multi-société automatique.
- `_sql_constraints` (list): Contraintes SQL [(name, sql_def, message)].

## TransientModel
`odoo.models.TransientModel`
Modèle temporaire (Wizards).
- Données nettoyées périodiquement.
- Pas de droits d'accès stricts requis (souvent accessible à tous les utilisateurs internes).
- Idéal pour les pop-ups de configuration ou d'action.

```python
class MyWizard(models.TransientModel):
    _name = 'my.wizard'
```

## Héritage

### Classique (`_name` + `_inherit`)
Crée une nouvelle table copiant la structure du parent.
Semblable à l'héritage objet.

### Extension (`_inherit` sans `_name`)
Modifie le modèle existant "en place".
Ajoute des champs ou surcharge des méthodes sur le modèle d'origine.
C'est le mécanisme standard pour personnaliser Odoo.

### Délégation (`_inherits`)
Héritage multiple par délégation (rarement utilisé directement, préférez `delegate=True` sur Many2one).
Chaque enregistrement est lié à un enregistrement du parent.
