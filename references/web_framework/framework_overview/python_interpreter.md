# Python Interpreter in JS

Odoo includes a limited Python interpreter in JavaScript to evaluate domains and simple expressions client-side without a roundtrip to the server.

## Purpose
*   Evaluating `attrs` / `invisible` domains in views dynamically.
*   Calculating simple modifiers.

## Capabilities
It supports a subset of Python syntax:
*   Booleans (`True`, `False`)
*   Lists, Tuples, Dictionaries
*   Comparisons (`==`, `!=`, `in`, `not in`)
*   Basic Math (`+`, `-`, `*`)
*   `context` variable access (e.g. `context.get('default_x')`)

## Limitations
*   No functions definitions.
*   No imports.
*   No complex control flow (loops).

## Usage
Usually transparently handled by the `Domain` class or `Evaluator`.
