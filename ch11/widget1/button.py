# button.py
# from tkinter import *
from tkinter import Tk
from tkinter import Button


# 1. 위젯 생성
otk = Tk()  #부모 윈도우 위젯 객체 생성
otk.geometry("100x150+400+400") # 단위(픽셀,px)


def hello1():
    print("버튼 1번이 눌렸음")
def hello2():
    print("버튼 2번이 눌렸음")
def hello3():
    print("버튼 3번이 눌렸음")

# 자식 위젯 객체 생성
# obtn1 = Button(otk, text="PUSH1" , command=hello1)  # 자식 위켓 객체 새성
# obtn2 = Button(otk, text="PUSH2" , command=hello2)
# obtn3 = Button(otk, text="PUSH3" , command=hello3)
obtn1 = Button(otk, text="PUSH1" , command=hello1)  
obtn2 = Button(otk, text="PUSH2" , command=hello2)
obtn3 = Button(otk, text="PUSH3" , command=hello3)
# 2. 위젯 배치
obtn1.pack()         # 위젯 배치
obtn2.pack()
obtn3.pack()

# 3. 이벤트 및 바인딩
# 누름(버튼 이벤트) 발생시, 특정 동작이 수행(바인딩) 
otk.mainloop()      # 주요 반복구조 부모 위젯 실행
