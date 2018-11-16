#!/usr/bin/env python3

import cgi, cgitb

# Create instance of FieldStorage

form = cgi.FieldStorage()

# Get data from fields

if form.getvalue('subject'):
    subject = form.getvalue('subject')
else:
    subject = "Not set"

print("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<title>Radio - Fourth CGI Promgram.</title>")
print("</head>")
print("<body>")
print("<h2>Selected subject is: %s </h2>" % subject)
print("</body")
print("</html>")