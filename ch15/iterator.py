# iterator.py

class MyIterator:
    

    def __init__(self, data):
        self.data = data
        self.position = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self. position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.data[self.position]
        self.position +=1
        return result

i = MyIterator([1,2,3])


print(next(i))
print(next(i))
print(next(i))
print(next(i))

# print(type(i))

# for item in i:
#     print(item)
