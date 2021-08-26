import tkinter

window = tkinter.Tk()
window.title("my tk project")
window.geometry("500x500+100+100")
window.resizable(1,1)

listbox = tkinter.Listbox(window,selectmode='extended',height=0)
listbox.insert(0,"1번")
listbox.insert(1,"2번")
listbox.insert(2,"2번")
listbox.insert(3,"2번")
listbox.insert(4,"3번")
listbox.delete(1,2)
listbox.pack()




# main
window.mainloop()