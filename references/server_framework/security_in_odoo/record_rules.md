# Record Rules (`ir.rule`)

Record rules are conditions which must be satisfied in order for an operation to be allowed. They are evaluated record-by-record, following access rights.

*   **Row-Level Security:** Filters specific records a user can see/modify.
*   **Default Allow:** If access rights grant access and *no rule applies* to the operation and model for the user, admission is granted.

## Model Definition

**Fields:**
*   `name`: Description of the rule.
*   `model_id`: The model to which the rule applies.
*   `groups`: `res.groups` to which access is granted/restricted.
    *   If no group is specified, the rule is **Global**.
*   `domain_force`: A Python expression domain.
    *   `['|', ('user_id', '=', user.id), ('user_id', '=', False)]`
*   `perm_read`: Apply rule for Read.
*   `perm_write`: Apply rule for Write.
*   `perm_create`: Apply rule for Create.
*   `perm_unlink`: Apply rule for Delete.

## Domain Variables

The domain evaluation context includes:
*   `user`: The current user (recordset singleton).
*   `time`: Python `time` module.
*   `company_id`: Current user's selected company ID (int).
*   `company_ids`: List of accessible company IDs (list of ints).

## Global vs Group Rules

*   **Global Rules (Intersect/AND):** If two global rules apply, **both** must be satisfied. Adding a global rule always restricts access further.
*   **Group Rules (Unify/OR):** If two group rules apply, **either** can be satisfied. Adding group rules expands access (up to the limit of global rules).
*   **Combination:** Global rules are applied first (AND), then the union of Group rules (OR) is applied within that subset.

**Implication:**
Reading a record requires: `(Global_Rule_1 AND Global_Rule_2) AND (Group_Rule_A OR Group_Rule_B)`

> [!WARNING]
> Creating multiple global rules is risky as it’s possible to create non-overlapping rulesets, which will remove all access.
