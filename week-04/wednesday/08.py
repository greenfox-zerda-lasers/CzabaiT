# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
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
    return canvas.create_rectangle(x,y,x+size,y+size, fill=color)

for i in range(4):
    x = random.randrange(0,250)
    y = random.randrange(0,250)
    size = 50
    squarizer(x,y,size)

root.mainloop()