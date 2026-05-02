# Human.py

class Human:
    eyes = 2
    nose = 1
    mouth = 1
    def __init__(self, age, name):
        # 인스턴스 변수
        self.age = age
        self.name = name

    #기능 : 자기소개 하다
    def introduce(self):
        print(str(self.age)+"살", end =" ")
        print(str(self.name + "입니다."))

    def sleep(self):
        print("자다")
    def talk(self):
        print("말하다")
    def eat(self, food):
        self.food = food
        print(self.food + "먹다")
       
print("눈 개수: " , Human.eyes)

kim = Human(29, "김시율")
kim.introduce()
kim.eat("피자")
lee = Human(45, "이시율")
lee. introduce()







