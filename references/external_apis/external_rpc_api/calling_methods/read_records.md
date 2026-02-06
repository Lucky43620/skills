# Read Records

Retrieve specific records by their IDs.

## Method: `read`

### Signature
`execute_kw(db, uid, password, model, 'read', [ids], {'fields': fields_list})`

### Example
```python
records = models.execute_kw(db, uid, password, 'res.partner', 'read',
    [[12, 14]], 
    {'fields': ['name', 'email']}
)
```

---

# Update Records (Write)

Update existing records.

## Method: `write`

### Signature
`execute_kw(db, uid, password, model, 'write', [[ids], values])`

### Example
```python
models.execute_kw(db, uid, password, 'res.partner', 'write',
    [[12, 14]],
    {'comment': "Updated via API"}
)
```

---

# Delete Records (Unlink)

Remove records from the database.

## Method: `unlink`

### Signature
`execute_kw(db, uid, password, model, 'unlink', [[ids]])`

### Example
```python
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[14]])
```
