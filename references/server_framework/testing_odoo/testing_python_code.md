# Testing Python Code

Odoo uses Python's `unittest` library. Tests should be located in a `tests/` package within your module and imported in `tests/__init__.py`.

## Test Classes

### `TransactionCase`
*   **Behavior:** Runs each test method in a **single transaction**.
*   **Role:** The transaction is rolled back after each test method.
*   **Setup:** Use `setUpClass` for common data setup (runs once per class).
*   **Best for:** Standard backend tests.

```python
from odoo.tests.common import TransactionCase

class TestMyModel(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.record = cls.env['my.model'].create({'name': 'Test'})

    def test_creation(self):
        self.assertEqual(self.record.name, 'Test')
```

### `SingleTransactionCase`
*   **Behavior:** All test methods run in the **same transaction**.
*   **Role:** Started at the first test, rolled back at the very end.
*   **Best for:** Complex scenarios where state persistence between methods is desired (less common).

### `SavepointCase` (Deprecated in favor of TransactionCase)
*   Historically used for speed (one transaction with savepoints), but `TransactionCase` is now the standard.

## Running Tests
Tests are run using the `--test-enable` (or `-d and -i`) flags.
`odoo-bin -c odoo.conf -d mydb -i my_module --test-enable --stop-after-init`
