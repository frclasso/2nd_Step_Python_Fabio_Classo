#!/usr/bin/env python3

import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program.</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s </h2>"%(first_name, last_name))
print("</body>")
print("</html>")
