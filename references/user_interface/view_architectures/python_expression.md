# Python Expressions in Views

Odoo views support Python expressions for dynamic behavior, particularly in attributes like `readonly`, `required`, `invisible`, `context`, and `domain`.

## Evaluation Context

Expressions are evaluated in a restricted environment containing:

*   **Field Names:** Access to the current record's field values (e.g., `state == 'draft'`).
*   **`id`:** The ID of the current record (Integer).
*   **`context`:** The current view configuration context (Dictionary).
*   **`uid`:** The current user's ID (Integer).
*   **`user`:** The current user (Recordset).
*   **`parent`:** In sub-views (e.g., One2many lines), refers to the parent record.
*   **`today`:** Current local date string (`YYYY-MM-DD`).
*   **`now`:** Current local datetime string (`YYYY-MM-DD hh:mm:ss`).
*   **`time`:** Python's `time` module.
*   **`datetime`:** Python's `datetime` module.
*   **`relativedelta`:** `dateutil.relativedelta`.

## Domains

Domains are lists of conditions used to filter records.

**Syntax:** `['|', ('field_a', '=', value), ('field_b', '!=', value)]`

*   **Polish Notation:** Operators like `|` (OR) and `!` (NOT) are placed *before* the operands. The default implied operator is AND.
*   **Dynamic Usage:**
    ```xml
    <field name="partner_id" domain="[('customer_rank', '>', 0), ('company_id', '=', parent.company_id)]"/>
    ```

## Context

The context is a dictionary used to pass parameters to views and server actions.

**Common Keys:**
*   `default_{field_name}`: Set default value for creation.
*   `search_default_{filter_name}`: Activate a search filter by default.
*   `group_by`: Set default grouping.
*   `active_id` / `active_ids`: ID of the record calling the action.

**Example:**
```xml
<field name="line_ids" context="{'default_product_id': product_id, 'tree_view_ref': 'my_module.view_line_tree'}"/>
```
