# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *
import random

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def line_centeralizer(x, y):
    return canvas.create_line(x,y,width/2,height/2, fill='light blue', width='20')



line_centeralizer(0,0)
line_centeralizer(0,height)
line_centeralizer(width,0)
line_centeralizer(width,height)

root.mainloop()