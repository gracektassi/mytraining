# -*- coding: utf-8 -*-

from odoo import fields, models


class EstateTag(models.Model):

    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _inherit="estate.mixin"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name should be unique"),
    ] 


    color = fields.Integer("Color Index")
