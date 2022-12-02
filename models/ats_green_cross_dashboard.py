from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ModelCV(models.Model):
    _name = 'ats.security.model.cv'
    _description = 'ATS Security Model CV'

    order = fields.Char(string='Order')
    div_id = fields.Char(string='DIV ID')


class ModelCV_Default(models.Model):
    _name = 'ats.security.model.cv.default'
    _description = 'ATS Security Model CV Default'

    month = fields.Char(string='Month')
    order = fields.Char(string='Order')
    div_id = fields.Char(string='DIV ID')


class ViewDateRef(models.Model):
    _name = 'ats.security.view.inc.date.ref'
    _description = 'ATS Security View Date Ref'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_date_ref AS (
            SELECT to_char(d.d, 'YYYYMMDD'::text)::integer AS date_id,
            d.d::date AS date_ref
            FROM generate_series((( SELECT ats_security_reference.office_date
           FROM ats_security_reference))::timestamp with time zone, (CURRENT_DATE - 1)::timestamp with time zone, '1 day'::interval) d(d)    )
        """)


class ViewDateRefMonth(models.Model):
    _name = 'ats.security.view.inc.date.ref.month'
    _description = 'ATS Security View Date Ref Month'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_date_ref_month AS (
             SELECT to_char(d.d, 'YYYYMMDD'::text)::integer AS date_id,
    d.d::date AS date_ref
   FROM generate_series(date_trunc('month'::text, CURRENT_DATE::timestamp with time zone)::date::timestamp with time zone, date_trunc('month'::text, CURRENT_DATE::timestamp with time zone) + '1 mon -1 days'::interval, '1 day'::interval) d(d)    )
        """)


class ViewDashPanel(models.Model):
    _name = 'ats.security.view.inc.dash.panel'
    _description = 'ATS Security View Incidents Dash Panel'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_dash_panel AS (
             SELECT (to_char((asi.date)::timestamp with time zone, 'YYYY'::text))::integer AS year_ref,
                    sum(
                        CASE
                            WHEN (asi.incident_type = 1) THEN 1
                            ELSE 0
                        END) AS accid_pers,
                    sum(
                        CASE
                            WHEN (asi.incident_type = 2) THEN 1
                            ELSE 0
                        END) AS accid_prop,
                    sum(
                        CASE
                            WHEN (asi.incident_type = 3) THEN 1
                            ELSE 0
                        END) AS accid_envir,
                    sum(
                        CASE
                            WHEN (asi.level = 1) THEN 1
                            ELSE 0
                        END) AS level_1,
                    sum(
                        CASE
                            WHEN (asi.level = 2) THEN 1
                            ELSE 0
                        END) AS level_2,
                    sum(
                        CASE
                            WHEN (asi.level = 3) THEN 1
                            ELSE 0
                        END) AS level_3,
                    sum(
                        CASE
                            WHEN (asi.level = 4) THEN 1
                            ELSE 0
                        END) AS level_4,
                    sum(
                        CASE
                            WHEN (asi.level = 5) THEN 1
                            ELSE 0
                        END) AS level_5,
                    sum(
                        CASE
                            WHEN (asi.company = 1) THEN 1
                            ELSE 0
                        END) AS owner_comp,
                    sum(
                        CASE
                            WHEN (asi.company <> 1) THEN 1
                            ELSE 0
                        END) AS third_comp
                FROM ats_security_incidents asi
                GROUP BY (to_char((asi.date)::timestamp with time zone, 'YYYY'::text))::integer   )
        """)


class ViewModelCV_Default(models.Model):
    _name = 'ats.security.view.inc.model.cv.default'
    _description = 'ATS Security View Model CV Default'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_model_cv_default AS (
             SELECT asmcd.id,
                    asvidp.year_ref,
                    asmcd.month,
                    asmcd."order",
                    asmcd.div_id
                FROM ats_security_model_cv_default asmcd,
                    ats_security_view_inc_dash_panel asvidp
                ORDER BY asvidp.year_ref, asmcd.id    )
        """)


