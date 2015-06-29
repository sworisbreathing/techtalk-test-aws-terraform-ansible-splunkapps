request.ui_context = (Added by Sideview Utils).  This is a serialized snapshot of the context keys that were present in the page when the search was saved.  This will be used by Sideview Utils modules to restore/prepopulate UI elements as necessary. Note that without custom logic embedded at the app level, the mere presence of this in the README file will not have any effect. 

request.ui_edit_view = (Added by Sideview Utils). This is a key that may be populated when the search is saved, and it indicates the name of the view within which the user can edit the search arguments.   Splunk allows two other keys -- 'request.ui_dispatch_view' and 'displayView', but those are intended to designate a 'read only' view. Note that without custom logic embedded at the app level, the mere presence of this in the README file will not have any effect. 