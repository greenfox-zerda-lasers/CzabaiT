# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width=width, height=height)
canvas.pack()

def liner(x1, y1, x2, y2, color):
    return canvas.create_line(x1, y1, x2, y2, fill=color)

size = 3
x = 0
y = 0
lines = 15

for i in range(lines):
    x = i * width / (lines - 1)
    y = i * height / (lines - 1)
    liner(x, height, 0, y, 'green')

for i in range(lines):
    x = i * width / (lines - 1)
    y = i * height / (lines - 1)
    liner(x, 0, width, y, 'blue')


root.mainloop()
