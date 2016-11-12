# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
from tkinter import *

root = Tk()

width = 300
height = 300
canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

x = 30

red_line = canvas.create_line(width/2-x,height/2-x,width/2+x,height/2-x, fill='red', width='3')
green_line = canvas.create_line(width/2+x,height/2-x,width/2+x,height/2+x, fill='green', width='3')
blue_line = canvas.create_line(width/2-x,height/2+x,width/2+x,height/2+x, fill='blue', width='3')
yellow_line = canvas.create_line(width/2-x,height/2-x,width/2-x,height/2+x, fill='yellow', width='3')

root.mainloop()

