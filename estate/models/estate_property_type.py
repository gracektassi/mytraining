
from odoo import api, fields, models


class EstatePropertyType(models.Model):

 
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]


    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=1)

    
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")


    offer_count = fields.Integer(string="Offers Count")
    offer_ids = fields.Many2many("estate.property.offer", string="Offers")


    property_count=fields.Integer(compute="_compute_property_count")

    @api.depends("property_ids")
    def _compute_property_count(self):
        for rec in self:
            rec.property_count=len(rec.property_ids)


    def action_open_property_ids(self):

        return {
            "name":"Related Props",
            "type":"ir.actions.act_window",
            "view_mode":"tree,form",
            "res_model":"estate.property",
            "target":"current",
            "domain":[("property_type_id","=",self.id)],
            "context":{
                "default_property_type_id":self.id
            }

        }
