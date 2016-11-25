import PIL.Image
import PIL.ImageTk
from tkinter import *
import time

class Intro:

    def __init__(self):
        self.cell_size = 50

        self.root = Tk()
        self.canvas = Canvas(self.root, width=(10+6)*self.cell_size, height=11*self.cell_size, bg="black")
        self.canvas.pack()
        self.canvas.focus_set()
        self.draw_logo()
        self.canvas.bind('<Return>', self.press_return)
        self.draw_message()
        self.root.mainloop()

    def draw_logo(self):
        self.photo_logo = self.resize("images/logo.png", 300, 150)
        self.canvas.create_image(((10 + 6) * self.cell_size) / 2, (11 * self.cell_size) / 2, anchor=CENTER,
                                 image=self.photo_logo)

    def draw_message(self):
            self.message = self.canvas.create_text(((10 + 6) * self.cell_size) / 2, 8 * self.cell_size, anchor=CENTER,
                                                      font=('Tempus Sans ITC', 13, 'bold'), fill="white",
                                                      text="Press enter")

    def resize(self, image_path, width, height):
        image = PIL.Image.open(image_path).resize((width, height), PIL.Image.ANTIALIAS)
        return PIL.ImageTk.PhotoImage(image)

    def press_return(self, event):
        print('Enter pressed')

intro = Intro()