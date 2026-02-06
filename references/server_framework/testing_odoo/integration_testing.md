# Integration Testing (Tours)

Tours are integration tests that verify that the Python backend and JavaScript frontend work together. A tour is a scenario of steps (clicks, inputs) executed by a headless browser (PhantomJS/Chrome).

## Structure
Located in `static/tests/tours/`.

**File `your_tour.js`:**
```js
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add('my_tour', {
    test: true,
    url: '/odoo',
    steps: () => [
        {
            content: "Click on the App",
            trigger: '.o_app[data-menu-xmlid="my_module.menu_root"]',
            run: "click",
        },
        {
            content: "Check result",
            trigger: '.o_kanban_view',
        },
    ]
});
```

## Running Tours
Tours are run from a Python test case using `HttpCase`.

```python
from odoo.tests.common import HttpCase

class TestMyTour(HttpCase):
    def test_tour(self):
        self.start_tour("/web", 'my_tour', login="admin")
```
