from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300, bg='red')
canvas.pack()

monster = PhotoImage(file="candy.gif")
monster = monster.subsample(10)
label = Label(canvas, image=monster)
label.pack()

root.mainloop()