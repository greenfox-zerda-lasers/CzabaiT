"""
for x in range(0, 9):
    globals()['string%s' % x] = 'Hello'

#print(string3)

proba = {'hero' : [0,0], 'boss': [0,8], 'skeleton': [5,5], 'skeleton2' : [6,7]}


for name, age in proba.items():
    if age == [0,0]:
        print(name)
"""

from tkinter import *


class First:
    def __init__(self, ready_function):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=10, height=10)
        self.canvas.pack()
        self.canvas.focus_set()
        self.canvas.bind('<Return>', self.press_return)
        self.on_complete = ready_function
        self.canvas.mainloop()

    def press_return(self, event):
        print('Enter')
        self.on_complete()

class Second:
    def __init__(self):
        print('jo oreg vmi')

class Main:
    def __init__(self):
        first = First(self.hammerTime)


    def hammerTime(self):
        first1 = First(None)

main = Main()