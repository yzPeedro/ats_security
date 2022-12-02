from odoo import fields, models


class AtsSecurityIncidents(models.Model):
    _name = "ats.security.reference"
    _description = "Office Date Reference"

    office_date = fields.Date(string="Office Date", required=True)
    username = fields.Many2one(comodel_name="res.users", string="Username", readonly=True, default=lambda self: self.env.user, required=True)
