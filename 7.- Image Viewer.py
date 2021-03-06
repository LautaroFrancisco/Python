from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Poggies")

my_img1 = ImageTk.PhotoImage(Image.open("Images/testing.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/testing1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/testing2.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/testing3.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/testing4.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

status = Label(root,text= "Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

def foward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command= lambda: foward(image_number + 1))
    button_back = Button(root,text="<<",command= lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root,text=">>", state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root,text= "Image " + str(image_number) + " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command= lambda: foward(image_number + 1))
    button_back = Button(root,text="<<",command= lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root,text="<<",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root,text= "Image " + str(image_number) + " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_back = Button(root,text="<<",command=back,state=DISABLED)
button_forward = Button(root,text=">>",command= lambda:foward(2))
button_exit = Button(root,text="Exit Program",command=root.quit)

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
