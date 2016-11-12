# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
from tkinter import *

root = Tk()

width = 300
height  = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def squarizer(size, color):
    return canvas.create_rectangle(width/2-size/2,height/2-size/2,width/2+size/2,height/2+size/2, fill=color, outline=color)

size = 300

for i in range(7):
    size -= 42
    colors = ['#FE080D', '#FE9307', '#FEF506', '#41C903', '#2AC3FC', '#0225F3', '#5630C3']
    squarizer(size,colors[i])

root.mainloop()
