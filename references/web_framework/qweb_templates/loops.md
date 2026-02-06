# Loops (QWeb)

## `t-foreach`
Iterates over a list, recordset, or object.

### Syntax
*   `t-foreach`: The collection to iterate.
*   `t-as`: The name of the variable for the current item.

```xml
<t t-foreach="[1, 2, 3]" t-as="i">
    <p>Number: <t t-out="i"/></p>
</t>
```

### Key Helpers
Inside the loop, extra variables are available (prefixed by the `t-as` name):
*   `i_index`: 0-based index of the iteration.
*   `i_first`: True if this is the first item.
*   `i_last`: True if this is the last item.
*   `i_size`: Total size of the collection.
*   `i_parity`: 'odd' or 'even'.

### Example with Helpers
```xml
<tr t-foreach="lines" t-as="line" t-att-class="line_parity">
    <td><t t-out="line_index + 1"/></td>
    <td><t t-out="line.name"/></td>
</tr>
```
