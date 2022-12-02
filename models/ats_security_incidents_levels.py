from odoo import fields, models


class AtsSecurityIncidentsLevels(models.Model):
    _name = "ats.security.incidents.levels"
    _description = "Incident levels"

    name = fields.Char(string="Incident Level", required=True)



