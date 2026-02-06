# Access Rights (`ir.model.access`)

Access rights grant access to an entire model for a given set of operations.

*   **Additive Rights:** A user’s accesses are the union of the accesses they get through all their groups.
*   **Default Deny:** If no access rights match an operation on a model for a user (through their group), the user doesn’t have access.

## Model Definition

The `ir.model.access` model allows defining these rights.

**Fields:**
*   `name`: The purpose or role of the group (e.g., "account.move.line.read.group").
*   `model_id`: The model whose access the ACL controls.
*   `group_id`: The `res.groups` to which the accesses are granted.
    *   Empty `group_id` means the ACL is granted to **every user** (including portal/public).
*   `perm_read`: Allow read access.
*   `perm_write`: Allow write access.
*   `perm_create`: Allow create access.
*   `perm_unlink`: Allow unlink (delete) access.

These flags are all unset (False) by default.

## CSV File Definition

Access rights are typically defined in a `ir.model.access.csv` file in the module's `security/` folder.

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,1,1,1
access_my_model_manager,my.model.manager,model_my_model,base.group_system,1,1,1,1
```
