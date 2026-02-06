# Security Pitfalls

As a developer, it is important to understand the security mechanisms and avoid common mistakes.

## Unsafe Public Methods

Any public method (not starting with `_`) can be executed via an RPC call.

*   **Untrusted Context:** On public methods, the record set (`self`) and parameters cannot be trusted.
*   **No Implicit Checks:** ACLs are only verified during CRUD operations, not arbitrary method calls.

**Bad Practice:**
```python
def action_done(self):
    # DANGEROUS: Anyone can call this on any record!
    self.write({'state': 'done'})
```

**Good Practice:**
```python
def action_done(self):
    # Check business logic or groups explicitely if needed
    if not self.env.user.has_group('my_module.group_manager'):
        raise AccessError("Not allowed")
    self.write({'state': 'done'})
```

## Bypassing the ORM

Using `self.env.cr.execute` directly bypasses all ORM features: translations, field invalidation, **access rights**, and record rules.

**SQL Injections:**
Never use Python string concatenation (`+`) or interpolation (`%`) to pass variables to a SQL query string.

**Bad:**
```python
self.env.cr.execute("SELECT id FROM table WHERE name = '" + name + "'")
```

**Good:**
```python
self.env.cr.execute("SELECT id FROM table WHERE name = %s", (name,))
```
