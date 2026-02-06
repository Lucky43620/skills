# Performance Profiling

Odoo provides an integrated profiling tool to record executed queries and stack traces.

## Enabling the Profiler
1.  **Developer Mode:** Click the "bug" icon and select "Enable profiling".
2.  **Settings:** Go to Settings > Performance to enable globally for a duration.

## Collectors
The profiler uses collectors to gather data:
*   **SQL Collector:** Records all executed SQL queries.
*   **Periodic Collector:** Samples the stack trace periodically (CPU usage).
*   **QWeb Collector:** Tracks QWeb rendering time.

## Analysis
Results can be inspected in the backend using the **Speedscope** integration (Flamegraph view) or exported to JSON for external analysis.

## Flame Graphs
Use flame graphs to identify "hot paths"—functions that consume the most time (width of the bar). Look for deep stacks that shouldn't be deep, or wide bars that indicate slow single functions.
