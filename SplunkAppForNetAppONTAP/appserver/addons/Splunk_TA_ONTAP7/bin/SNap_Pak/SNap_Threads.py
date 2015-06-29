#!/usr/bin/python

##  SPLUNK FOR NETAPP (SNap)
##
##  Author:	Ron Naken (ron@splunk.com)
##  Version:	1.0
##
##  Copyright (c) 2013 Splunk Inc.  All rights reserved.
##
##  This program was written to allow Splunk to collect performance
##  metrics and configuration data from NetApp filers.

import os
import sys
import threading
import time

import ontapi.NaServer as NAS

from time import strftime

app = ''
path = ''
max_log_size = 1 * 1024 ** 2

lock = threading.Lock()
date_format = '%m-%d-%Y %H:%M:%S %Z'

counters = ''

class naThread (threading.Thread):
	def __init__(self, tid, name, user, pw, suffix):
		threading.Thread.__init__(self)
		self.tid = tid
		self.name = name
		self.user = user
		self.pw = pw
		self.error = 0
		self.suffix = suffix
		if suffix == '':
			self.log = os.path.join(path, 'log', app.lower() + '.__' + self.name.lower() + '.log')
		else:
			self.log = os.path.join(path, 'log', app.lower() + suffix+ '.__' + self.name.lower() + '.log')			
	def stop(self):
		diag_out('Stopping Thread')
		self.error = 1
	def run(self):
		diag_out('START Thread -%i- %s@%s' % (self.tid, self.user, self.name))
		server = NAS.NaServer(self.name)
		server.setTransportType('https')
		server.setAdminUser(self.user, self.pw)
		fp = open(self.log, 'a')

		for l in counters:
			s, c, typ, lst = l.split('|')
			if (s == 'perf') :
				na_stats(server, self, fp, c, typ, lst)
			if (s == 'conf'):
				na_config(server, self)

		if fp.tell() >= max_log_size:
			log_rotate(fp, self)
		fp.close()
		diag_out('END Thread -%i- %s@%s' % (self.tid, self.user, self.name))

def na_stats_x2(server, thread, fp, counter, typ, lst):
	buf = {}
	results = server.invoke('perf-object-get-instances', {'objectname': counter})
	buf['api_time'] = ' api_time=' + results.getChildByName('timestamp').getContent()
	r = results.getChildByName('instances')
	for x in r.getChildren():									   # iterate instance-data branches
		inst = []
		y = x.getChildByName('counters')
		for tmp in y.getChildren():
			l = len(tmp.getChildren())
			k = tmp.getChildByName('name').getContent()
			v = tmp.getChildByName('value').getContent()
			if (l == 2):
				if (typ == '*') or (((typ == '-') or (typ[:1] == 'x')) and (k in lst)):
					inst.append(show_kv(k, v))
			else:
				fp.write('Error in container.  Not an even pair of name/value to parse in', tmp.getName())
		buf[x.getChildByName('name').getContent()] = inst
	return buf

def na_stats(server, thread, fp, counter, typ, lst):
	buf = {}
	if (typ[:1] == 'x'):
		buf = na_stats_x2(server, thread, fp, counter, typ, lst)

	# if we have two sets, make sure the clock rolled
	for c in range(18):					# loop a max of 18 times (1.5 mins)
		results = server.invoke('perf-object-get-instances', {'objectname': counter})
		api_time = results.getChildByName('timestamp').getContent()
		if (typ[:1] == 'x'):
			if (api_time == buf['api_time'][10:]):
				time.sleep(5)
				continue
		break
		
	tstamp = strftime(date_format) + ' '
	r = results.getChildByName('instances')
	for x in r.getChildren():									   # iterate instance-data branches
		inst = x.getChildByName('name').getContent()
		fp.write(tstamp + show_kv('object', counter)  + ' ')
		fp.write(show_kv('instance', inst))
		if (typ[:1] == 'x'):
			fp.write(' api_time_2=' + api_time)
		else:
			fp.write(' api_time=' + api_time)		
		if (buf):
			fp.write(buf['api_time'])
			for d in buf[inst]:
				fp.write(' ' + d)
		y = x.getChildByName('counters')
		for tmp in y.getChildren():
			l = len(tmp.getChildren())
			k = tmp.getChildByName('name').getContent()
			v = tmp.getChildByName('value').getContent()
			if (l == 2):
				if (typ == '*') or (typ == 'x') or (((typ == '-') or (typ == 'x-')) and (k in lst)):
					if (typ[:1] == 'x') and (k in lst):
						fp.write(' ' + show_kv(k + '_2', v))
					else:
						fp.write(' ' + show_kv(k, v))
			else:
				fp.write('Error in container.  Not an even pair of name/value to parse in', tmp.getName())
		fp.write("\n")
		fp.flush()
		
def na_generic(server, thread, fp, lf, obj, container, elems):

	results = server.invoke(obj)
	r = results.getChildByName(container)
	
	for tmp in r.getChildren():
		if (tmp.getName() == elems) :
			fp.write(show_kv(tmp.getChildByName('name').getContent(), tmp.getChildByName('value').getContent()))
			if (lf):
				fp.write('\n')

def na_config(server, thread):
	global app, path
	
	fp = open(os.path.join(path, 'cfg', app.lower() + '.__' + thread.name.lower() + '.cfg'), 'w')
	na_generic(server, thread, fp, True, 'options-list-info', 'options', 'option-info')
	fp.close()

def show_kv(key, value):
	# only quote if non-numeric
	try:
		float(value)
	except:
		if (value is None):
			value = ''		
		return key + '=\"' + value + '\"'
	return key + '=' + value

def log_rotate(fp, thread):
	old = thread.log
	new = thread.log + '.1'
	fp.close()
	diag_out('Rotating %s' % (old))
	try:
		os.remove(new)
	except:
		pass
	try:
		os.rename(old, new)
	except:
		diag_out('Failed to rename %s to %s' % (old, new))
		diag_out(sys.exc_info())
	try:
		fp = open(old, 'a')
	except:
		diag_out('Failed to create %s' % (old))
		diag_out(sys.exc_info())
		thread.stop()

def init_diag(a, p, m, date_f):
	global app, path, max_log_size, date_format
	app = a
	path = os.path.join(p, '_OUT_')
	max_log_size = m
	date_format = date_f
	
def init_counters(path, suffix):
	global counters
	
	try:
		fil = os.path.join(path,'conf','snap_counters' + suffix + '.csv')
		fp = open(fil)
		counters = fp.readlines()
		fp.close()
	except:

		diag_out('I/O Error: ' + os.path.join(path,'conf','snap_counters' + suffix + '.csv'))

	# strip comment lines
	i = 0
	while (i < len(counters)):
		if counters[i][:1] == '#':
			del counters[i]
		else:
			i += 1

	for i in range(len(counters)):
		s = ''
		counters[i] = counters[i][:-1]		# strip CR/LF
		for tmp in counters[i].split('|'):	# strip lead/trail space
			if (len(s) > 1):
				s = s + '|'
			s = s + tmp.strip()
		counters[i] = s

def diag_out(s):
	lock.acquire()
	print strftime(date_format), app + ':', s
	lock.release()
