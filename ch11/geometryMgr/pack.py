# pack.py
# from tkinter import *
from tkinter import Tk
from tkinter import Button


# 1. 위젯 생성
otk = Tk()  #부모 윈도우 위젯 객체 생성
otk.geometry("600x550+400+400") # 단위(픽셀,px)


obtn1 = Button(otk, text="PUSH1")  
obtn2 = Button(otk, text="PUSH2")
obtn3 = Button(otk, text="PUSH3")


# 2. 위젯 배치
obtn1.pack(side="left")        
obtn2.pack(side="right")
obtn3.pack(side="bottom")

# 3. 이벤트 및 바인딩


otk.mainloop()     
