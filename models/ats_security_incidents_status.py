from odoo import fields, models


class AtsSecurityIncidentsLevels(models.Model):
    _name = "ats.security.incidents.status"
    _description = "Status de incidentes"

    name = fields.Char(string="Status de incidente", required=True)
