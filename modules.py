#!/usr/bin/env python 
# enable debugging

import os, sys
import urllib2
import cgitb

from StringIO import StringIO
cgitb.enable()

def header():


	f = open('modules/header.html', 'r')
	for line in f:
        	print line,

def footer():

	f = open('modules/footer.html', 'r')
	for line in f:
        	print line,

	
def sidebar():
	f = open('modules/sidebar-a.html', 'r')
	for line in f:
		print line,

def modules():
	header()
	sidebar()
	
