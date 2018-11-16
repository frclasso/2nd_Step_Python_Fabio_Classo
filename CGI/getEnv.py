#!/usr/bin/env python3

import os

print("Content-type: text/html")
print()
print("<font size=+1>Environment</font></br>")
for param in os.environ.keys():
    print("<b>%20s</b>: %s</br>" % (param, os.environ[param]))