# file_append.py


print(locale.getdefaultlocale())


f = open(r"ch12\file1.txt","w", encoding="utf-8")

#f.write("hi")


for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)


f.close()

# "r" : raed
# "w" : write
# "a" : append
# "r+" : read + Write => 파일을 읽고 쓰기(기 데이터가 존재) 
# "w+" : write + read => 파일을 새로 만들거나 비우고 쓰고 읽기
# "a+" : append + read