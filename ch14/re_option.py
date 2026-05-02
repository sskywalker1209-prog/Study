# re_option.py

import re

p = re.compile("a.b", re.DOTALL)
print(p.match("a\nb"))


print("-------------------")

p = re.compile("[a-z]+", re.I)
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))

print("-------------------")

p = re.compile("[a-z]+", re.M)