# create a 300x300 canvas.
# fill it with a checkerboard pattern.
from tkinter import *
import random
import webcolors

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height)
canvas.pack()

def rgb():
    return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])

def squarizer(size, x, y):
    return canvas.create_rectangle(x, y, x+size, y+size, fill=rgb())

size = 3
x = 0
y = 0

for i in range(width//size):
    x = i * size
    for j in range(height//size):
        y = j * size
        squarizer(size, x, y)

root.mainloop()
