# Actions

Actions define the behavior of the system in response to user interactions: login, button clicks, selection of an item in a menu, etc.

## Window Actions (`ir.actions.act_window`)
The most common action type, used to present visualizations of a model through views.

**Fields:**
*   `res_model`: Model to present views for.
*   `views`: List of `(view_id, view_type)` pairs.
*   `view_mode`: Comma-separated list of view types (e.g., `list,form`).
*   `res_id`: Record ID to load (if default view is form).
*   `target`: `current` (default), `fullscreen`, `new` (dialog), `main`.
*   `context`: Context data to pass.
*   `domain`: Filtering domain.
*   `limit`: Number of records to display (default 80).

**Example:**
```python
{
    "type": "ir.actions.act_window",
    "res_model": "res.partner",
    "views": [[False, "list"], [False, "form"]],
    "domain": [["customer", "=", True]],
}
```

## URL Actions (`ir.actions.act_url`)
Allow opening a URL (website/web page) via an Odoo action.

**Fields:**
*   `url`: The address to open.
*   `target`: `new` (new window), `self` (replace content), `download`.

## Server Actions (`ir.actions.server`)
Trigger complex server code from any valid action location.

**Fields:**
*   `model_id`: Odoo model linked to the action.
*   `state`: Type of server action.
    *   `code`: Execute Python code.
    *   `object_create`: Create a new record.
    *   `object_write`: Update record.
    *   `multi`: Execute several actions.
*   `code`: Python code to execute.

## Report Actions (`ir.actions.report`)
Triggers the printing of a report.

**Fields:**
*   `name`: File name (if `print_report_name` not specified).
*   `model`: Model the report is about.
*   `report_type`: `qweb-pdf` or `qweb-html`.
*   `report_name`: XMLID of the QWeb template.
*   `print_report_name`: Python expression for the filename.
*   `attachment_use`: If `True`, save as attachment.

## Client Actions (`ir.actions.client`)
Triggers an action implemented entirely in the client (e.g., Point of Sale, Kiosk Mode).

**Fields:**
*   `tag`: Client-side identifier (arbitrary string registered in client).
*   `params`: Dictionary of data to send to the client.
*   `target`: `current`, `fullscreen`, `new`, `main`.

## Scheduled Actions (`ir.cron`)
Actions triggered automatically on a predefined frequency.

**Fields:**
*   `name`: Name of the scheduled action.
*   `interval_number`: Number of units between executions.
*   `interval_type`: `minutes`, `hours`, `days`, `weeks`, `months`.
*   `model_id`: Model to call method on.
*   `code`: Code to execute (e.g., `model.method()`).
*   `nextcall`: Next planned execution date.
*   `priority`: Execution priority.
