# homework.py

# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0]

# print(arr)

# a = [3, 6, 7, 4, 9, 10, 13]
# for x in a:
#     x % 2 == 1 
    



# a = [3, 6, 7, 4, 9, 10, 13]

# for i in range(len(a)):
#     if a[i] % 2 == 0 :
#         first_even = i
#         break

# for i in range(len(a)-1,-1,-1):
#     if a[i] % 2 != 0:
#         last_odd = i
#         break

# a[first_even], a[last_odd] = a[last_odd], a[first_even]

# print(a)

# a = [3, 6, 7, 4, 9, 10, 13]
# max_val = a[0]
# for i in range(len(a)):
#     if a[i] > max_val :
#         max_val = a[i]

# print(max_val)

# 10. 주어진 딕셔너리에서 모든 값의 합을 구하는 함수를 작성하세요. 
# ( 예를 들어, 딕셔너리 { 'a': 10, 'b': 20, 'c': 30 }가 주어졌을 때, 합은 60 )

# d = { 'a': 10, 'b': 20, 'c': 30 }

# def sum_values(d):
#     total = 0

#     for value in d.values() :
#         total += value
#     return total
    
# print(sum_values(d))

# # 점수가 80 이상인 사람 이름만 출력해라
# scores = {
#     "민수": 75,
#     "영희": 92,
#     "철수": 88
# } 
# # for name, score in scores.items():
# #     if score >= 80:
# #         print(name)

# # resule = [score for name, score in scores.items() ]
# # print(resule)

# result = [name for name, score in scores.items() if score >= 80 ]
# print(result)

# passed = [(name, score) for name, score in scores.items() if score >= 80]
# print(passed)

