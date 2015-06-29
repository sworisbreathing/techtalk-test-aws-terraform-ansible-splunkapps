switch (Splunk.util.getCurrentView()) {
    case "configs_diff":
        if (Splunk.Module.LinkList) {
            Splunk.Module.LinkList = $.klass(Splunk.Module.LinkList, {

                // override sendSearchToView to use stringReplace intention
                sendSearchToView: function(event, field) {
                    var target = event.target;
                    if (target.tagName.toUpperCase() == 'A') {
                        var context = this.getContext();
                        var search  = context.get("search");
                        search.abandonJob();
                        search.setBaseSearch(this._params[field + 'FieldSearch']);
                        var intention = { 
                            'name': 'stringreplace',
                            'arg':  { 'source' : 
                                        { 'value' : $(target).text().replace(/(\r\n|\n|\r)/gm,""),
                                          'prefix' : 'source="',
                                          'suffix' : '"' 
                                        }   
                                    }   
                        };  
                        search.addIntention(intention);
                        search.sendToView(this._params[field + 'FieldTarget']);
                        event.preventDefault();
                    }   
                    return false;
                }   

            }); 
        }   
}
