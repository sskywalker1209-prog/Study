# try_except.py

# 예외 처리 기본 문법
# try:
#     코드블록

# except 예외클라스 :
#     코드블록
# finally : 
#     코드블록



 
# while True:
#     x = int(input("please enter a number"))
#     break



while True:
    try:
        x = int(input("please enter a number"))
        break
    except ValueError :
        print("Oop! That was no valid number. Try agian")
    finally : 
        print("에외 처리 후 동작하는 코드")

print("program exit5")