# 14homework.py

import re

# text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"

# pattern = r"[\w.-]+@[\w.-]+\.\w+"

# result = re.findall(pattern,text)

# print(result)

# print("-----------------------")

# text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"

# pattern = r"\d{2,3}-\d{3,4}-\d{4}"

# result = re.findall(pattern,text)

# print(result)

# print("-----------------------")

# text = "I love Python. Java is also popular. Python is great for AI."

# pattern = r"[^.]*Python[^.]*\."


# result = re.findall(pattern,text)

# print(result)

# print("-----------------------")

# text = "상품 코드: A123, B456, C789, 가격: 12000원"

# pattern = r"\d+"

# result = re.findall(pattern,text)

# print(result)


print("-----------------------")

text = "NASA is working on AI projects with IBM and Google."

pattern = r"\b[A-Z]{2,}\b"

result = re.findall(pattern,text)

print(result)