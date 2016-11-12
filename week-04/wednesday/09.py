# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
from tkinter import *
import random

root = Tk()

width = 300
height  = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def squarizer(size):
    colors = ['silver', 'purple', 'gold', 'light blue']
    color = colors[random.randrange(0,4)]
    return canvas.create_rectangle(width/2-size/2,height/2-size/2,width/2+size/2,height/2+size/2, fill=color)

for i in range(3):
    size = random.randrange(1,300)
    squarizer(size)

root.mainloop()
