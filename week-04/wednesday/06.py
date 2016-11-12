# create a 300x300 canvas.
# draw a green 10x10 square to its center.
from tkinter import *

root = Tk()

width = 300
height  = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

x = 10

green_square = canvas.create_rectangle(width/2-x/2,height/2-x/2,width/2+x/2,height/2+x/2, fill='green')

root.mainloop()
