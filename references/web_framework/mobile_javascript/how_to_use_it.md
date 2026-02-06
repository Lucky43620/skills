# How to Use It (Mobile)

To interact with mobile features, use the `mobile` service or `browser` methods.

## Scanning Barcodes
```javascript
const mobile = useService("mobile");
if (mobile.methods.scanBarcode) {
    const code = await mobile.methods.scanBarcode();
}
```

## Vibrate
```javascript
import { browser } from "@web/core/browser/browser";
// Uses HTML5 Vibration API, mapped to native by the app
browser.navigator.vibrate(200); 
```

## Back Button
You can listen to the hardware back button (Android):
```javascript
import { useBackButon } from "@web/core/utils/hooks";

useBackButon(() => {
    this.closeDialog();
});
```
