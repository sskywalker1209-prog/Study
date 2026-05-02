#founc1.py

# 함수 정의
# def 함수명():
#     코드블록
#     return 반환값

# 기능/동작: 토끼에게 인사
# def my_fun():
#     print("토끼야 안녕!")

# #호출(사용)
# my_fun()

# letters = "ABCDE"
# for i in range(6):
#     for j in range(i):            
#         print(letters[j],end="") 
#     print()                       




# for i in range(1, 6):
#     for j in range(i):          
#         print(letters[j], end=" ")
#     print()                   

MyName = ""

while True:
    print("이름을 입력하세요")
    MyName = input()
    
    # 1. 이름이 틀리면 다시 처음으로 돌아간다 (continue)
    if MyName != 'hongkildong':
        continue
        
    print("패스워드를 입력하세요")
    MyPass = input()
    
    # 2. 패스워드가 맞으면 반복문을 탈출한다 (break)
    if MyPass == 'hahaha':
        break

print("확인되었습니다")