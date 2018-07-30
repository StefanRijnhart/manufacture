# coding: utf-8
# Copyright 2012 - 2016 Odoo S.A.
# Copyright 2017 Bima Wijaya
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    property_ids = fields.Many2many('mrp.property',
                                    'procurement_property_rel',
                                    'procurement_id', 'property_id',
                                    string='Properties')

    @api.multi
    def _get_matching_bom(self):
        """ Inject property ids in the context, to be honoured in the
        production model's search method """
        return super(ProcurementOrder, self.with_context(
            property_ids=self.property_ids.ids))._get_matching_bom()

    @api.multi
    def make_mo(self):
        """ Pass the properties over to the production order """
        res = super(ProcurementOrder, self).make_mo()
        for procurement_id, produce_id in res.iteritems():
            procurement = self.browse(procurement_id)
            production = self.env['mrp.production'].browse(produce_id)
            production.write({
                'property_ids': [(6, 0, procurement.property_ids.ids)],
            })
        return res
