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
<h2>Page2 inside html folder</h2>
</body>
</html>
"""
print """\
A First Level Header
====================

A Second Level Header
---------------------

Now is the time for all good men to come to
the aid of their country. This is just a
regular paragraph.

The quick brown fox jumped over the lazy
dog's back.

### Header 3

> This is a blockquote.
> 
> This is the second paragraph in the blockquote.
>
> ## This is an H2 in a blockquote
"""

