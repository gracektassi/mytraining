
from odoo import fields,models

class EstateMixin(models.Model):
    _name="estate.mixin"

    name = fields.Char("Name", required=True)
    