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
        self.available_tiles = self.first_level.level_availables
        self.draw_level(self.first_level.level_map)
        self.draw_logo()

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
        self.boss_figure = self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_boss)
        self.canvas.pack()

    def draw_skeleton1(self, positions):
        self.skeleton1 = self.canvas.create_image(positions[1] * self.cell_size, positions[0] * self.cell_size, anchor=NW, image=self.photos.photo_skeleton)
        self.canvas.pack()

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