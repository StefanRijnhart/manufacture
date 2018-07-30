# coding: utf-8
# Copyright 2012-2016 Odoo S.A.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': "MRP Production Properties",
    'summary': 'Control BoM selection from properties on sale order lines',
    'version': '10.0.1.0.0',
    'category': 'Manufacturing',
    'author': "Odoo S.A.,Odoo Community Association (OCA)",
    'website': 'https://github.com/oca/manufacture',
    'license': 'LGPL-3',
    'depends': [
        'sale_mrp',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_view.xml',
    ],
    'installable': True,
    'post_init_hook': 'post_init_hook',
}
