# Mobile Javascript

Odoo's Mobile App is a wrapper around the Web Client, but it exposes native device capabilities (Camera, GPS, Vibration) via a "Bridge".

## The Bridge
The variable `odoo.browser` or specific services detect if the code is running in a mobile app native context.

## Determining Environment
To check if you are on mobile:

```javascript
import { isMobileOS } from "@web/core/browser/feature_detection";

if (isMobileOS()) {
    // We are on Android or iOS
}
```

## Features
*   **Camera:** Scan barcodes.
*   **Geolocation:** Background tracking (Enterprise).
*   **Push Notifications:** Native alerts.
