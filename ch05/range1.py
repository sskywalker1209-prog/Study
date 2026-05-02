# range1.py

nums = range(10)
print(nums)
print(type(nums))
print(type(list(nums)))


print('---------------')
print(range(10))
print(list(range(10)))

print('---------------')
print(range(5))
print(list(range(5)))

print('---------------')
print(range(1,5))
print(list(range(1,5)))

print('---------------')
print(range(2,9,2))
print(list(range(2,9,2)))

print('---------------')
for num in range(3) : 
    print('안녕','거북이',num)

print('---------------')
for num in range(1,5) : 
    print('안녕','거북이',num)

print('---------------')
for num in range(1,5,2) : 
    print('안녕','거북이',num)


print('-------튜플-------')
fruits = ('사과','배','바나나','망고')

print('내가 좋아하는 과일')
for fruit in fruits:
    print(fruit)