from odoo import http
from odoo.http import request


class AtsSecurityReports(http.Controller):

    @http.route('/custom/url', type='http', auth='user', website=True)
    def loadReportsPage(self):
        return http.request.render("ats_security.reports_page")
