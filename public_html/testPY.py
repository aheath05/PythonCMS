
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# enable debugging
import cgitb; 
cgitb.enable()
import sys
import web


urls = (
  '/', 'index'
)

print "Content-Type: text/plain;charset=utf-8"
print "Hello World!"

f = open('index.html', 'r')
print f
f.read()
for line in f:
	print line,
