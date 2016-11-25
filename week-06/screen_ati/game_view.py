# this is the view module for RPG game.

from tkinter import *
from PIL import Image, ImageTk
import game_setup



my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=725, height=795)
my_canvas.pack()

image_wall = Image.open("images/wall.png")
photo_wall = ImageTk.PhotoImage(image_wall)
image_hero = Image.open("images/hero-down.png")
photo_hero = ImageTk.PhotoImage(image_hero)
image_enemy = Image.open("images/skeleton.png")
photo_enemy = ImageTk.PhotoImage(image_enemy)
image_boss = Image.open("images/boss.png")
photo_boss = ImageTk.PhotoImage(image_boss)

for j in range(11):
    for i in range(10):
        if game_setup.map_level_1[j][i] == 'W':
            my_canvas.create_image(i*72+2, j*72, anchor=NW, image=photo_wall)
        elif game_setup.map_level_1[j][i] == 'H':
            my_canvas.create_image(i * 72 + 2, j * 72, anchor=NW, image=photo_floor)
            my_canvas.create_image(i * 72 + 2, j * 72, anchor=NW, image=photo_hero)
        elif game_setup.map_level_1[j][i] == 'B':
            my_canvas.create_image(i * 72 + 2, j * 72, anchor=NW, image=photo_floor)
            my_canvas.create_image(i * 72 + 2, j * 72, anchor=NW, image=photo_boss)
        elif game_setup.map_level_1[j][i].isdigit():
            my_canvas.create_image(i * 72 + 2, j * 72, anchor=NW, image=photo_floor)
            my_canvas.create_image(i * 72 + 2, j * 72, anchor=NW, image=photo_enemy)
        else:
            my_canvas.create_image(i*72+2, j*72, anchor=NW, image=photo_floor)


my_canvas.pack()

my_canvas.mainloop()