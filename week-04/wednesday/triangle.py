from tkinter import *
import random
import math
import webcolors
import time

root = Tk()

width = 400
height = 400

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def rgb():
    return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])

def triangulizer(x, y):
    return canvas.create_polygon(x, y, x+length, y, x+length/2, y-(length/2*math.sqrt(3)), fill=rgb(), outline='black')

lines = 15
length = 10

for i in range(1,lines+1):
    time.sleep(0.3)
    canvas .update()
    if i % 2 == 0:
        print(triangulizer(200, 10 + i *length/2*math.sqrt(3)))
        for j in range(-i//2,i//2):
            print(triangulizer(200 + j * length, 10 + i *length/2*math.sqrt(3)))
    else:
        for j in range(-i//2,i//2):
            print(triangulizer(200 + length/2 + j * length, 10 + i *length/2*math.sqrt(3)))

root.mainloop()