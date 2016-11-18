from tkinter import *
from time import *

class Game:
    size = 30
    x = 20
    y = 20

    move_available = True

    def __init__(self, root):

        self.canvas = Canvas(root, width=300, height=300, bg='red')
        self.canvas.pack()
        self.canvas.focus_set()
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size, fill='blue')
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, width=30, height=5, text="Press arrow button")
        self.label.pack(fill=X)
        self.key_bind()

    def key_bind(self):
        self.canvas.bind('<Left>', self.leftKey)
        self.canvas.bind('<Right>', self.rightKey)
        self.canvas.bind('<Up>', self.upKey)
        self.canvas.bind('<Down>', self.downKey)
        self.canvas.bind('<Return>', self.returnKey)

    def leftKey(self, event):
        if self.move_available:
            self.canvas.move(self.rect, -15, 0)
            self.move_available = False
            self.canvas.update()
            print("Left key pressed")

    def rightKey(self, event):
        if self.move_available:
            self.canvas.move(self.rect, 15, 0)
            self.move_available = False
            self.canvas.update()
            print("Right key pressed")

    def upKey(self, event):
        if self.move_available:
            self.canvas.move(self.rect, 0, -15)
            self.move_available = False
            self.canvas.update()
            print("Up key pressed")

    def downKey(self, event):
        if self.move_available:
            self.canvas.move(self.rect, 0, 15)
            self.move_available = False
            self.canvas.update()
            print("Down key pressed")

    def returnKey(self, event):
        if self.move_available:
            self.move_available = False
            print("Enter key pressed")

    def round(self):
        while True:
            self.move_available = True
            sleep(1)
            self.canvas.update()


root = Tk()
game1 = Game(root)
game1.round()

root.mainloop()