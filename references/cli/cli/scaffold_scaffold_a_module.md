# Scaffold

Generates a new module directory structure with boilerplate code.

## Usage
`./odoo-bin scaffold <module_name> <destination_directory>`

## Example
```bash
# Create a module named 'my_addon' in the 'custom_addons' folder
./odoo-bin scaffold my_addon custom_addons/
```

## Generated Structure
```
my_addon/
├── __init__.py
├── __manifest__.py
├── controllers/
├── demo/
├── models/
├── security/
└── views/
```
