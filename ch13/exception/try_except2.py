# try_except2.py
print("try-except2")

path = r"ch13\exception\myfil.txt"

#f = open(path)      # mode 기본값 = 'r'

try :
    f = open(path, 'w+')
    s = f.readline()
    i = int(s.strip())
except FileExistsError:
    print("파일을 찾을 수 없습니다.")
except ValueError:
    print("정수형으로 변환할 수 없습니다.")

print("program exit")