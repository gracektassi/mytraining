from odoo import fields, models

class estate_property(models.Model):
    _name="estate.property"
    _description="Test model"
    name=fields.Char(default="House",required=True)
    description=fields.Text()
    postcode=fields.Char()
    data_availability=fields.Float()
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedroom=fields.Integer()
    living_area=fields.Float()
    facades=fields.Float()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection("North")
