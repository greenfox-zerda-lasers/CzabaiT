from tkinter import *
import math
import time


root = Tk()
size = 600
canvas = Canvas(root,width=size, height=size, bg='white')
canvas.pack()

height = math.sqrt(3)/2

def hexagonal(x,y,length):
    time.sleep(0.03)
    canvas.create_polygon(x+length/2, y, x+3/2*length, y, x+2*length, y+length*height, x+3/2*length, y+2*(length*height), x+length/2, y+2*(length*height), x, y+(length*height), fill='white', outline='black')
    canvas.update()
    if length > 5:
        hexagonal(x+length/3, y, length/3)
        hexagonal(x+length, y, length/3)
        hexagonal(x+2/3*length, y+(2*length*height)/3, length/3) #CENTER
        hexagonal(x+4/3*length, y+(2*length*height)/3, length/3)
        hexagonal(x+length, y+2*((2*length*height)/3), length/3)
        hexagonal(x+length/3, y+2*((2*length*height)/3), length/3)
        hexagonal(x, y+(2*length*height)/3, length/3)

hexagonal(0, 0, 100)

root.mainloop()