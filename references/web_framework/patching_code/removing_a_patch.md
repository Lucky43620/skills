# Removing a Patch

When you call `patch()`, it returns an `unpatch` function.

## Usage
Checking code to test that patches can be removed.

```javascript
import { patch } from "@web/core/utils/patch";
import { MyClass } from "./my_class";

// Apply patch
const unpatch = patch(MyClass.prototype, {
    getValue() { return 100; }
});

console.log(new MyClass().getValue()); // 100

// Remove patch
unpatch();

console.log(new MyClass().getValue()); // Original value
```

## Why?
This is critical for **Unit Testing**. Tests often patch components to mock behavior. If they don't unpatch in `teardown()`, the mock leaks into other tests, causing random failures.
