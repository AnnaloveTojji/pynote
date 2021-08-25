from tkinter import *

root = Tk()
root.title("my first project")

e = Entry(root, width=50,bg="blue", fg="white")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_add():
    return

button_1=Button(root,text="1",padx=40,pady=20,command=button_add)

button_1.grid(row=1,col=1)

# def mclick():
#     hello = "hello" + e.get()
#     myLabel1 = Label(root, text=hello)
#     myLabel1.pack()



myButton = Button(root, text="enter your name", padx=50, pady=50,
 command=mclick, fg="blue", bg="red")
myButton.pack()



root.mainloop()