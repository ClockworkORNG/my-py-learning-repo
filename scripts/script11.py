import json
person = {"name": "John", "age": 25}
x = json.dumps(person)
print(x)
y = json.loads(x)
print(y)

import datetime
print(datetime.datetime.now())

import re
s = "simple string"
print(s.find("s"))

j = 0
p = 0
while p != -1:
    p = s.find(("st"), j)
    j = p + 1
    if p != -1:
        print(p)

str0 = "sim"
j1 = 0
p1 = 0
while p1 != -1:
    p1 = s.index(str0, j1)
    j1 = p1 + len(str0)
    if p1 != -1:
        print(p1)

while p != -1:
    try:
        p = s.index(str0, j)
    except:
        p = -1
    j = p + 1
    if p != -1:
        print(p)