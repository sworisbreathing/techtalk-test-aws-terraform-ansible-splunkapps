##  Splunk Technology Add-on for NetApp (SNap)
##
##  Author:	Ron Naken (ron@splunk.com)
##  Version:	1.0
##
##  Copyright (c) 2012 Splunk Inc.  All rights reserved.
##
##  This program was created to allow Splunk to collect performance
##  metrics and configuration from NetApp filers.

Create a user account for Splunk to use when collecting NetApp data.  The
account requires the following rights:

	login-http-admin
	api-*
	
You can perform the following commands to create the role, group, and user:
	
	useradmin role add role_api -a login-http-admin,api-*
	useradmin group add group_api -r role_api
	useradmin user add user_api -g group_api

snap_counters.map

TIME FORMAT:

The format strings used by Splunk to display time within the NetApp app are
controlled, centrally, through macros.  If you would like to change how
time is displayed, you can modify the following macros:

	snap_ctime()


Special thanks to Jim Crumpler for his magnificent work in developing
py-ontapi.  The library is included in the SNap package, and it is used
by SNap for API calls.


COLLECTING PERFORMANCE AND CONFIGURATION DATA:

SNAP.PY:

SNap.py is a Python script that allows API access to NetApp performance
and configuration data.  Use snap_counters.csv to configure API access,
and snap_hosts.csv to list filers and login configuration.  Documentation
for theses files can be found inside them.  

SNap.py is multi-threaded, and it will pull data from all configured filers,
concurrently.  SNap.py also allows for the use of command-line arguments to
support running multiple copies with different configuration sets.

Command-line options are shown, below:

	-h	:	When using additional SNap.py configurations, this instructs
			SNap.py to use additional snap_hosts.csv files.  Normally,
			SNap.py will use the default snap_hosts.csv file.  Files are
			enumerated the same as snap_counters.csv.

	##	:	You may specify exactly two digits to use as enumerators for
			API/counter configuration files.  This allows you to run SNap.py
			with separate configurations.  Filenames will be of the format, 
			snap_counters.##.csv.  (This option must follow the -h
			option when -h is used)   

	Sample Usage:
	
		./SNap.py		:	run SNap.py using default configuration
							files.

							uses files:
								snap_hosts.csv, snap_counters.csv

		./SNap.py 01	:	run SNap.py using API/counter set 01.

							uses files:
								snap_hosts.csv, snap_counters.01.csv

							uses files:
								snap_hosts.01.csv, snap_counters.01.csv





