# Search and Read

Retrieve records matching a domain used to filter the requested data.

## Method: `search_read`
A shortcut that performs `search` followed by `read`.

### Signature
`execute_kw(db, uid, password, model, 'search_read', [domain], {'fields': fields_list, 'limit': limit})`

### Arguments
*   `domain`: List of tuples in Polish notation, e.g. `[['is_company', '=', True]]`.
*   `fields`: List of field names to retrieve.
*   `limit`: Max number of records.

### Example
```python
partners = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
    [[['is_company', '=', True]]],
    {'fields': ['name', 'country_id', 'comment'], 'limit': 10}
)
# Returns list of dicts: [{'id': 1, 'name': '...', ...}, ...]
```
