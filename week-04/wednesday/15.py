# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

root = Tk()

width = 300
height  = 300

canvas = Canvas(root, width=width, height=height, bg='black')
canvas.pack()

def polygonizer(list):
     return canvas.create_polygon(list, fill='black', outline='red')

list = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

polygonizer(list)

root.mainloop()