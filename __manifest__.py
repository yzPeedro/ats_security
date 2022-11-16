# noinspection PyStatementEffect
{
    "name": "ATS Security",
    "summary": "Gerenciamento de segurança",
    "version": "1.0.0",
    "author": "AllianceTechSystem",
    "website": "https://alliancetechsystem.com/",
    "license": "LGPL-3",
    "sequence": -100,
    "category": "Security System",
    "depends": ["mgmtsystem", "mgmtsystem_action", "hr", "ks_curved_backend_theme"],
    "data": [
        "views/incidents.xml",
        "views/incidents_types.xml",
        "views/incidents_level.xml",
        "views/incidents_status.xml",
        "views/refs.xml",
        "views/menus.xml",
        "views/reports.xml",
        "security/ir.model.access.csv",
        "data/ats_incidents_levels_data.xml",
        "data/ats_incidents_status_data.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": True
}
