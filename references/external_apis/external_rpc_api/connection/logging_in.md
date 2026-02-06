# Logging In

To perform operations, you must first authenticate to get a User ID (`uid`).

## Authenticate
**Method:** `authenticate`
**Service:** `common`

### Arguments
1.  `db` (string): Database name.
2.  `login` (string): User login (email).
3.  `password` (string): User password or **API Key** (recommended).
4.  `user_agent_env` (dict): Empty dictionary `{}`.

### Return
*   **Integer:** The User ID (`uid`) if successful.
*   **False:** If authentication fails.

### Example (Python)
```python
uid = common.authenticate(db, username, password, {})
if not uid:
    print("Auth failed via XMLRPC")
```
