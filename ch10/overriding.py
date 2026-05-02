# overriding.py

class Animal:
    def eat(self):
        print("먹다.")
    def move(self):
        print("이동하다.")
    def sound(self):
        print("소리내다.")
    

class Cat(Animal):
    def eat(self):
        print("잡식하다.")
    def sound(self): 
        print("야옹~ " , end="")
        super().sound()

dog = Animal()
taiger = Animal()
lion = Animal()

dog.eat()
dog.sound()

print('----------------------')

cat1 = Cat()
cat1.eat()
cat1.sound()