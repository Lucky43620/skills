# Custom Fonts

To use custom fonts in QWeb reports, you must add the font and related CSS/Less to the `web.reports_assets_common` bundle.

*   Adding to `web.assets_backend` is **NOT** sufficient for reports (wkhtmltopdf needs access).

**Example:**
```xml
<template id="report_assets_common_custom_fonts" inherit_id="web.report_assets_common">
    <xpath expr="." position="inside">
        <link href="/my_module/static/src/less/fonts.less" rel="stylesheet" type="text/less"/>
    </xpath>
</template>
```

**CSS (`fonts.less`):**
```css
@font-face {
    font-family: 'MyFont';
    src: url(/my_module/static/fonts/MyFont.ttf) format('truetype');
}
.my-custom-class {
    font-family: 'MyFont';
}
```
