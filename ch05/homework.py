# homework.py

# 과일 = ["사과","귤","수박"]
# for 변수 in 과일 :
#     print(변수)

# 변수 = [10,20,30]
# for num in 변수:
#     print(num)

# 가격리스트 = [100, 200, 300]
# for num in 가격리스트 :
#     print(num + 10)

# 리스트 = ['dog', 'cat', 'parrot']
# for animal in 리스트:
#     print(animal,len(animal))

# 리스트 = ["가", "나", "다", "라"]
# for kor in 리스트[1:] :
#     print(kor) 

# 리스트 = [3, -20, -3, 44]
# for m in 리스트 :
#     if m < 0:
#         print(m)

# for year in range(2002, 2051, 4) :
#     print(year)

# 숫자 = 1
# 합 = 0
# while 숫자 <= 100 :
#     합 = 숫자 + 합
#     숫자 = 숫자 + 1
# print(합)

# for num in range(1,31):
#     if num % 2 == 1:
#         print(num,'홀수')
#     else:
#         print(num,'짝수')

홀수리스트 = []
짝수리스트 = []

for num in range(1,31):
    if num % 2 == 1:
      홀수리스트.append(num)
    else:
        짝수리스트.append(num)

print('홀수:', 홀수리스트)
print('짝수:', 짝수리스트)