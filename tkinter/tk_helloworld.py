from tkinter import *

# main window obejct, root
root = Tk()

# giving title to the main window
root.title("First_Program")

# Label: output on the window
myLabel1 = Label(root, text="hello world!")
myLabel2 = Label(root, text="my name is abby")
# packing
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)

# mainloop: telling the code to keep displaying
root.mainloop()

