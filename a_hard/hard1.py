# # hard1.py
# result = []

# for x in range(1, 6):
#     result.append(x * x)
# print(result)


# result = [x*x for x in range(1, 6)]
# print(result)


# evens = []



# nums = [1, 2, 3, 4, 5, 6]

# for x in nums:
#     if x % 2 == 0:
#         evens.append(x)

# print(evens)


# evens = [x for x in nums if x % 2 == 0]
# print(evens)


# nums = [1, 2, 3, 4]
# result = []

# for x in nums:
#     result.append(x * 2)

# print(result)

# result = [x * 2 for x in nums]
# print(result)


# result = list(map(lambda x : x * 2, nums))
# print(result)


# nums = list(range(1, 11))
# result = []

# result = [x*x for x in nums if x % 2 == 0]
# print(result)

# scores = {
#     "민수": 75,
#     "영희": 92,
#     "철수": 88,
#     "지연": 60
# }

# for name, score in scores.items():
#     if score >= 80:
#         print(name, score)


# passed = [(name, score) for name, score in scores.items() if score >= 80]
# print(passed)




# switch = False
# if not switch :
#     switch = True

# if switch :
#     print ("ON")
# else:
#     print ("OFF")

# a = (1,2,3)

# b = list(a)

# # b.insert(0,7)

# a = tuple(b)
# print(a)

# a = (7,) + a
# print(a)


# # my_tuple = ('사과', '바나나', '포도')
# # print(my_tuple[1])

# # print(my_tuple[1])
# # 딕셔너리 clover = {'나이': 27, '직업': '병사'}에서 나이의 값을 28로 

# clover = {'나이': 27, '직업': '병사'}
# clover['나이'] = 28
# print(clover)

# clover['나이'] = 28

# for i in range(1, 10, 2):
#     print(i)

# def count_down(n):
#     if n == 0:
#         print("완료!")
#         return
    
#     print(n)
#     count_down(n-1)

# count_down(5)




# def count_down(c) :
#     if c == 0 :
#         print("완료")
#         return
    
#     count_down(c-1)
#     print(c)

# count_down(5)




# def count_down(n):
#     if n == 0 :
#         print("완료")
#         return
    
#     count_down(n-1)
#     print(n)

# count_down(5)


# def check_even(Nums):
#     for n in Nums:
#         if n % 2 == 0:
#             return n

# print(check_even([1,2,3,4,5,6,7,8]))

# x = 10

# def test():
#     return x + 5

# test()

# x = 10

# def test():
#     x = x + 5   # ← 값 바꿈

# test()


# x = 10

# # def test():
# #     print(x)   # 출력하지만 읽기만 함

# # test()

# # x = 10

# # def test():
# #     print(x)
# #     x = 20

# # test()

# x = 10

# def test():
#     return x + 5

# print(test())


# def test():
#     x = 5
#     return x

# print(test())

a = {1: '월', 2: '화'}

# a[10] = a[1]
# del a[1]

# print(a)


a={10:a[1], 2:a[2]}
print(a)