class ViewDashLastAccid(models.Model):
    _name = 'ats.security.view.inc.dash.last.accid'
    _description = 'ATS Security View Dash Last Accident'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_dash_last_accid AS (
              SELECT to_char(asi.date::timestamp with time zone, 'YYYY'::text)::integer AS year_last_accid,
                    max(
                        CASE
                            WHEN asi.incident_type = 1 THEN to_char(asi.date::timestamp with time zone, 'DD/MM/YYYY'::text)
                            ELSE '--/--/----'::text
                        END) AS accid_pers,
                    max(
                        CASE
                            WHEN asi.incident_type = 2 THEN to_char(asi.date::timestamp with time zone, 'DD/MM/YYYY'::text)
                            ELSE '--/--/----'::text
                        END) AS accid_prop,
                    max(
                        CASE
                            WHEN asi.incident_type = 3 THEN to_char(asi.date::timestamp with time zone, 'DD/MM/YYYY'::text)
                            ELSE '--/--/----'::text
                        END) AS accid_envir
                FROM ats_security_incidents asi
                GROUP BY (to_char(asi.date::timestamp with time zone, 'YYYY'::text)::integer)    )
        """)


class ViewGreenCrossMonth(models.Model):
    _name = 'ats.security.view.inc.green.cross.month'
    _description = 'ATS Security View Green Cross Month'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_green_cross_month AS (
             SELECT asvidrm.date_id,
                asvidrm.date_ref,
                to_char(asvidrm.date_ref::timestamp with time zone, 'YYYY'::text)::integer AS year_ref,
                to_char(asvidrm.date_ref::timestamp with time zone, 'MM'::text)::integer AS month_ref,
                to_char(asvidrm.date_ref::timestamp with time zone, 'DD'::text)::integer AS day_ref,
                asi.incident_type,
                    CASE
                        WHEN asvidrm.date_ref >= CURRENT_DATE THEN 'GREY'::text
                        WHEN asi.incident_type = 1 THEN 'RED'::text
                        WHEN asi.incident_type = 2 THEN 'BLUE'::text
                        WHEN asi.incident_type = 3 THEN 'YELLOW'::text
                        ELSE 'GREEN'::text
                    END AS color,
                    CASE
                        WHEN asvidrm.date_ref >= CURRENT_DATE THEN '#ddd'::text
                        WHEN asi.incident_type = 1 THEN '#ff0000'::text
                        WHEN asi.incident_type = 2 THEN '#00b0f0'::text
                        WHEN asi.incident_type = 3 THEN '#ffff00'::text
                        ELSE '#00b050'::text
                    END AS color_code
            FROM ats_security_incidents asi
                RIGHT JOIN ats_security_view_inc_date_ref_month asvidrm ON asi.date = asvidrm.date_ref    )
        """)


class ViewGreenCrossCentral(models.Model):
    _name = 'ats.security.view.inc.green.cross.central'
    _description = 'ATS Security View Green Cross Central'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_green_cross_central AS (
              SELECT asvidr.date_id,
                asvidr.date_ref,
                to_char(asvidr.date_ref::timestamp with time zone, 'YYYY'::text)::integer AS year_ref,
                to_char(asvidr.date_ref::timestamp with time zone, 'MM'::text)::integer AS month_ref,
                to_char(asvidr.date_ref::timestamp with time zone, 'DD'::text)::integer AS day_ref,
                asi.incident_type,
                    CASE
                        WHEN asvidr.date_ref >= CURRENT_DATE THEN 'GREY'::text
                        WHEN asi.incident_type = 1 THEN 'RED'::text
                        WHEN asi.incident_type = 2 THEN 'BLUE'::text
                        WHEN asi.incident_type = 3 THEN 'YELLOW'::text
                        ELSE 'GREEN'::text
                    END AS color,
                    CASE
                        WHEN asvidr.date_ref >= CURRENT_DATE THEN '#ddd'::text
                        WHEN asi.incident_type = 1 THEN '#ff0000'::text
                        WHEN asi.incident_type = 2 THEN '#00b0f0'::text
                        WHEN asi.incident_type = 3 THEN '#ffff00'::text
                        ELSE '#00b050'::text
                    END AS color_code
            FROM ats_security_incidents asi
                RIGHT JOIN ats_security_view_inc_date_ref asvidr ON asi.date = asvidr.date_ref    )
        """)


class ViewGreenCrossDefault(models.Model):
    _name = 'ats.security.view.inc.green.cross.default'
    _description = 'ATS Security View Green Cross Default'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_green_cross_default AS (
               SELECT asvimcd.id,
                    asvimcd.year_ref,
                    asvimcd.month,
                    asvimcd.div_id,
                    asvimcd."order",
                    asvigcc.incident_type,
                        CASE
                            WHEN asvimcd."order"::text = ' '::text THEN 'WHITE'::text
                            WHEN asvigcc.color IS NULL OR asvigcc.color = ' '::text THEN 'GREY'::text
                            ELSE asvigcc.color
                        END AS color,
                        CASE
                            WHEN asvimcd."order"::text = ' '::text THEN '#ffffff'::text
                            WHEN asvigcc.color_code IS NULL THEN '#ddd'::text
                            ELSE asvigcc.color_code
                        END AS color_code
                FROM ats_security_view_inc_model_cv_default asvimcd
                    LEFT JOIN ats_security_view_inc_green_cross_central asvigcc ON asvimcd.year_ref::text = asvigcc.year_ref::text AND asvimcd.month::text = asvigcc.month_ref::text AND asvimcd."order"::text = asvigcc.day_ref::character varying::text
                ORDER BY asvimcd.year_ref, asvimcd.id    )
        """)


