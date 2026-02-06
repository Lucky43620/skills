# Data Files (XML & CSV)

Odoo utilise des fichiers de données pour tout : configuration, vues, droits d'accès, données de démonstration.

## 1. Droits d'Accès (`ir.model.access.csv`)

Fichier **obligatoire** pour tout nouveau modèle (sinon erreur de sécurité au chargement).
Doit être dans le dossier `security/` et référencé dans le `__manifest__.py`.

**Structure des colonnes :**
`id`: XML ID unique (ex: `access_my_model_group_user`)
`name`: Nom lisible (ex: `my.model.access.user`)
`model_id:id`: Référence au modèle (ex: `model_my_model`)
`group_id:id`: Groupe autorisé (ex: `base.group_user`). Laisser vide pour "tous les utilisateurs".
`perm_read`: 1/0
`perm_write`: 1/0
`perm_create`: 1/0
`perm_unlink`: 1/0

**Exemple :**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_todo_task_user,todo.task.user,model_todo_task,base.group_user,1,1,1,1
access_todo_task_manager,todo.task.manager,model_todo_task,base.group_system,1,1,1,1
```

## 2. Fichiers XML (`<record>`)

Utilisés pour les vues, les actions, les menus et les données par défaut.

```xml
<odoo>
    <!-- Record standard (Update si existe, Create sinon) -->
    <record id="view_partner_form_inherit" model="ir.ui.view">
        <field name="name">res.partner.form.inherit</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='vat']" position="after">
                <field name="is_company"/>
            </xpath>
        </field>
    </record>

    <!-- Suppression d'un record existant -->
    <delete model="ir.ui.menu" id="module.menu_to_delete"/>

    <!-- Appel de méthode (Function) -->
    <function model="res.users" name="_init_data_method"/>
</odoo>
```

### Attributs Clés
- **`id`** : L'identifiant externe (XML ID). Unique par module.
- **`model`** : Le modèle Odoo cible (ex: `ir.ui.view`, `res.partner`).
- **`noupdate="1"`** : Si présent dans `<odoo noupdate="1">`, les enregistrements ne seront **pas mis à jour** lors des upgrades du module (utile pour la configuration modifiable par l'utilisateur).
- **`forcecreate="0"`** : Ne crée pas l'enregistrement s'il n'existe pas (rare).

## 3. Données de Démo
Placez les fichiers de démo dans la clé `'demo': [...]` du manifest. Ils ne sont chargés que si "Load Demo Data" est coché à la création de la DB.
