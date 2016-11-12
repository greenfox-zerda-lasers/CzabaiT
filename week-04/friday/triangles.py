from tkinter import *
import math
import time


root = Tk()
size = 600
canvas = Canvas(root ,width=size, height=size, bg='white')
canvas.pack()

def triangles(x,y,length):
    time.sleep(0.03)
    canvas.create_polygon(x, y, x+length, y, x+length/2, y+(length/2*math.sqrt(3)), fill='white', outline='black')
    canvas.update()
    if length > 5:
        triangles(x, y, length/2)
        triangles(x+length/2, y, length/2)
        triangles(x+(length/2)/2, y + ((length/2*math.sqrt(3)))/2, length/2)

triangles(0, 0, 600)

root.mainloop()