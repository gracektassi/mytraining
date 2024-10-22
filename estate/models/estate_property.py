from dateutil.relativedelta import relativedelta
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero


def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

class EstateProperty(models.Model):
    _name="estate.property"
    _description="Test model prop"
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode") 
    date_availability = fields.Date("Available From", default=_default_date_availability, copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False, readonly=True,default=200)
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
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    active = fields.Boolean("Active", default=True)

    
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one("res.users", string="User", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    total_area = fields.Integer(
        "Total Area ",
        compute="_compute_total_area",
        help="Total area  = the living area + the garden area",
    )


    best_offer = fields.Float("Best Offer", compute="_compute_best_offer", help="Best offer received")


    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area


    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for prop in self:
            prop.best_price = max(prop.offer_ids.mapped("price")) if prop.offer_ids else 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
         for estate in self:
            if not estate.garden:
                 estate.garden_area=0


    
    @api.onchange("date_availability")
    def _onchange_date_availability(self):
        for estate in self:
           return {
         "warning": {
             "title": "Warning",
             "message": "What is this?"
                        }
            }



    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for prop in self:
            if (
                not float_is_zero(prop.selling_price, precision_rounding=0.01)
                and float_compare(prop.selling_price, prop.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! "
                    + "You must reduce the expected price if you want to accept this offer."
                )
