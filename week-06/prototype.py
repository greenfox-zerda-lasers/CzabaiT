import PIL.Image
import PIL.ImageTk
from tkinter import *
import rpg_levels

class View:

    def __init__(self):
        self.num_of_rows = 11
        self.num_of_columns = 10
        self.cell_size = 50

        self.root = Tk()
        self.canvas = Canvas(self.root, width=(10+6)*self.cell_size, height=11*self.cell_size, bg="black")
        self.canvas.pack()
        self.canvas.focus_set()
        self.photos = Photos()
        self.first_level = rpg_levels.FirstLevel()
        self.draw_level(self.first_level.level_map)

### KÍSÉRLET ############
        self.draw_logo()

        self.availables = self.first_level.level_availables
        print(self.availables)
        self.hero_pos = [0, 0]
        self.hero_check = 0
        self.boss_pos = [1, 1]
        self.draw_hero('down', self.hero_pos)
        self.draw_boss(self.boss_pos)
        self.keyboard_bind()
#########################
        self.root.mainloop()

    def draw_logo(self):
        self.canvas.create_image(540, 0, anchor=NW, image=self.photos.photo_logo)

    def draw_level(self, actual_level):
        for i in range(self.num_of_rows):
            for j in range(self.num_of_columns):
                if actual_level[i][j] == 'W':
                    self.canvas.create_image(j * self.cell_size, i * self.cell_size, anchor=NW, image=self.photos.photo_wall)
                elif actual_level[i][j] == '_':
                    self.canvas.create_image(j * self.cell_size, i * self.cell_size, anchor=NW, image=self.photos.photo_floor)
        self.canvas.pack()

    def draw_hero(self, direction, positions):
        if direction == 'down':
            self.hero_figure = self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_hero_down)
        elif direction == 'left':
            self.hero_figure = self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_hero_left)
        elif direction == 'right':
            self.hero_figure = self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_hero_right)
        elif direction == 'up':
            self.hero_figure = self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_hero_up)
        self.canvas.pack()

    def draw_boss(self, positions):
        self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_boss)
        self.canvas.pack()

    def draw_skeleton(self, positions):
        self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_skeleton)
        self.canvas.pack()

    def keyboard_bind(self):
        self.canvas.bind('<Left>', self.left_key)
        self.canvas.bind('<Right>', self.right_key)
        self.canvas.bind('<Up>', self.up_key)
        self.canvas.bind('<Down>', self.down_key)
#       self.view.canvas.bind('<Return>', self.model.return_key)

    def left_key(self, event):
            self.canvas.delete(self, self.hero_figure)
            if self.hero_check - 1 in self.availables:
                self.hero_pos[1] -= 1
                self.hero_check -= 1
            self.draw_hero('left', self.hero_pos)
            print("hero_pos:", self.hero_pos)
            print("hero_check:", self.hero_check)
#            print("Left key pressed")

    def right_key(self, event):
            self.canvas.delete(self, self.hero_figure)
            if self.hero_check + 1 in self.availables:
                self.hero_pos[1] += 1
                self.hero_check += 1
            self.draw_hero('right', self.hero_pos)
            print("hero_pos:", self.hero_pos)
            print("hero_check:", self.hero_check)
#            print("Right key pressed")

    def up_key(self, event):
            self.canvas.delete(self, self.hero_figure)
            if self.hero_check - 100 in self.availables:
                self.hero_pos[0] -= 1
                self.hero_check -= 100
            self.draw_hero('up', self.hero_pos)
            print("hero_pos:", self.hero_pos)
            print("hero_check:", self.hero_check)
#            print("Up key pressed")

    def down_key(self, event):
            self.canvas.delete(self, self.hero_figure)
            if self.hero_check + 100 in self.availables:
                self.hero_pos[0] += 1
                self.hero_check += 100
            self.draw_hero('down', self.hero_pos)
            print("hero_pos:", self.hero_pos)
            print("hero_check:", self.hero_check)
#           print("Down key pressed")


class Photos:

    def resize(self, image_path, width, height):
        image = PIL.Image.open(image_path).resize((width, height), PIL.Image.ANTIALIAS)
        return PIL.ImageTk.PhotoImage(image)

    def __init__(self):
        self.photo_floor = self.resize("images/floor.png", 50, 50)
        self.photo_candy = self.resize("images/candy.gif", 50, 50)
        self.photo_wall = self.resize("images/wall.png", 50, 50)
        self.photo_hero_up = self.resize("images/hero-up.png", 50, 50)
        self.photo_hero_down = self.resize("images/hero-down.png", 50, 50)
        self.photo_hero_right = self.resize("images/hero-right.png", 50, 50)
        self.photo_hero_left = self.resize("images/hero-left.png", 50, 50)
        self.photo_skeleton = self.resize("images/skeleton.png", 50, 50)
        self.photo_boss = self.resize("images/boss.png", 50, 50)

        self.photo_logo = self.resize("images/logo.png", 232, 105)

view = View()
print(view.availables)