#!/usr/bin/env python
# enable debugging
import cgitb; 
cgitb.enable()
import sys, os
#import web



print "Content-type: text/html\r\n\r\n";
print "<font size=+1>Environment</font><\br>";
for param in os.environ.keys():
  print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])


print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
for line in f:
   print(line, end='')
<h2>Homepage!</h2>

</body>
</html>
"""
