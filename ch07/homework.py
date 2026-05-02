# homework.py

# def inner_function(x, y):
#     return x + y # ---------------------> 2
# def outer_function(x, y): #-------------> 3
#     return inner_function(x, y) #-------> 4
# add_10 = outer_function(10, 5) #--------> 1
# print(add_10) #-------------------------> 5

# def add_numbers(a, b):
#     result = a + b
#     return result

# print(result)


# def add_numbers(a, b):
#     result = a + b
#     return result  # 계산 결과를 바깥으로 던짐

# print(add_numbers(3, 4)) # 함수를 호출하고 그 결과를 출력

# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()

# print("A")
# def message() :
#     print("B")
# print("C")
# message()

# def check_odd_even(number):
#     if number % 2 == 0:     
#         return "Even"       
#     else:
#         return "Odd"        

# # 사용 예시
# print(check_odd_even(4))   
# print(check_odd_even(7))   




def calculate_average(num_list):
    total = sum(num_list)
    count = len(num_list)
    return total / count

num_list = [10, 20, 30, 40, 50]
average = calculate_average(num_list)
print("평균: ", average)

