#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
# enable debugging
import cgitb
import os, sys
import urllib2
import modules

from StringIO import StringIO
cgitb.enable()


def md2html(filename):
  sys.path.append('Markdown-2.5/')
  old_stdout = sys.stdout
  #sys.stdout = open('out.html', 'w')
  result = StringIO()
  sys.stdout = result
  if __name__ == '__main__':
    sys.argv.append(filename)
    from markdown.__main__ import run
    run()
  sys.stdout = old_stdout
  result_string = result.getvalue()
  print result_string


print "Content-Type: text/html;charset=utf-8"
print
print "<html>"

print "        <title>Blue CMS</title>" 
print "		<meta name='viewport' content='width=device-width, initial-scale=1'>"
print "        <link rel='stylesheet' href='home/default.css' />" 
print "        <link rel='stylesheet' href='home/main.css' >"
print "        <link rel='stylesheet' href='home/responsive.css' media='screen' >"


req_uri = os.environ["REQUEST_URI"]
cont_prefix = os.environ["CONTEXT_PREFIX"]
path = r'/var/www/pythoncms.com/content'
data = {}
dir_bool = False
   
site_path = req_uri.replace(cont_prefix, "", 1)
if not site_path == "/" and not site_path.endswith('.md'):
  site_path = site_path+".md"

# For comparing site_path to directories in content folder
for dir_entry in os.listdir(path):
  dir_entry = "/%s" % (dir_entry)
  if site_path == dir_entry:
    dir_bool = True
    break
 
if site_path == "/":
  # call the header and sidebar
  modules.modules()
  md2html("content/index.md")
  modules.footer()
elif dir_bool == True:
  # call the header and sidebar
  modules.modules()
  md2html("content"+site_path)
  modules.footer()
else:
  modules.header()
  print "<div style=\"height:400px;text-align:center;\">    <h5>      <em style='color:#2F7288; '>        The page you requested does not exsist or you do not have permission to view it.<br/>        If neither of these are true please contact the server administrator.      </em>    </h5>  </div>"
  modules.footer()

print "</html>"
