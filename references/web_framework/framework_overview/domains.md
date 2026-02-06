# Domains (JS)

In the web client, domains effectively work like in Python (Polish notation), but they are handled by the `Domain` class provided by `@web/core/domain`.

## Usage
Unlike Python tuples, JS interactions often require constructing explicit `Domain` objects to combine or analyze them.

```javascript
import { Domain } from "@web/core/domain";

const d1 = new Domain([["a", "=", 1]]);
const d2 = new Domain([["b", ">", 2]]);

// Combine (AND)
const d3 = Domain.and([d1, d2]); // [['a','=',1], ['b','>',2]]

// Combine (OR)
const d4 = Domain.or([d1, d2]); // ['|', ['a','=',1], ['b','>',2]]

// Evaluate against a record (local evaluation)
const record = { a: 1, b: 5 };
const matches = d3.contains(record); // true
```

## Parsing
The framework can convert string representations of domains (from XML views) into arrays.
