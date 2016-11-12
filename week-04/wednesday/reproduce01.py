from tkinter import *

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height)
canvas.pack()

def squarizer(size, x, y):
    return canvas.create_rectangle(x,y,x+size,y+size, fill='purple')

size = 10

for i in range(1,20):
    x = i * size
    y = i * size
    squarizer(size, x, y)

root.mainloop()
