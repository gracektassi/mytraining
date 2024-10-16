from odoo import fields
from odoo import models

class RealEstate(models.Model):
    _name="real.estate"
    _description="Test model"
    name=fields.Char(default="House",required=True)
    price=fields.Float()
