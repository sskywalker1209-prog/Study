# homework9.py

class Phone:
     def __init__(self, 제조사, 출고년도, 색상):
         self.제조사 = 제조사
         self.출고년도 = 출고년도
         self.색상 = 색상

     def info(self):
         print("제조사: ",self.제조사)
         print("출고년도:", self.출고년도)
         print("색상:", self.색상)
         
     def setInfo(self, maker, year, color):
         self.maker = maker
         self.year = year
         self.color = color
          


my_phone = Phone("아이폰", 2026, "화이트")
my_phone.info()



