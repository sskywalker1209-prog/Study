# Bag.py

# 클래스 : 가방
# 객체 : 숄더백 , 백팩 ...
# 속성 : 재질, 색, 무게, 브랜드
# 기능 : 넣다, 꺼내다, 꾸미다

class Bag:
    # 클래식 맴버 변수
    call_name = "가방"

    # 맴버함수 (메서드)
    def info(self):
        #인스턴스 맴버변수
        self.kind = ""
        self.color = ""
        self.data = []

    def add(self,x):
        self.data.append(x)
    
    def addtwice(self,x):
        self.add(x)
        self.add(x)



sholder = Bag()

print(sholder.call_name)   # 클래스 변수 출력

sholder.info()             # 👈 이게 핵심 (data 생성)

sholder.add("휴대폰")
sholder.addtwice("돈")

print(sholder.data)