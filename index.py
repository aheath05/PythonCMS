#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
# enable debugging
import cgitb
import os
import urllib2
import get_markdown
cgitb.enable()


print "Content-Type: text/html;charset=utf-8"
print
print "<html>"
   
req_uri = os.environ["REQUEST_URI"]
cont_prefix = os.environ["CONTEXT_PREFIX"]
path = r'/var/www/sites/pythoncms.com/content'
data = {}
dir_bool = False
   
site_path = req_uri.replace(cont_prefix, "", 1)


for dir_entry in os.listdir(path):
  dir_entry = "/%s" % (dir_entry)
  if site_path == dir_entry:
    dir_bool = True
    break
    
if site_path == "/":
  f = open("content/index.html")
  file_contents = f.read()
  print (file_contents)
  f.close()
#elif dir_bool == True and dir_entry.endswith('.jpg'):
#  urllib2.urlopen("http://pythoncms.com/content"+dir_entry)
elif dir_bool == True and dir_entry.endswith('.md'):
  content = get_markdown.md2html("content"+dir_entry)
  print (content)
elif dir_bool == True:
  f = open("content"+dir_entry, 'r')
  file_contents = f.read()
  print (file_contents)
  f.close()
else:
  print "Broken Link"



# Uncomment the two lines below to see all web variables for this page request
#
      
#for param in os.environ.  keys():
#  print "<p><b>%20s</b>: %s</p>" % (param, os.environ[param])
                 
print "</html>"