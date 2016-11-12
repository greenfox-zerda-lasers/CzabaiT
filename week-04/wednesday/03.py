# create a 300x300 canvas.
# draw its diagonals in green.
from tkinter import *

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

green1 = canvas.create_line(0,0,300,300, fill='green', width='3')
green2 = canvas.create_line(0,300,300,0, fill='green', width='3')

root.mainloop()