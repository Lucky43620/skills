# Web Client Architecture

The Web Client is a **Single Page Application (SPA)** driven by Owl.

## Boot Process
1.  **`web.layout` (Controller):** The server renders the initial HTML shell.
2.  **`boot.js`:** Loads assets (bundles) and definitions.
3.  **`WebClient` (Component):** The root Owl component mounts to the DOM.
4.  **Services Start:** Core services (orm, rpc, user, menu) are started asynchronously.
5.  **Action Service:** Loads the default action (e.g. Inbox or Discuss).

## Main Components
*   **NavBar:** The top menu.
*   **ActionContainer:** The main area where views (Kanban, List, Form) are rendered.
*   **MainComponentsContainer:** A portal area for dialogs, notifications, and popups.
