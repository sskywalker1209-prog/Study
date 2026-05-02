# bindEvent.py

from tkinter import Tk
from tkinter import Button
from tkinter import Label


# 1. 위젯 생성
otk = Tk()  #부모 윈도우 위젯 객체 생성
otk.geometry("500x450+400+400") # 단위(픽셀,px)


def order():
    print("주문합니다.")

olabel1 = Label(otk, text="치즈버거")
olabel2 = Label(otk, text="불고기버거")
olabel3 = Label(otk, text="새우버거")

olabel1.pack()         # 위젯 배치
olabel2.pack()
olabel3.pack()

obtn = Button(otk, text="주문" , command=order)
obtn.pack() 

otk.mainloop() 