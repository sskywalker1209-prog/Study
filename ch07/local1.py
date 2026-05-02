# local1.py

b = 0
print("b값:" ,b)

b=1 
print("b값:", b)

def scope_test():
    a = 1            # 지역변수 선언
    print("함수 안 a:", a)

a = 0                #전역변수 선언
print("함수 밖 a:", a)
scope_test()

print("함수 호출 후 a:", a)

