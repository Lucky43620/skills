# Populate (Test Data)

Automatically fills a database with random test data based on models. Useful for performance testing or demos.

## Usage
`./odoo-bin populate -d <database> --model <model_name> --size <size>`

## Options
*   `--model`: Specific model to populate (e.g., `res.partner`). If omitted, populates all.
*   `--size`: `small`, `medium`, `large`. Controls the volume of data.

## Example
```bash
./odoo-bin populate -d mydb --model res.partner --size small
```
