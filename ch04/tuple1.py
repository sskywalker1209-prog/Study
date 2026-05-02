# tuple1.py

clovers = ('클로버1','클로버2','클로버3')
print(clovers[1])

print(clovers)
print(type(clovers))

my_tuple1 = ()
print(my_tuple1)

my_tuple2 = (1, -2, 3.14, True, 'hi', [1,2])
print(my_tuple2)
my_tuple2[5][1] = 3
print(my_tuple2)

print('------------------------------')
my_list1 = list(my_tuple2)
print(my_list1)

my_list1[3] = False
print(my_list1)