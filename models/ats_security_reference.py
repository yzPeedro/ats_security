from odoo import fields, models


class AtsSecurityIncidents(models.Model):
    _name = "ats.security.reference"
    _description = "Referência"

    data = fields.Date(string="Data do Escritório", required=True)
    usuario = fields.Many2one(comodel_name="res.users", string="Usuário", readonly=True, default=lambda self: self.env.user, required=True)
