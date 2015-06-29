#!/usr/bin/python

##  SPLUNK FOR NETAPP (SNap)
##
##  Author:	 Ron Naken (ron@splunk.com)
##  Version:	1.0
##
##  Copyright (c) 2013 Splunk Inc.  All rights reserved.
##
##  This program was written to allow Splunk to collect performance
##  metrics and configuration data from NetApp filers.

import os
import sys
import SNap_Pak.SNap_Threads as NA

from time import strftime

APP = 'SNap'
PATH = ''
MAX_LOG_SIZE = 500 * 1024 ** 2
DATE_FORMAT = '%m-%d-%Y %H:%M:%S %Z'

hosts = []

# read the list of filers
def get_config(suffix, host_flag):
	global hosts, PATH

	try:
		if (host_flag == 1):
			fil = os.path.join(PATH,'conf', 'snap_hosts' + suffix + '.csv')
		else:
			fil = os.path.join(PATH,'conf', 'snap_hosts.csv')

		fp = open(fil, 'r')
		for l in fp.readlines():
			if not l[:1] == '#':		# strip comments
				hosts.append(l)
		fp.close()
	except:
		pre_diag_out('I/O error: ' + fil)
		sys.exit(1)

# get command-line arguments
def get_args():
	hostFlag = 0
	
	if len(sys.argv) <= 3:
		if len(sys.argv) < 2:		# no arguments is OK
			return '', 0
		for arg in sys.argv:
			if (arg == '-h'):
				hostFlag = 1
			elif (len(arg) == 2) and arg.isdigit():
				return '.' + arg, hostFlag
	pre_diag_out('Incorrect command-line options specified.  Usage:  SNap.py [-h] [suffix]')
	sys.exit(1)

def get_path():
	global PATH
	
	try:
		PATH = os.environ['SPLUNK_HOME']
	except:
		pre_diag_out('Environment variable SPLUNK_HOME not set.')
		sys.exit(1)
	
	PATH = os.path.join(PATH, 'etc', 'apps', 'Splunk_TA_ONTAP7')

def pre_diag_out(s):
	global APP, DATE_FORMAT
	print strftime(DATE_FORMAT), APP + ':', s

# main thread
get_path()

suffix, host_flag = get_args()
	
get_config(suffix, host_flag)
NA.init_diag(APP, PATH, MAX_LOG_SIZE, DATE_FORMAT)
NA.init_counters(PATH, suffix)

NA.diag_out('Entering Main Thread, %d Filers.' % (len(hosts)))

# create a thread for each filer
tid = 1
threads = []

for l in hosts:
	ip, user, pw = l.split(',')
	thread = NA.naThread(tid, ip.strip(), user.strip(), pw.strip(), suffix)
	thread.start()
	threads.append(thread)
	tid += 1

# exit all threads
for t in threads:
	t.join()
NA.diag_out('Exiting Main Thread')
