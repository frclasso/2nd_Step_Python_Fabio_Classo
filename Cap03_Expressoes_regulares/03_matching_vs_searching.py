#!/usr/bin/env python3

import re

line = 'Cats are smarter than Dogs'

matchObj = re.match(r'dogs', line, re.M|re.I)

if matchObj:
    print("match --> matchObj.group():",matchObj.group())
else:
    print("No match!")

searchObj = re.search(r'dogs', line, re.M|re.I)

if searchObj:
    print("search --> searchObj.group():",searchObj.group())
else:
    print("Nothing found!")
