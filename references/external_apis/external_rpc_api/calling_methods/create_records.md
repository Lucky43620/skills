# Create Records

Create new records in the database.

## Method: `create`

### Signature
`execute_kw(db, uid, password, model, 'create', [values_list])`

### Arguments
*   `values_list`: A list of dictionaries, where each dictionary creates one record.
    *   **Pro Tip:** Passing a single dictionary inside a list is also supported (creates 1 record).
    *   **Pro Tip:** Batch creation (list of dicts) is much faster than loop creation.

### Example
```python
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner",
    'email': "new@example.com",
}])
```

### Return
*   Returns the ID (int) of the created record (or list of IDs if batch create).
