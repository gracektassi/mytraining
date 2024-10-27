# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):

    _inherit = "res.users"


  
    property_ids = fields.One2many(
        "estate.property", "user_id", string="Properties", domain=[("state", "in", ["new","sold", "offer_received"])]
    )
    property_ids2 = fields.One2many(
        "estate.property", "user_id", string="Properties2", domain=[("state", "in", ["new","sold", "offer_received"])]
    )
