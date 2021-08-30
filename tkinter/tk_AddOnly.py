from tkinter import *
root = Tk()
root.title("더하기 계산기")
# 더하기 기능, 함수
# 버튼: 입력,출력,더하기
def button_add():
    num1 = e1.get()
    num2 = e2.get()
    e3.insert(0,int(num1)+int(num2))
l1 = Label(root,text="더하기만 할 수 있음")
l1.pack()
e1 = Entry(root,width=35)
e1.pack()
e2 = Entry(root,width=35)
e2.pack()
b1 = Button(root,width=35, highlightbackground="green",command=button_add)
b1.pack()
e3 = Entry(root,width=35)
e3.pack()
# 더하기 함수

root.mainloop()