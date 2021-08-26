import tkinter

window = tkinter.Tk()
window.title("abby's project")
window.geometry("500x500+100+100")
window.resizable(1,1)

label = tkinter.Label(window,text="hi i'm abby",width=10,height=5,fg='red',bg='yellow',relief="solid")
label.pack()

def calc(event):
    label.config(text="result: "+str(entry.get()))

entry = tkinter.Entry(window)
entry.bind("<Return>",calc)
entry.pack()

label = tkinter.Label(window)
label.pack()





# main
window.mainloop()