import PIL.Image
import PIL.ImageTk
from tkinter import *
import rpg_maps

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
        self.map = rpg_maps.FirstMap()
        self.available_tiles = self.map.level_availables
        self.draw_level(self.map.level_map)
        self.draw_logo()
        self.draw_instructions()

    def draw_logo(self):
        self.canvas.create_image(540, 0, anchor=NW, image=self.photos.photo_logo)

    def draw_enemy_stats(self, enemy):
        self.enemy_stat_img = self.canvas.create_image(11.5*self.cell_size, 7.5*self.cell_size, anchor=N, image=self.photos.enemy_photos[enemy.image])
        self.enemy_stat = self.canvas.create_text(13.5*self.cell_size, 8.2*self.cell_size, font=('Tempus Sans ITC', 9, 'bold'), fill="white", text="Level: {0}\nHealth point: {1}/{2}\nStrike point: {3}\nDefend point: {4}\n".format(enemy.level, enemy.current_hp, enemy.max_hp, enemy.sp, enemy.dp))

    def draw_hero_stats(self, hero):
        self.hero_stat_img = self.canvas.create_image(11.5*self.cell_size, 3.5*self.cell_size, anchor=N, image=self.photos.photo_hero_down)
        self.hero_stat = self.canvas.create_text(13.5*self.cell_size, 4.2*self.cell_size, font=('Tempus Sans ITC', 9, 'bold'), fill="white", text="Level: {0}\nHealth point: {1}/{2}\nStrike point: {3}\nDefend point: {4}\n".format(hero.level, hero.current_hp, hero.max_hp, hero.sp, hero.dp))

    def draw_key(self):
        self.key_img = self.canvas.create_image(11.5 * self.cell_size, 5 * self.cell_size, anchor=N, image=self.photos.photo_key)
        self.key = self.canvas.create_text(13.3 * self.cell_size, 5.3 * self.cell_size, font=('Tempus Sans ITC', 9, 'bold'), fill="white", text="You got the key!")

    def draw_instructions(self):
        self.canvas.create_text(13*self.cell_size, 9*self.cell_size, anchor=N, fill="white", font=('Tempus Sans ITC', 22, 'bold'), text="Instructions")
        self.canvas.create_text(13*self.cell_size, 10*self.cell_size, anchor=N, fill="white", font=('Tempus Sans ITC', 9, 'bold'), text="ESC: quit     \u21E7 move up     SPACE: attack")
        self.canvas.create_text(13*self.cell_size, 10.3*self.cell_size, anchor=N, fill="white", font=('Tempus Sans ITC', 9, 'bold'), text="\u21E6 move left  \u21E9 move down  \u21E8 move right")

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

    def draw_enemy(self, enemy):
        self.canvas.create_image(enemy.pos[1] * self.cell_size, enemy.pos[0] * self.cell_size, anchor=NW, image=self.photos.enemy_photos[enemy.image], tag=enemy.id)
        self.canvas.pack()

class Photos:

    def resize(self, image_path, width, height):
        image = PIL.Image.open(image_path).resize((width, height), PIL.Image.ANTIALIAS)
        return PIL.ImageTk.PhotoImage(image)

    def __init__(self):
        self.enemy_photos = {'boss': self.resize("images/boss.png", 50, 50), 'skeleton': self.resize("images/skeleton.png", 50, 50)}
        self.photo_floor = self.resize("images/floor.png", 50, 50)
        self.photo_wall = self.resize("images/wall.png", 50, 50)
        self.photo_hero_up = self.resize("images/hero-up.png", 50, 50)
        self.photo_hero_down = self.resize("images/hero-down.png", 50, 50)
        self.photo_hero_right = self.resize("images/hero-right.png", 50, 50)
        self.photo_hero_left = self.resize("images/hero-left.png", 50, 50)

        self.photo_logo = self.resize("images/logo.png", 232, 105)
        self.photo_key = self.resize("images/key.png", 32, 30)