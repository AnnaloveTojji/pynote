import tkinter as tk
import sys

def exit():
    sys.exit(0)

root = tk.Tk()
root.wm_withdraw()
for i in range (10):
    top = tk.Toplevel(root)
    top.title("Window %s" % i)
    label = tk.Label(top, text="This is toplevel #%s" % i)
    button = tk.Button(top, text="exit", command=exit)
    label.pack()
    button.pack()

root.mainloop()