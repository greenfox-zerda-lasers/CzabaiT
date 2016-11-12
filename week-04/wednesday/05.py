# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.
from tkinter import *
import random

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def line_centeralizer(x, y):
    return canvas.create_line(x,y,x,y+50, fill='gold', width='2')

for i in range(3):
    x = random.randrange(0,300)
    y = random.randrange(0,300)
    line_centeralizer(x,y)

root.mainloop()