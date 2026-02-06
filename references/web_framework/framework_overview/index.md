# Web Framework Overview

This section covers the architecture of the Odoo Web Client (the JavaScript frontend).

## Core Concepts
*   **WebClient:** The root component that manages the user interface.
*   **Environment:** The central context containing services and the bus.
*   **Context:** Detailed context for RPC calls (user language, timezone, etc.).
*   **Building Blocks:** Primitive components used throughout Odoo.

## Key Technologies
*   **Owl:** The UI framework (based on React hooks principle).
*   **Modules:** Native ES6 modules.
*   **QWeb:** The templating engine.
