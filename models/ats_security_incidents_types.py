from odoo import fields, models


class AtsSecurityIncidentsTypes(models.Model):
    _name = "ats.security.incidents.types"
    _description = "Tipos de incidentes"

    name = fields.Char(string="Tipo do incidente", required=True)
