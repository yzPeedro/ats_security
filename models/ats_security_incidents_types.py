from odoo import fields, models


class AtsSecurityIncidentsTypes(models.Model):
    _name = "ats.security.incidents.types"
    _description = "Incidents Types"

    name = fields.Char(string="Incidents Type", required=True)
