# Session (JS)

The `session` object contains the initial state of the Odoo instance loaded at boot time.

## Contents
*   `uid`: Current user ID.
*   `server_version`: Odoo version string.
*   `user_context`: Default context.
*   `company_id`: Current active company.
*   `currencies`: Format definitions for currencies.

## Direct Access
The session is globally available via `odoo.session` (deprecated approach) or injected into the `user` service.
**Best Practice:** Use the `user` service or `company` service instead of accessing `session` directly.
