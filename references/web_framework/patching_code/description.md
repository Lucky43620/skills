# Patching Code

Odoo allows you to modify existing JavaScript logic without replacing file contents, using a specialized `patch` utility. This is the JS equivalent of `super()` in Python.

## The `patch` Utility
Import it from `@web/core/utils/patch`.

```javascript
import { patch } from "@web/core/utils/patch";
```

## How it works
Patches are applied in the order modules are loaded.
When you call `super.method()`, it calls the implementation from the previous patch (or the original method).

## Unpatching
Every patch function returns an `unpatch` callback, mostly used in testing to clean up side effects.
