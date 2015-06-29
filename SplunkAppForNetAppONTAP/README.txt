INTRODUCTION

The Splunk App for NetApp ONTAP uses the NetApp Manageability SDK (http://www.netapp.com/us/products/management-software/open-management.html) combined with read-only API access to one or more FAS controllers to provide realtime and historical visibility into the performance and configuration of your NetApp storage infrastructure. 

Included with this version of the Splunk App for NetApp ONTAP are:

* One app:
  * SplunkAppForNetAppONTAP - The main app which includes a basic set of
    sample dashboards highlighting some of the performance data which is being
    collected
* Two add-ons (located in the archive under appserver/addons):
  * Splunk_TA_ONTAP7 - The Technology Add-on which can run on an Indexer, or a 
    Forwarder
  * Splunk_SA_ONTAP_KB - An add-on which contains configuration files intended
    for both the Index and Search Head tiers in a distributed install of Splunk

REQUIREMENTS

In addition to Splunk (version 4.3 or later), you will need:

* One or more NetApp FAS or V-Series controllers, or the Data ONTAP Simulator
* Your controllers must be running Data ONTAP in 7-mode. Testing has been 
  performed using various versions of v7 and v8.
* Your Splunk server or forwarder must have network access to the storage
  controllers you wish to query.
* If using a Splunk Forwarder to run the Technology Add-on (more on that in a 
  moment), it should be a Lightweight or Heavy Forwarder, as the Universal
  Forwarder does not include a Python interpreter. Alternately, install Python
  2.6 on a Universal Forwarder.

CLUSTER MODE?

Due to API changes, Data ONTAP Cluster Mode, sometimes referred to as Clustered ONTAP, is not supported at this time. C-mode support is in development.

GETTING STARTED

Step 1: Create a user account on the storage controller(s) with the following permissions:

	login-http-admin
	api-*
	
You can use the following commands to create the role, group, and user:
	
	useradmin role add role_api -a login-http-admin,api-*
	useradmin group add group_api -r role_api
	useradmin user add user_api -g group_api

Step 2: Enable HTTPD on your filers:

In the filer CLI, you can check "options httpd" to see the status of your HTTPD service. To enable it and administration via the service, enter the following commands (on every filer to be managed by this app):

	options httpd.enable on
	options httpd.admin.enable on

Step 3: Install the app

Single Server Deployment

For a single server deployment, copy all three apps: SplunkAppForNetAppONTAP, Splunk_TA_ONTAP7, Splunk_SA_ONTAP_KB, to $SPLUNK_HOME/etc/apps on your Splunk server and continue to Step 4.

Distributed Deployment

  * SplunkAppForNetAppONTAP - Deploy this app to $SPLUNK_HOME/etc/apps on your SEARCH HEAD only.
  * Splunk_TA_ONTAP7 - Deploy this app to $SPLUNK_HOME/etc/apps on an INDEXER, or a LIGHTWEIGHT FORWARDER. Do not deploy this app to multiple servers without taking special care to configure the inputs uniquely, otherwise data duplication might occur.
  * Splunk_SA_ONTAP_KB - Deploy this app to $SPLUNK_HOME/etc/apps on your SEARCH HEAD *and* INDEXER. This app contains:
  	indexes.conf
  	macros.conf
  	props.conf
  	transforms.conf
  	default.meta

Step 4: Configure the app

1. Examine the configuration files in $SPLUNK_HOME/Splunk_TA_ONTAP7 in the default/, conf/, and local/ folders.
2. Rename or copy conf/snap_hosts.csv.sample to snap_hosts.csv, and edit this file. The columns are: host, username, password. Create an entry for each NetApp storage controller to be polled by Splunk.
3. If running Windows, rename default\inputs.conf to inputs.conf.bak, and rename default\inputs.conf.windows to inputs.conf.
4. Create an NFS mount to the system partition of your filer(s). Copy local/inputs.conf.sample to inputs.conf and edit this file. Specify path to the system log path. For example:

    [monitor:///opt/netapp_logs/10.160.114.230/etc/log]
    
Step 5: Restart Splunk!

When configured correctly, data should start to be indexed within several minutes following a restart. To validate that an installation is successful, run the following search:

	index=netapp* | stats count by sourcetype

There should be at minimum, three sourcetypes:

* netapp:cfg - configuration data
* netapp:internal - debug data showing performance of the TA
* netapp:perf - performance data

The storage controller system logs (mounted via NFS) are auto-assigned a sourcetype based on their content, for example "syslog".

NOTES ABOUT THE DATA

The data for this app comes into Splunk via two ways: SNap.py, and NFS mount. 

SNap.py is a multi-threaded script which writes the data it collects to the "_OUT_" folder inside of the app folder. Each storage controller's data is written to a unique file, and the contents of these files are read into Splunk by the tailing processor (a file monitor). This data includes both performance and configuration data sourcetypes as mentioned above.

NFS mounts are used to access the system logs on the system partition of a 7-mode filer. These logs contain alerts and messages from various subsystems within ONTAP.

About Performance Data

Many of the performance-related values returned from the SDK are "raw". In other words, various equations must be performed on these values before the data matches what one would expect to see based on looking at tools such as perfstat, Data Fabric Manager, or OnCommand Operations Manager. For this reason, we are including several macros with the app which help to perform some of these equations. 

NOTES ABOUT THE DASHBOARDS

The dashboards in this app are samples which you can use as-is, or customize to suit your needs. They are not intended to be a complete monitoring solution for NetApp storage controllers. The power and potential of this app revolve more around taking the data and making it a part of full stack, of which storage is one piece. For an applied example, see the Splunk App for Citrix XenApp (http://splunk-base.splunk.com/apps/48390/splunk-app-for-citrix-xenapp).

KNOWN ISSUES

* The host (forwarder or indexer) running the TA scripts will appear in the pick list of some dashboards. It did not magically turn into a storage controller, this is a bug and the data can be ignored.
* The "Configuration Info" table in the "Report on filer" dashboard is not showing all configuration detail due to a visualization bug. To see all of this data, search against the "netapp:cfg" sourcetype.

Feedback welcome! You can contact us by emailing <netapp@splunk.com>.