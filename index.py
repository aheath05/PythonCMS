#!/usr/bin/env python
# enable debugging
import cgitb; 
cgitb.enable()
#import sys
#import web

print "Content-Type: text/html"
print
print """\
<html>
<body>
<<<<<<< HEAD
<h2>Hello World!</h2>
=======
<h2>Homepage!</h2>
>>>>>>> 9e1bd46a2fa601cb75156832d599ac5a8ac555f9
</body>
</html>
"""

