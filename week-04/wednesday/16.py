# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random

root = Tk()

width = 300
height  = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()



def stardustizer(x, y):
    colors = ['silver', 'grey', 'light grey', 'dark grey']
    color = colors[random.randrange(0, 4)]
    return canvas.create_rectangle(x, y, x+size, y+size, fill=color)

size = 3

for i in range(100):
    x = random.randrange(0, 300)
    y = random.randrange(0, 300)
    stardustizer(x, y)

root.mainloop()