# Views (JS Reference)

In the frontend, a "View" is the combination of:
1.  **Controller:** Handles logic (search, paging, buttons).
2.  **Renderer:** Displays the data (table, cards).
3.  **Model:** Manages the state (loading data from server).
4.  **Arch Parser:** Parses the XML architecture.

## Standard Views
*   **List:** `ListController`, `ListRenderer`.
*   **Form:** `FormController`, `FormRenderer`.
*   **Kanban:** `KanbanController`, `KanbanRenderer`.

## Registry
Views are registered in `registry.category("views")`.
