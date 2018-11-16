#!/usr/bin/env python3

import cgi, cgitb

# Create a instance of FieldStorage
form = cgi.FieldStorage()

# Get data  form fields

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "Not entered"

print("Content-type: text/html")
print()
print("<html>")
print("<head>")
print("<title>Text Area - Fifth CGI Program.</title>")
print("</head>")
print("<body>")
print("<h2>Entered text content is : %s </h2>" % text_content)
print("</body")
print("</html>")