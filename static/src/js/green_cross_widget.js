/*odoo.define('ats_security.custom_dashboard', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var WidgetRegistry = require('web.widget_registry');

    var CustomDashboard = Widget.extend({
        template: 'custom_dashboard',
        xmlDependencies: ['/ats_security/static/src/xml/green_cross_widget_templates.xml'],

        init: function(parent, data, options) {
            this._super.apply(this, arguments);
            this.res_id = data.res_id;
            this.node = options;
        },

        start: function () {
            var self = this;

            return this._super.apply(this, arguments);
        }
    });

    WidgetRegistry.add('custom_dashboard', CustomDashboard);
    return CustomDashboard;
});*/


odoo.define('pj_dashboard.Dashboard', function (require) {
    "use strict";
    
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');
    var _t = core._t;
    var session = require('web.session');
    var web_client = require('web.web_client');
    var abstractView = require('web.AbstractView');
    
    
    
    
    var PjDashboard = AbstractAction.extend({
        template:'PjDashboard',
        cssLibs: [
            '/ats_security/static/src/css/lib/nv.d3.css'
        ],
        jsLibs: [
            '/ats_security/static/src/js/lib/d3.min.js'
        ],
    
   
        init: function(parent, context) {
            this._super(parent, context);
            this.dashboards_templates = ['custom_dashboard','DashboardProject'];
            this.fetch_data()
        },

        fetch_data: function () {
            const self = this;
            this._rpc({
                model: 'ats.dashboard.fields',
                method: 'get_security_status'
            }).then((response) => {
                self.qty_personal_accidents = response['qty_personal_accidents']
                self.qty_property_accidents = response['qty_property_accidents']
                self.qty_environments_accidents = response['qty_environments_accidents']
            })
        },

        start: function() {
                var self = this;
                this.set("title", 'Dashboard');
                return this._super().then(function() {
                    self.render_dashboards();
                });
            },
    
        render_dashboards: function(){
            var self = this;
            _.each(this.dashboards_templates, function(template) {
                    self.$('.o_pj_dashboard').append(QWeb.render(template, {widget: self}));
                });
        },

    
    });
    
    core.action_registry.add('gc_dashboard', PjDashboard);
    
    return PjDashboard;
    
    });
    
    