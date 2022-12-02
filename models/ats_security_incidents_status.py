from odoo import fields, models


class AtsSecurityIncidentsLevels(models.Model):
    _name = "ats.security.incidents.status"
    _description = "Incident Status"

    name = fields.Char(string="Incident Status", required=True)
