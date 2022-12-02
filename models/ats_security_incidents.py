from odoo import fields, models


class AtsSecurityIncidents(models.Model):

    _name = "ats.security.incidents"
    _description = "Company Incident Database"

    date = fields.Date(string="Incident Date", required=True)
    company = fields.Many2one(comodel_name="res.partner", string="Company Incident", default=lambda self: self.env.user.company_id.id, required=True)
    sector = fields.Many2one(comodel_name="hr.department", string="Sector", required=True)
    employee = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True)
    incident_type = fields.Many2one(comodel_name="ats.security.incidents.types", string="Incident Type", required=True)
    report = fields.Text(string="Incident Report", required=True)
    level = fields.Many2one(comodel_name="ats.security.incidents.levels", string="Incident Level", required=True)
    action = fields.Many2one(comodel_name="mgmtsystem.action", string="Incident Action", required=True)
    responsible = fields.Many2one(comodel_name="hr.employee", string="Incident Responsible", required=True)
    status = fields.Many2one(comodel_name="ats.security.incidents.status", string="Incident Status", default=1, required=True)
    username = fields.Many2one(comodel_name="res.users", string="Incident Username", readonly=True, default=lambda self: self.env.user, required=True)
    justification_status = fields.Text(string="Justification Status")
