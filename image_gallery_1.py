from tkinter import *
from PIL import Image, ImageTk

imgs = ["C:\\Users\\HP\\Pictures\\New folder\\3q4asb3jbqf71.jpg",
"C:\\Users\\HP\\Pictures\\New folder\\8ed6544e-89d0-4921-a56d-a3f4bced1084.jpg",
"C:\\Users\\HP\\Pictures\\New folder\\Floating Islands - Justin Donaldson, Gouache, 2020.jpg"
]

root = Tk()
root.title('learn')

img1 = ImageTk.PhotoImage(Image.open(imgs[0]).resize((300,300)))
l1 = Label(image=img1)

img2 = ImageTk.PhotoImage(Image.open(imgs[1]).resize((300,300)))
l2 = Label(image=img2)

img3 = ImageTk.PhotoImage(Image.open(imgs[2]).resize((300,300)))
l3 = Label(image=img3)

def nextimg():
    global pg_num
    print(pg_num)
    global imglab
    if pg_num in [0,1]:
        pg_num += 1
    if pg_num in [2]:
        pg_num = 0
    imglab=imgdict.get(pg_num).grid(row=0,column=0,columnspan=3)

def previmg():
    global pg_num
    global imglab
    if pg_num in [1,2]:
        pg_num -= 1
    if pg_num in [0]:
        pg_num = 2
    imglab=imgdict.get(pg_num).grid(row=0,column=0,columnspan=3)

imgdict = {
    0:l1, 1:l2, 2:l3,
}
try:
    imglab=imgdict.get(pg_num)
except NameError:
    imglab=imgdict.get(0)
imglab.grid(row=0,column=0,columnspan=3)

Button(root, text="<<",command=previmg).grid(row=1,column=0)
Button(root, text="exit", command=root.quit).grid(row=1,column=1)
Button(root, text=">>",command=nextimg).grid(row=1,column=2)

root.mainloop()