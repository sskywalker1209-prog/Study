# slash.py

import re

# 패턴객체 = re.compile("정규표현식")
# 패턴객체.match('대상문자열')

p = re.compile("\section")
print(p.match('\section python hello thanks'))