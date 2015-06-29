// Copyright 2011 Splunk, Inc.
//
//   Licensed under the Apache License, Version 2.0 (the "License"); 
//   you may not use this file except in compliance with the License.    
//   You may obtain a copy of the License at
//                                                                                                        
//       http://www.apache.org/licenses/LICENSE-2.0 
//
//   Unless required by applicable law or agreed to in writing, software 
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and 
//   limitations under the License.

Splunk.namespace("Module");
Splunk.Module.Unix_FTR= $.klass(Splunk.Module, {

    ADMIN_CONFIGURE: '<p class="popupText">The Splunk for Unix App has not been configured yet.</p><p class="popupText">Until it is configured, it may not work as expected.</p><p class="popupText">Please click \'Configure\' below to perform setup configuration.</p>',
    NON_ADMIN_CONFIGURE:  '<p class="popupText">The Splunk *nix App has not been configured yet.</p><p class="popupText">  Until it is configured, it may not work as expected. Please notify your Splunk admin about this message.</p>',
    COLLISION_WARN: '<p class="popupText">The app "%s" is installed on this system.</p><p class="popupText">The Splunk *nix App and the "%s" app cannot exist together on the same Splunk instance.</p><p class="popupText">Please click on Manage Apps to disable the conflicting app, then remove "%s" from $SPLUNK_HOME/etc/apps and restart Splunk.</p>',

    initialize: function($super, container) {
        $super(container);
        this.logger = Splunk.Logger.getLogger("unix_ftr.js");
        this.messenger = Splunk.Messenger.System.getInstance();
        this.popupDiv = $('.ftrPopup', this.container).get(0);
        this.redirectTo = this.getParam('configLink', 'setup');
        this.getResults();
    },

    renderResults: function(response, turbo) {
        if (response.is_conflict && response.is_conflict===true) {
            this.popupDiv.innerHTML = this.COLLISION_WARN.replace(/%s/g, response.app_label);
            this.popup = new Splunk.Popup(this.popupDiv, {
                cloneFlag: false,
                title: _("Unsupported Configuration"),
                pclass: 'configPopup',
                buttons: [
                    {
                        label: _("Manage Apps"),
                        type: "primary",
                        callback: function(){
                            Splunk.util.redirect_to(['manager',  Splunk.util.getCurrentApp(),
                                                     'apps', 'local'].join('/'));
                        }.bind(this)
                    }
                ]
           });
        } else if ((response.has_ignored && response.has_ignored===true) 
                || (response.is_configured && response.is_configured===true)) {
            return true;
        } else if (response.is_admin && response.is_admin===true) {
            this.popupDiv.innerHTML = this.ADMIN_CONFIGURE; 
            this.popup = new Splunk.Popup(this.popupDiv, {
                cloneFlag: false,
                title: _("This App Needs Configuration"),
                pclass: 'configPopup',
                buttons: [
                     {
                         label: _("Ignore"),
                         type: "secondary",
                         callback: function(){
                             this.setIgnored();
                             return true;
                         }.bind(this)
                     },
                     {
                         label: _("Configure"),
                         type: "primary",
                         callback: function(){
                             Splunk.util.redirect_to(['app', Splunk.util.getCurrentApp(),
                                                      this.redirectTo].join('/'));
                         }.bind(this)
                     }
                 ]
             });
        } else {
            this.popupDiv.innerHTML = this.NON_ADMIN_CONFIGURE;
            this.popup = new Splunk.Popup(this.popupDiv, {
                cloneFlag: false,
                title: _("This App Needs Configuration"),
                pclass: 'configPopup',
                buttons: [
                    {
                        label: _("Continue"),
                        type: "primary",
                        callback: function(){
                            this.setIgnored();
                            return true;
                        }.bind(this)
                    }
                ]
           });
        }
    },

    setIgnored: function() {
        var params = this.getResultParams();
        if (!params.hasOwnProperty('client_app')) {
            params['client_app'] = Splunk.util.getCurrentApp();
        }
        params['set_ignore'] = true;
        var xhr = $.ajax({
                        type:'GET',
                        url: Splunk.util.make_url('module', Splunk.util.getConfigValue('SYSTEM_NAMESPACE'), this.moduleType, 'render?' + Splunk.util.propToQueryString(params)),
                        beforeSend: function(xhr) {
                            xhr.setRequestHeader('X-Splunk-Module', this.moduleType);
                        }, 
                        success: function() {
                            return true;
                        }.bind(this),
                        error: function() {
                            this.logger.error(_('Unable to set ignored flag')); 
                        }.bind(this),
                        complete: function() {
                            return true; 
                        }
        });

    }
});
