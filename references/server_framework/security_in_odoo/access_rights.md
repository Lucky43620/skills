# Access Rights (ACL)

## TL;DR

- Les ACL (`ir.model.access.csv`) définissent les droits CRUD par modèle et groupe.
- C’est la première couche : sans read, rien n’apparaît.

## Concepts clés

- Colonnes CSV : `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`.
- group_id vide → règle globale pour tous les utilisateurs.

## Patterns recommandés

- Créer des groupes dédiés à ton module si tu dois séparer les rôles.
- Donner le minimum (least privilege) et compléter avec record rules.

## Pièges fréquents

- Oublier une ACL → erreurs d’accès dans l’UI.
- Mettre ACL trop permissives puis tenter de compenser avec des rules complexes.

## Exemples

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_x_user,x user,model_x_model,base.group_user,1,1,1,0
```

## Voir aussi

- `assets/templates/server/ir_model_access.csv`
- record_rules.md
