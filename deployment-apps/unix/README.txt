Copyright (C) 2005-2011 Splunk Inc. All Rights Reserved.

App:                Splunk for Unix
Current Version:    4.2.4
Last Modified:      2011-10-12
Splunk Version:     4.2.x, 4.3.x
Author:             Splunk, Inc.


The Splunk for UNIX app provides general health monitoring reports and metrics for Unix-based operating systems. The app includes support for a variety of different metrics available through various sources, including:

	* CPU statistics via the 'sar', 'mpstat' and 'iostat' commands (cpu.sh scripted input).

	* Free disk space available for each mount via the 'df' command (df.sh scripted input).

	* Hardware information - cpu type, count, cache; hard drives; network interface cards, count; and memory via 'dmesg', 'iostat', 'ifconfig', 'df' commands (hardware.sh scripted input).
	
	* Information about the configured network interfaces via the 'ifconfig' and 'dmesg' commands (interfaces.sh scripted input)

	* Input/output statistics for devices and partitions via 'iostat' command (iostat.sh scripted input).

	* Last login times for system accounts via 'last' command (lastlog.sh scripted input)

	* Information about files opened by processes via 'lsof' command (lsof.sh scripted input).

	* Network connections, routing tables and network interface statistics via 'netstat' command (netstat.sh scripted input).

	* Available network ports via 'netstat' command (openPorts.sh scripted input).

	* Information about software packages or sets that are installed on the system via 'dpkg-query', 'pkginfo', 'pkg_info' commands (package.sh scripted input).

	* Information about TCP/UDP transfer statistics via 'netstat' command (protocol.sh scripted input).

	* Status of current running processes via 'ps' command (ps.sh scripted input).

	* Audit information recorded by auditd daemon to /var/log/audit/audit.log (rlog.sh scripted input).

	* System date and time and the NTP server time via 'date' and 'ntpdate' commands (time.sh scripted input).

	* List of running system processes via 'top' command (top.sh scripted input).

	* User attribute information for the local system via /etc/passwd file (usersWithLoginPrivs.sh scripted input).

	* Process related memory usage information via 'top', 'vmstat' and 'ps' commands (vmstat.sh scripted input).

	* Information of all users currently logged in via 'who' command (who.sh scripted input).



##### What's New #####

4.2.4 (2011-10-12)
- Nearly 100 bug fixes
- New setup and first time run tools
- Enhanced support for AIX

##### Technology Add-on Details ######

Sourcetype(s):
	* top
	* package
	* lsof
	* vmstat
	* iostat
	* cpu
	* time
	* netstat
	* lastlog
	* who
	* time
	* lastlog
	* who
	* usersWithLoginPrivs
	* openPorts
	* hardware
	* df
    
Supported Technologies:     Unix based operating systems
Compatible Solutions:       Unix


###### Installation Instructions ######

The Unix app can be downloaded and installed by either using the Splunk app setup screen or by manually installing and configuring the app.  Instructions for both methods are described.

+++ Automated setup using the app setup +++

The automated setup is designed to walk you through the configuration of the Unix app once it is installed on your Splunk deployment.  The setup screen can be accessed in one of the following ways:

1. Click on the "Setup" link in the modal pop-up when visiting the app's home page
2. Click the "Setup" link on the right side of the top level navigation within the app

The setup of the app allows selective enabling of file and scripted inputs as well as the interval to which the scripted inputs run.

+++ Manual setup and configuration +++

--- Configuring the Unix app for the first time ---

If this is the first time you are installing the UNIX app to your Splunk deployment, follow these instructions.

1. Copy the default inputs.conf file ($SPLUNK_HOME/etc/apps/unix/default/inputs.conf) to the local directory ($SPLUNK_HOME/etc/apps/unix/local/inputs.conf).  This is necessary to preserve the upgrade-ability of the UNIX app as Splunk pushes new versions of the app out.

2. Open the $SPLUNK_HOME/etc/apps/unix/local/inputs.conf file for edit.  Within the file you will find configuration stanzas for each of the scripted inputs that drive the Unix app dashboards.  Example:

   [script://./bin/vmstat.sh]
   interval = 60
   sourcetype = vmstat
   source = vmstat
   index = os
   disabled = 1

3. Each of the scripted inputs will be disabled by default.  To enable one of the scripted inputs, modify the "disabled=1" to "disabled=0" or "disabled=false".  Example:

   [script://./bin/vmstat.sh]
   interval = 60
   sourcetype = vmstat
   source = vmstat
   index = os
   disabled = false

4. The "interval" represents the interval between each execution of the script (in seconds).  To modify the default interval, simply change the interval from the default value to another integer representing the number of seconds desired.

5. Once you have enabled the desired inputs and modified the parameters as desired, save the file.  

WARNING: Do NOT make modifications to either the source or sourcetype fields defined on the scripted inputs.  These fields are used by the Unix app.  If modified, the Unix app may not behave properly.  Note also that it is not advised to change the index location as well.

6. Splunk requires a restart before the modified changes will take effect.  Restart and check splunkd.log for errors.

--- Re-Configuring or Upgrading the Unix app ---

If the Unix app has been installed already and you are re-configuring the app or if you have upgraded the app, follow the same instructions above, but DO NOT copy the inputs.conf file from the default to local directories.  Doing so will wipe out any previously configured settings.  


###### Getting Help ######

  * Splunk add-on overview: http://splunkbase.splunk.com/apps/All/4.x/app:Splunk+for+Unix+and+Linux
  * Questions and answers (Unix app specific): http://answers.splunk.com/questions/tagged/unix
  * Questions and answers (General Splunk): http://answers.splunk.com
  * General support: http://www.splunk.com/support