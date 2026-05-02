# re1.py

# re = compile

# p = re.compile("[abc]")
# m = p.match("a")

import re

p = re.compile("a[.]b")
print(p.match("aab"))
print(p.match("a.b"))
        
print("-----------------")

p = re.compile("a*")
print(p.match('apple'))
print(p.match('aaapple'))

p = re.compile("ca*t")
print(p.match('ct'))
print(p.match('cat'))
print(p.match('caaat'))

