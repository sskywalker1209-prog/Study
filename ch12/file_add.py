# file_add.py

path = r"ch12\file1.txt"
mode = "a"
f = open(path, mode,  encoding="utf-8")

for i in range(11,21):
    date = "%d번째 줄입니다.\n" %i
    f.write(date)

f.close()


f = open(path,'r',encoding='utf-8')
print(f.read())
f.close()