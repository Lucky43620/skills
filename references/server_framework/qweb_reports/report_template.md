# QWeb Report Templates

Reports in Odoo are web pages generated using QWeb templates.

## Standard Variables

Report templates always provide the following variables:
*   `docs`: Records for the current report (iterable).
*   `doc_ids`: List of IDs for the docs records.
*   `doc_model`: Model for the docs records.
*   `time`: Python `time` module.
*   `user`: `res.users` record for the user printing the report.
*   `res_company`: Record for the current user’s company.
*   `web_base_url`: The base URL for the webserver.
*   `context_timestamp`: Function converting UTC datetime to user's timezone.

## Minimal Viable Template

```xml
<template id="report_invoice">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <h2>Report title</h2>
                    <p>This object's name is <span t-field="o.name"/></p>
                </div>
            </t>
        </t>
    </t>
</template>
```

*   `web.html_container`: Necessary root layout.
*   `web.external_layout`: Adds default header/footer (company logo, etc.).
*   `class="page"`: The content inside this div defines the PDF body.

## Translatable Templates

To translate reports (e.g., to the customer's language), use a sub-template method:

1.  **Main Template:** Iterates over docs and calls the document template with `t-lang`.
2.  **Document Template:** Renders the single record.

```xml
<!-- Main Template -->
<template id="report_saleorder">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="doc">
            <t t-call="sale.report_saleorder_document" t-lang="doc.partner_id.lang"/>
        </t>
    </t>
</template>

<!-- Translatable Document Template -->
<template id="report_saleorder_document">
    <t t-set="doc" t-value="doc.with_context(lang=doc.partner_id.lang)" />
    <t t-call="web.external_layout">
        <div class="page">
            <!-- Content -->
        </div>
    </t>
</template>
```
