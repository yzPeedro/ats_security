from odoo import fields, models


class AtsSecurityIncidents(models.Model):

    _name = "ats.security.incidents"
    _description = "Segurança"

    data = fields.Date(string="Data do incidente", required=True)
    empresa = fields.Many2one(comodel_name="res.company", string="Empresa", default=lambda self: self.env.user.company_id.id, required=True)
    setor = fields.Many2one(comodel_name="hr.department", string="Setor", required=True)
    funcionario = fields.Many2one(comodel_name="hr.employee", string="Funcionário", required=True)
    tipo_incidente = fields.Many2one(comodel_name="ats.security.incidents.types", string="Tipo do incidente", required=True)
    relato = fields.Text(string="Relato", required=True)
    nivel = fields.Many2one(comodel_name="ats.security.incidents.levels", string="Nível", required=True)
    acao = fields.Many2one(comodel_name="mgmtsystem.action", string="Ação", required=True)
    responsavel = fields.Many2one(comodel_name="hr.employee", string="Responsável", required=True)
    status = fields.Many2one(comodel_name="ats.security.incidents.status", string="Status", default=1, required=True)
    usuario = fields.Many2one(comodel_name="res.users", string="Usuário", readonly=True, default=lambda self: self.env.user, required=True)
    justificativa_status = fields.Text(string="Justificativa do Status", required=True)