class ViewGreenCross(models.Model):
    _name = 'ats.security.view.inc.green.cross'
    _description = 'ATS Security View Green Cross'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_green_cross AS (
               SELECT asmc.id,
                    asmc."order",
                    asmc.div_id,
                    asvigcm.incident_type,
                        CASE
                            WHEN asmc."order"::text = ' '::text THEN 'WHITE'::text
                            WHEN asvigcm.color IS NULL OR asvigcm.color = ' '::text THEN 'GREY'::text
                            ELSE asvigcm.color
                        END AS color,
                        CASE
                            WHEN asmc."order"::text = ' '::text THEN '#ffffff'::text
                            WHEN asvigcm.color_code IS NULL THEN '#ddd'::text
                            ELSE asvigcm.color_code
                        END AS color_code
                FROM ats_security_model_cv asmc
                    LEFT JOIN ats_security_view_inc_green_cross_month asvigcm ON asmc."order"::text = asvigcm.day_ref::character varying::text
                ORDER BY asmc.id    )
        """)


class ViewIncidentsASPT(models.Model):
    _name = 'ats.security.view.inc.aspt'
    _description = 'ATS Security View Incidents ASPT'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_aspt AS (
               SELECT asr.office_date,
                    min(asi.date) AS date_first_accid,
                    max(asi.date) AS date_last_accid,
                    EXTRACT(day FROM min(asi.date)::timestamp without time zone - asr.office_date::timestamp without time zone) AS record_initial,
                    EXTRACT(day FROM CURRENT_DATE::timestamp without time zone - max(asi.date)::timestamp without time zone) AS record_current,
                    asit.name AS incident_type
                FROM ats_security_reference asr,
                    ats_security_incidents asi
                    JOIN ats_security_incidents_types asit ON asi.incident_type = asit.id
                WHERE asi.incident_type <> 1
                GROUP BY asr.office_date, asi.incident_type, asit.name    )
        """)


class ViewIncidentsACPT(models.Model):
    _name = 'ats.security.view.inc.acpt'
    _description = 'ATS Security View Incidents ACPT'
    _auto = False

    def init(self):
        self._cr.execute(""" 
         CREATE OR REPLACE VIEW ats_security_view_inc_acpt AS (
               SELECT asr.office_date,
                    min(asi.date) AS date_first_accid,
                    max(asi.date) AS date_last_accid,
                    EXTRACT(day FROM min(asi.date)::timestamp without time zone - asr.office_date::timestamp without time zone) AS record_initial,
                    EXTRACT(day FROM CURRENT_DATE::timestamp without time zone - max(asi.date)::timestamp without time zone) AS record_current,
                    asit.name AS incident_type
                FROM ats_security_reference asr,
                    ats_security_incidents asi
                    JOIN ats_security_incidents_types asit ON asi.incident_type = asit.id
                WHERE asi.incident_type = 1
                GROUP BY asr.office_date, asi.incident_type, asit.name    )
        """)


class DashboardFields(models.Model):
    _name = 'ats.dashboard.fields'
    _inherit = 'ats.security.incidents'

    @api.model
    def get_security_status(self):

        personal_accidents = self.env['ats.security.incidents'].search([('incident_type', '=', 1)])
        property_accidents = self.env['ats.security.incidents'].search([('incident_type', '=', 2)])
        environments_accidents = self.env['ats.security.incidents'].search([('incident_type', '=', 3)])

        return {
            'qty_personal_accidents': len(personal_accidents),
            'qty_property_accidents': len(property_accidents),
            'qty_environments_accidents': len(environments_accidents),
        }

