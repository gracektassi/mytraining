from odoo import fields
from odoo import models

class EstateProperty(models.Model):
    _name="estate.property"
    _description="Test model prop"
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")

    def _default_date_availability(self):
        return fields.Date.today()
    
    date_availability = fields.Date("Available From", default=_default_date_availability, copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False, readonly=True)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation=fields.Selection(
        selection=[
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
        ],
        string="Garden Orientation",
    )
    
