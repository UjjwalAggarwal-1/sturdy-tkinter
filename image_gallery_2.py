from tkinter import *
from PIL import Image, ImageTk

imgs = [
    "C:\\Users\\HP\\Pictures\\New folder\\3q4asb3jbqf71.jpg",
    "C:\\Users\\HP\\Pictures\\New folder\\8ed6544e-89d0-4921-a56d-a3f4bced1084.jpg",
    "C:\\Users\\HP\\Pictures\\New folder\\Floating Islands - Justin Donaldson, Gouache, 2020.jpg",
]

root = Tk()
root.title('learn')

cur_page = 0

img1 = ImageTk.PhotoImage(Image.open(imgs[0]).resize((300,300)))
l1 = Label(image=img1)

img2 = ImageTk.PhotoImage(Image.open(imgs[1]).resize((300,300)))
l2 = Label(image=img2)

img3 = ImageTk.PhotoImage(Image.open(imgs[2]).resize((300,300)))
l3 = Label(image=img3)

img_dict = {
    0:l1, 1:l2, 2:l3,
}
img_dict.get(cur_page).grid(row=0,column=0,columnspan=3)

def previmg():
    global cur_page
    cur_page -=1
    if cur_page <0:
        cur_page += 3
    imin=img_dict.get(cur_page)
    imin.grid(row=0,column=0,columnspan=3)

def nextimg():
    global cur_page
    cur_page +=1
    cur_page %= 3
    imin=img_dict.get(cur_page)
    imin.grid(row=0,column=0,columnspan=3)

Button(root, text="<<",command=previmg).grid(row=1,column=0)
Button(root, text="exit", command=root.quit).grid(row=1,column=1)
Button(root, text=">>",command=nextimg).grid(row=1,column=2)

root.mainloop()