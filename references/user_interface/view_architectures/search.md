# Search View Architecture

Search views are used to filter another view's content (usually aggregated views like List, Kanban, or Graph). They do not display data themselves but define the search options available in the Control Panel.

The root element is `<search>`.

```xml
<search>
    ...
</search>
```

## Components

### `<field>`

Defines fields that can be searched. When a user types in the search box, these fields are suggested.

**Attributes:**

*   `name` (Mandatory): The field to filter on.
*   `string`: Label.
*   `operator`: Override default operator (e.g., `operator="child_of"` for hierarchical search).
*   `filter_domain`: A Python expression returning a domain. Uses `self` as the user input value. Use this for flexible searches.
    *   Example: `filter_domain="['|', ('name', 'ilike', self), ('email', 'ilike', self)]"`
*   `context`: Context to pass.
*   `domain`: Domain to force (rarely used directly on field).
*   `groups`: Visibility by user group.

### `<filter>`

Creates pre-defined filters that users can toggle.

**Attributes:**

*   `name` (Mandatory): Technical name (used for `search_default_...`).
*   `string`: UI Label.
*   `domain`: The domain to apply when the filter is active.
    *   Example: `domain="[('state', '=', 'draft')]"`
*   `context`: Context to apply. Often used for **Group By**.
    *   Example: `context="{'group_by': 'partner_id'}"`
*   `date`: For Date/Datetime fields, creates a set of time-based filters (Month, Quarter, Year).
    *   Example: `date="create_date" string="Creation Date"`
*   `invisible`: Visibility condition.

### `<separator>`

Separates groups of filters. Filters separated by a `<separator/>` use **OR** logic between the groups (within a group, filters use **OR** logic if they are selected together, but across separators, it behaves like OR? No, Odoo default is AND between different fields/types, but OR between filters of the same "type" or separated by separator?
*Correction*:
*   Filters *without* a separator between them are usually treated as "OR" (inclusive) if they are just simple domain filters.
*   Wait, the documentation says: "Sequences of filters (without non-filters elements separating them) are treated as inclusively composited: they will be composed with OR rather than the usual AND."
*   So `<filter A/> <filter B/>` -> A OR B.
*   `<filter A/> <separator/> <filter B/>` -> A AND B.

### `<group>`

Used to group custom filters or Group By options visually in the "Group By" menu or "Filter" menu (less common for simple filters, more for layout).

For "Group By", it's common to put them in a `<group expand="0" string="Group By">` container.

### `<searchpanel>`

Displays a panel on the left side of the view for quick filtering.

```xml
<searchpanel>
    <field name="department_id" icon="fa-building"/>
    <field name="state" select="multi" icon="fa-tags"/>
</searchpanel>
```

**Attributes:**
*   `view_types`: Comma-separated list of view types where this panel is visible (e.g., `view_types="list,kanban"`).

**Child `<field>` Attributes:**
*   `name`: Field to filter by.
*   `select`: `one` (radio buttons) or `multi` (checkboxes).
*   `icon`: Icon for the section.
*   `enable_counters`: Show record counts.

## Search Defaults

You can activate filters by default using the action's context.

Key format: `search_default_{filter_name}`

*   Value: `1` (or `True`) to activate.
*   For fields (less common): The value to search for.

Example in Action:
```python
'context': {'search_default_my_filter': 1, 'search_default_group_by_stage': 1}
```
