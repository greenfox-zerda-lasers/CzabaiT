# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.
import random
import webcolors
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def rgb():
    return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])

def liner(x1, y1, x2, y2, color):
    return canvas.create_line(x1, y1, x2, y2, fill=rgb())


lines = 30
width = 150
height = 150

for i in range(lines):
    x = i * width / (lines - 1)
    y = i * height / (lines - 1)
    liner(x, 150, 150, 150-y, 'red')  # top-left
    liner(x+150, height, 0+150, y, 'green') #top-right
    liner(x, 0+150, width, y+150, 'blue') #bottom-left
    liner(150, 300-y, x+150, 150, 'orange') #bottom-right


root.mainloop()
