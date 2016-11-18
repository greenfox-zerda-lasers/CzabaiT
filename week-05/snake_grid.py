from random import *
from tkinter import *
from time import *

class Snake:

    def __init__(self, matrix_w, matrix_h):
        self.matrix_w = matrix_w
        self.matrix_h = matrix_h

        self.x = matrix_w // 2
        self.y = matrix_h // 2

class Apple:

    def __init__(self, matrix_w, matrix_h):

        self.x = randrange(0, matrix_w)
        self.y = randrange(0, matrix_h)


class Game:

    matrix_w, matrix_h, cell_size = 10, 10, 20
    move_available = True
    delta_x, delta_y = 0, 0

    def __init__(self):
        self.Matrix = [['blank' for x in range(self.matrix_w)] for y in range(self.matrix_h)]
        self.snake = Snake(self.matrix_w, self.matrix_h)
        self.Matrix[self.snake.x][self.snake.y] = 'snake'
        self.apple = Apple(self.matrix_w, self.matrix_h)
        self.Matrix[self.apple.x][self.apple.y] = 'apple'
        self.root = Tk()

    def print_matrix(self):
        for i in range(10):
            print(self.Matrix[i])

    def display(self):

        self.frame = Frame(self.root)
        self.frame.pack()
        self.label = Label(self.frame, width=30, height=5, bg='yellow', text="Snake")
        self.label.pack(fill=X)

        self.canvas = Canvas(self.root, width=len(self.Matrix[0])*self.cell_size, height=len(self.Matrix)*self.cell_size)
        self.canvas.pack()
        self.canvas.focus_set()
        self.key_bind()



    def key_bind(self):
        self.canvas.bind('<Left>', self.leftKey)
        self.canvas.bind('<Right>', self.rightKey)
        self.canvas.bind('<Up>', self.upKey)
        self.canvas.bind('<Down>', self.downKey)
        self.canvas.bind('<Return>', self.returnKey)

    def leftKey(self, event):
        if self.move_available:
            self.delta_x -= 1
            self.delta_y = 0
            self.move_available = False
            self.canvas.update()

            print("Left key pressed")

    def rightKey(self, event):
        if self.move_available:
            self.delta_x += 1
            self.delta_y = 0
            self.move_available = False
            self.canvas.update()

            print("Right key pressed")

    def upKey(self, event):
        if self.move_available:
            self.delta_x = 0
            self.delta_y -= 1
            self.move_available = False
            self.canvas.update()

            print("Up key pressed")

    def downKey(self, event):
        if self.move_available:
            self.delta_x = 0
            self.delta_y += 1
            self.move_available = False
            self.canvas.update()

            print("Down key pressed")

    def returnKey(self, event):
            print("Enter key pressed")

    def round(self):
        self.display()

        while True:
            self.canvas.update()
            sleep(1)
            self.move_available = True

            self.player = self.canvas.create_rectangle((self.snake.x+self.delta_x) * self.cell_size, (self.snake.y+self.delta_y) * self.cell_size,
                                                       (self.snake.x+self.delta_x) * self.cell_size + self.cell_size,
                                                       (self.snake.y+self.delta_y) * self.cell_size + self.cell_size, fill='green')
            self.target = self.canvas.create_rectangle(self.apple.x * self.cell_size, self.apple.y * self.cell_size,
                                                       (self.apple.x * self.cell_size) + self.cell_size,
                                                       (self.apple.y * self.cell_size) + self.cell_size, fill='pink')



game1 = Game()
game1.print_matrix()
game1.round()


root.mainloop()
