# Field Access

An ORM field can have a `groups` attribute providing a list of groups (as a comma-separated string of XMLIDs).

```python
secret_code = fields.Char(groups="base.group_system")
```

If the current user is not in one of the listed groups:
1.  **Views:** Restricted fields are automatically removed from requested views.
2.  **Introspection:** Restricted fields are removed from `fields_get()` responses.
3.  **Access:** Attempts to explicitly read or write to restricted fields result in an Access Error in the ORM.
