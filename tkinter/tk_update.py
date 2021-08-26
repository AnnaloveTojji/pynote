# Import the tkinter library
from tkinter import *
from tkinter import ttk
import time

# Create an instance of tkinter frame
win= Tk()

# Set the size of the Tkinter window
win.geometry("700x350")
def add_Text():
   for i in range(10):
      label.config(text= "The loops starts from 1 to "+ str(i))
      # Wait for two seconds
      win.update_idletasks()
      time.sleep(2)
      label.config(text= i)

# Add a label text
label= Label(win, text="Original Text", font= ('Aerial 16'))
label.pack(pady= 30)

# Add a button to update the Label text
ttk.Button(win, text="Change Text", command= add_Text).pack(pady= 40)
win.mainloop()