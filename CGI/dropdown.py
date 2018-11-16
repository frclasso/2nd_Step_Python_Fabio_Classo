#!/usr/bin/env python3

import cgi, cgitb

# Create instance of FieldStorage

form = cgi.FieldStorage()

# Get data from fields

if form.getvalue('dropdown'):
    subject = form.getvalue('dropdown')
else:
    subject = "Not entered"

print("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<title>DropDown - Sixth CGI Promgram.</title>")
print("</head>")
print("<body>")
print("<h2>Selected subject is: %s </h2>" % subject)
print("</body")
print("</html>")