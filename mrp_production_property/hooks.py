# coding: utf-8
# Copyright 2018 Opener B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, pool):
    """ Add everyone to the properties group by default upon installation
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['sale.config.settings'].create({}).write({'group_mrp_properties': 1})
