# create a 300x300 canvas.
# fill it with four different size and color rectangles.
from tkinter import *
import random

root = Tk()

width = 300
height  = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def squarizer(x, y, size):
    colors = ['silver', 'purple', 'gold', 'light blue']
    color = colors[random.randrange(0,4)]
    return canvas.create_rectangle(x-size/2,y-size/2,x+size/2,y+size/2, fill=color)

for i in range(4):
    x = random.randrange(0,250)
    y = random.randrange(0,250)
    size = random.randrange(10,100)
    squarizer(x,y,size)

root.mainloop()

