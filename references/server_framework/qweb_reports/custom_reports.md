# Custom Reports

By default, the reporting system passes the records (`docs`) to the template. If you need arbitrary data (e.g., aggregated stats, data from other models), you can define a **Custom Report**.

This is an `AbstractModel` named `report.{module.report_name}`.

```python
from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'report.module.report_name'

    def _get_report_values(self, docids, data=None):
        # get the records selected for this rendering of the report
        docs = self.env['my.model'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': 'my.model',
            'docs': docs,
            'other_data': self._get_stats(),
        }
```

> [!WARNING]
> When using a custom report, the default `docs`, `doc_ids`, and `doc_model` variables are NOT automatically included. You must return them in the dictionary if your template needs them.
