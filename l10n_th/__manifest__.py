# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Thailand - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
Chart of Accounts for Thailand.
===============================

Thai accounting chart and localization.
    """,
    'author': 'Amacom ,Thai Odoo Comumnity Association',
    'website': 'http://thaiodoo.org/',
    'depends': ['account'],
    'data': [
        'data/l10n_th_chart_data.xml',
        'data/account_chart_template_data.yml',
    ],
}
