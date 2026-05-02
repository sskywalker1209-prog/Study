# homework2.py

# a = 3.14
# b = True
# c = "False"

# print(type(a))
# print(type(b))
# print(type(c))

# num1 = int(input("첫 번째 숫자를 입력하세요: "))
# num2 = int(input("두 번째 숫자를 입력하세요: "))

# print("덧셈:", num1 + num2)
# print("뺄셈:", num1 - num2)
# print("곱셈:", num1 * num2)
# print("나눗셈:", num1 / num2)



# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# elif score >= 70:
#     print("C학점")
# else:
#     print("F학점")

# fruits = ['banana', 'peach', 'lemon', 'grape']
# print(fruits[2])


# student3 = {"나이": 22, "직업": "학생", "취미": "게임"}
# student3["도시"] = "수원"   
# print(student3.keys())      


# Numbers = [1, 2, 3, 4, 5]

# for num in Numbers:
#     print(num)


# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']

# for fruit in fruits:
#     print('fruit')
#     if fruit == '사과':
#         print("사과를 찾았습니다.")



# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']

# for fruit in fruits:
#     print(fruit)
#     if fruit == '사과':  # 방금 꺼낸 과일이 사과인지 검사!
#         print("사과를 찾았습니다!")



# def solution(a, b):
#     sum = a + b
#     sub = a - b
#     multi = a * b
#     return sum, sub, multi


# def sum(n):
#     total = 0                   
#     for i in range(1, n + 1):   
#         total = total + i        
#     return total                

# print(sum(10))





def sum_to_n(n):
    total = 0                    
    for i in range(1, n + 1):      
        print(f"{total} + {i} = {total + i}")
        total = total + i
        
    return total                 

# 함수를 호출해 봅니다.
sum_to_n(5)