#!/usr/bin/env python 
# enable debugging

import os, sys
import urllib2
import cgitb

from StringIO import StringIO
cgitb.enable()

def header():


	f = open('content/modules/header.html', 'r')
	for line in f:
        	print line,

def footer():

	f = open('content/modules/footer.html', 'r')
	for line in f:
        	print line,

	
def sidebar():
	f = open('content/modules/sidebar-a.html', 'r')
	for line in f:
		print line,
