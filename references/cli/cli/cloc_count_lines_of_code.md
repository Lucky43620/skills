# Cloc (Count Lines of Code)

Odoo includes a tool to count the lines of custom code in a database. This is used for Odoo.sh or Enterprise licensing calculations.

## Usage
`./odoo-bin cloc -d <database_name>`
`./odoo-bin cloc -p <path_to_module>`

## Rules
*   **Excluded:** Empty lines, comments, standard Odoo modules, manifest files.
*   **Included:** Python, JS, XML, CSS/SCSS in custom addons.

## Output
It prints a breakdown of lines by type (Python, XML, JS) and a total.
