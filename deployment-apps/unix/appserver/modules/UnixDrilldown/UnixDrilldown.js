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

/**
 * A module that handles drilldown for the Unix app 
 * @author araitz
 */
Splunk.Module.UnixDrilldown = $.klass(Splunk.Module, {

    initialize: function($super, container) {

        $super(container);

        this.logger = Splunk.Logger.getLogger("UnixDrilldown.js");
        this.messenger = Splunk.Messenger.System.getInstance();
        this.drilldownKey = this.getParam('drilldownKey', null);

    },

    getModifiedContext: function() {
        var context = this.getContext(), 
            click = context.getAll('click'),
            search = context.get('search'),
            new_search = search.job.getEventSearch(),
            time_range;
        search.abandonJob();
        if (!(this.drilldownKey == null)) {
            if (click.name2 && click.name2 != 'OTHER') {
                new_search = new_search + ' | search ' 
                    + this.drilldownKey + '="' + click.name2 + '"'; 
            }
        }
        if (click.timeRange) {
            time_range = click.timeRange.clone();
            search.setTimeRange(time_range);
        }
        search.setBaseSearch(new_search);
        context.set('search', search);
        return context;
    }
});
