from tkinter import *
import time
import random
import webcolors

root = Tk()
size = 600
canvas1 = Canvas(root,width=size, height=size, bg="black")
canvas1.pack()
def rgb():
   return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])
def nervtangle(x,y,size):
    time.sleep(0.03)
    canvas1.create_rectangle(x,y,x+size,y+size, outline=rgb())
    canvas1.update()
    if size > 20:
        nervtangle(x,y+size/3,size/3)
        nervtangle(x+(size*(2/3)),y+size/3,size/3)
        nervtangle(x+size/3,y,size/3)
        nervtangle(x+size/3,y+(size*(2/3)),size/3)

nervtangle(0,0,600)

root.mainloop()