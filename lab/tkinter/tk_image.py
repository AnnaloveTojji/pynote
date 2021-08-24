from tkinter import *
from Pillow import ImageTk, Image

root = Tk()
root.title('my project')
#root.iconbitmap('/Users/kim/kimcode/assets/')

# images to display
my_img1 = ImageTk.PhotoImage(Image.open("/Users/kim/kimcode/assets/sadness.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("/Users/kim/kimcode/assets/joy.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("/Users/kim/kimcode/assets/anger.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("/Users/kim/kimcode/assets/inside_out.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("/Users/kim/kimcode/assets/bingbong.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]


my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

# button functions
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda: back(image_number-1))
    
    my_label.grid(row=0,column=0,comlumnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.gird(row=1, column=2)



def back():
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    buttom_back=Button(root,text="<<",command=lambda: back(image_number-1))
    my_label.grid(row=0,column=0,comlumnspan=3)

    my_label.grid(row=0,column=0,comlumnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.gird(row=1, column=2)



# control buttons
button_back = Button(root, text="<<",command=back)
button_exit = Button(root,text="EXIT", command=root.quit)
button_forward=Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

# exit button
button_quit = Button(root, text='exit', command=root.quit)
button_quit.pack()

# mainloop
root.mainloop()