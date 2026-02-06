# Testing JS Code

Frontend testing ensures the web client behaves correctly. Odoo 19 uses a new framework called **Hoot** (built on QUnit concepts).

## Structure
Test files live in `static/tests/` and usually end with `.test.js`.

## Frameworks
*   **Hoot:** The modern runner for Odoo 19.
*   **Web Test Helpers:** Utilities to interact with the DOM (click, fill, etc.).
*   **Mock Server:** Simulates backend responses so JS tests can run without a live Odoo server.

**Example:**
```js
import { test } from '@odoo/hoot';
import { click, contains } from '@odoo/hoot-dom';
import { mockService } from '@web/../test/web_test_helpers';

test('can click button', async () => {
    mockService('rpc', { ... });
    await click('.btn-primary');
    await contains('.success-message');
});
```
