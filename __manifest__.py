# noinspection PyStatementEffect
{
    "name": "ATS Security",
    "summary": "Security Management Module",
    "version": "15.1.1.0",

    # Author
    "author": "Alliance Tech System",
    "support": "suporte@alliancetechsystem.com",
    "website": "https://alliancetechsystem.com",
    "maintainer": "ATSDEV",
    "license": "LGPL-3",
    "sequence": -100,
    "category": "ATS",
    "depends": ["mgmtsystem", "mgmtsystem_action", "hr"],

    # Always loaded.
    "data": [
        # Security...
        "security/ir.model.access.csv",

        # Views...
        "views/incidents.xml",
        "views/incidents_types.xml",
        "views/incidents_level.xml",
        "views/incidents_status.xml",
        "views/refs.xml",
        "views/menus.xml",
        "views/reports.xml",

        # Data...
        "data/ats_incidents_cv_data_default.xml",
        "data/ats_incidents_cv_data.xml",
        "data/ats_incidents_levels_data.xml",
        "data/ats_incidents_status_data.xml",
        "data/ats_incidents_types_data.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "ats_security/static/src/js/green_cross_widget.js",
            "ats_security/static/src/css/lib/nv.d3.css",
            "ats_security/static/src/css/dashboard.css",
            "ats_security/static/src/js/lib/d3.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.js",
        ],
        "web.assets_qweb": [
            "ats_security/static/src/xml/green_cross_widget_templates.xml",

        ],
    },
    "installable": True,
    "application": True,
    "auto_install": True
}
