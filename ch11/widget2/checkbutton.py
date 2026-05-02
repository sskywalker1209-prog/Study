# checkbutton.py

from tkinter import Tk
from tkinter import Button
from tkinter import BooleanVar
from tkinter import Checkbutton

otk = Tk()  #부모 윈도우 위젯 객체 생성
otk.geometry("500x450+400+400") # 단위(픽셀,px)

coffee = {0:"아메리카노",
          1:"라떼",
          2:"카푸치노",
          3:"에스프레소"}
check_value = {}


for i in range(len(coffee)):
    check_value[i] = BooleanVar()

# check_value1.set(True)
# val = check_value1.get

# oncheckbutton3 = Checkbutton(otk, text =coffee[2], variable=check_value[0])
# oncheckbutton1 = Checkbutton(otk, text =coffee[0], variable=check_value[1])
# oncheckbutton4 = Checkbutton(otk, text =coffee[3], variable=check_value[2])
# oncheckbutton2 = Checkbutton(otk, text =coffee[1], variable=check_value[3])
for i in range(len(coffee)):
    oncheckbutton = Checkbutton(otk, text =coffee[i], variable=check_value[i])
    oncheckbutton.pack()

def buy():
    print("다음 메뉴를 주문합니다.")
    for i in range(len(coffee)):
        if check_value[i].get():
            print(coffee[i])
          
obtn1 = Button(otk, text="주문" , command=buy) 

# oncheckbutton1.pack()
# oncheckbutton2.pack()
# oncheckbutton3.pack()
# oncheckbutton4.pack()
obtn1.pack()

otk.mainloop() 