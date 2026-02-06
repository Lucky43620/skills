# How it Works (Mobile)

The Mobile App injects a special Javascript object `window.odoo.native_bridge` into the WebView.

## The Bridge
When the Odoo Web Client starts, specific services (like `mobile`) detect this bridge.
They override standard web behaviors (like `notification.add`) to use native device APIs instead.

## Offline Mode
The mobile app also manages a local database/cache to support limited offline capabilities, syncing `web_offline` actions when connectivity returns.
