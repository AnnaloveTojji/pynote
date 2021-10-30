from tkinter import *
from tkinter import filedialog

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/Users/kim/kimcode/assets/", 
        title="testing", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf) 
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg']='#fb0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)
ws.mainloop()

'''
Any index that is after the last character is treated as being the end. 
When you insert something into an entry widget that is empty, 
every index is treated as 0. 
Thus, the index is mostly useful for inserting text somewhere into existing text.
'''


