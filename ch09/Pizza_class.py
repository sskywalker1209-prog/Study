# Pizza_class.py

# class 클래스명:
#     # 1. 맴버변수
#     변수명 = 속성값
#     # 2. 맴버함수(매서드)
#     def 함수명(self,매개변수):
#         self.맴버변수 = 속성값
#         return 반환값

# 빈 클래스
# class 클래스명:
#     pass


# 클래스 정의 (기억)
class Pizzaclass:
    def order(self):
        print("주문하다.")
        self.kind = 10

# 객체 생성 (클래스 사용)
na = Pizzaclass()

na.order()       # 객체.매서드()
print(na.kind)   # 객체.맴버변수


name = "시율"
print(name + "님 안녕하세여.")
print(f"{name}님 안녕하세요")
