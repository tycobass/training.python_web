#!/usr/bin/env python
import cgi
import cgitb
from functools import reduce

cgitb.enable()

form = cgi.FieldStorage()
stringval = form.getvalue('a', None)
listval = form.getlist('b')

listint = [map(int, x) for x in listval]
result = [reduce(lambda x, y: x+y, l) for l in listint]
#result = [sum(b) for b in listint]
#result = reduce( (lambda x, y: x * y), listint )

print("Content-type: text/plain")
print()
print("Your job is to make this work")
print(result)
print (listval)
print (listint)
