from odoo import fields, models


class AtsSecurityIncidentsLevels(models.Model):
    _name = "ats.security.incidents.levels"
    _description = "Níveis de incidentes"

    name = fields.Char(string="Nível de incidente", required=True)



