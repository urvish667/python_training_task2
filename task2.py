#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

def wordFinder(str):
    if "cal" in str: 
        return "cal"
    elif "date" in str:
        return "date"
    else:                                                                                                        return None
    
y = cgi.FieldStorage()
value = y.getvalue("x")

if "run" in value  or "execute" in value:
    if(wordFinder(value)!=None):
        x = subprocess.getoutput(wordFinder(value))
else:
    x = "Enter valid command"
print(x)
