# py2.py

path = r"ch12/계좌1.txt"
mode = "r"

f = open(path, 'r', encoding="utf-8")

account_list = []

lines = f.readlines()

for line in lines:
    data = line.split()     
    account_list.append(data[1])

    f.close()

print(account_list)