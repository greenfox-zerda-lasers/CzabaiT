from tkinter import *

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height)
canvas.pack()

def squarizer(size, x, y):
    return canvas.create_rectangle(x,y,x+size,y+size, fill='#B147F1')

position = 10
size = 0
x = 10
y = 10

for i in range(1,6):
    x += size
    y += size
    size += 10
    squarizer(size, x, y)

root.mainloop()