# Human.py


class Human:
    # 1. 맴버변수
    eyes = 2    #클래스 함수
    nose = 1
    mouth = 1
    # 2. 맴버함수(매서드)
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print("이름:" , self.name)
        print("나이:" , self.age)
    def eat(sefl):
        print("먹다")
    def sleep(self):
        print("자다")
    def talk(self):
        print("말하다")

class Student(Human):
    # 1. 맴버변수(속성)
    # 2. 맴버함수(매서드, 기능/동작)
    def __init__(self,name,age, studentNum):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        
        self.studentNum = studentNum
    def introduce(self):
        # print("이름:" , self.name)
        # print("나이:" , self.age)
        super().introduce()
        print("학번:" , self.studentNum)
    def study(self):
        print("공부하다")

print("눈의 개수:" ,Human.eyes) 
lee = Human("이시율",36)
print(lee.name)
lee.introduce()
lee.eat()

print("-----------------")
print("눈의 개수:" , Student.eyes)
print("코의 개수:" , Student.nose)

kim = Student("김수로",56,123456)
print(kim.name)
kim.introduce()
kim.eat()
print(kim.studentNum)