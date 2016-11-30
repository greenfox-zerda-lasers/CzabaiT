import PIL.Image
import PIL.ImageTk
from tkinter import *
import time

class Intro:

    def __init__(self):
        self.cell_size = 50
        self.width = (10+6)*self.cell_size
        self.height = 11*self.cell_size

        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        self.canvas.focus_set()
        self.draw_logo()
        self.canvas.bind('<Return>', self.press_return)
        self.draw_message()
        self.root.mainloop()

    def draw_logo(self):
        self.photo_logo = self.resize("images/intro.gif", self.width, self.height)
        self.canvas.create_image(0, 0, anchor=NW,
                                 image=self.photo_logo)

    def draw_message(self):
            self.message = self.canvas.create_text(self.width / 2, 0.8 * self.height, anchor=CENTER,
                                                      font=('Tempus Sans ITC', 17, 'bold'), fill="white",
                                                      text="Press enter")

    def resize(self, image_path, width, height):
        image = PIL.Image.open(image_path).resize((width, height), PIL.Image.ANTIALIAS)
        return PIL.ImageTk.PhotoImage(image)

    def press_return(self, event):
        print('Enter pressed')
