# radio.py

from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar

otk = Tk()  #부모 윈도우 위젯 객체 생성
otk.geometry("500x450+400+400") # 단위(픽셀,px)

# 어떤 메뉴를 선택했는지 저장 변수
radio_value = IntVar()     # 정수형 변수 저장객체 생성
radio_value.set(-1)        # 아무것도 선택 안되도록 설정하는 방법
#radio_value.set(-1)        # 정수값 설정        
#val =  radio_value.get()   # 정수값 접근
#print(lunch[val])

lunch = {0:"A런치", 1:"B런치", 2:"C런치", 3:"D런치"}

# variable => 클릭된 버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장된 데이터를 지정하는 변수
orb1 = Radiobutton(otk, text=lunch[0], variable=radio_value, value=0)
orb2 = Radiobutton(otk, text=lunch[1], variable=radio_value, value=1)
orb3 = Radiobutton(otk, text=lunch[2], variable=radio_value, value=2)
orb4 = Radiobutton(otk, text=lunch[3], variable=radio_value, value=3)


def buy():
    print("다음 메뉴를 주문합니다.")
    val =  radio_value.get()   # 정수값 접근
    print(lunch[val])
obtn1 = Button(otk, text="주문" , command=buy) 

# 2.위젯 배치
orb1.pack()
orb2.pack()
orb3.pack()
orb4.pack()
obtn1.pack()

otk.mainloop() 


class Intvar:
    def __init__(self):
        self.int_val = 0

    def set(self, int_val):
        self.int_val = int_val
    
    def get(self):
        return self.int_val