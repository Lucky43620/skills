# Performance Good Practices

## Batch Operations
Always batch operations when working with recordsets. Avoid calling methods that run SQL queries inside a loop.

**Bad:**
```python
for record in self:
    record.count = other_model.search_count([('related_id', '=', record.id)]) # N queries
```

**Good (Read Group):**
```python
counts = other_model.read_group([('related_id', 'in', self.ids)], ['related_id'], ['related_id'])
mapped_data = {c['related_id'][0]: c['related_id_count'] for c in counts}
for record in self:
    record.count = mapped_data.get(record.id, 0) # 1 query
```

**Creation:**
Accumulate values in a list and call `create` once.
```python
vals_list = [{'name': 'foo'}, {'name': 'bar'}]
model.create(vals_list) # 1 query
```

## Reduce Algorithmic Complexity
Avoid nested loops with quadratic complexity O(n^2). Use dictionaries or sets for O(1) lookups.

**Bad:**
```python
for record in self:
    for res in results:
        if res['id'] == record.id: ...
```

**Good:**
```python
results_map = {res['id']: res for res in results}
for record in self:
    res = results_map.get(record.id) ...
```

## Use Indexes
Add database indexes for fields frequently used in search domains.
```python
name = fields.Char(index=True)
```
*   **Warning:** Do not index *every* field. Indexes slow down Create/Write/Unlink operations.
