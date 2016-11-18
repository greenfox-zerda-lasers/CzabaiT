# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class ElevatorModel:

    persons = ["___", "_x_", "xx_", "xxx","xxX","xXX","XXX"]

    def __init__(self, elev_level=0, elev_fill=0):
        self.floors = 30
        self.elev_level = elev_level
        self.elev_fill = elev_fill

    def draw_elev(self):
        if self.elev_level == 0:
            elev = "  _||_||_[{0}]_||_||_______||_||_".format(self.persons[self.elev_fill])
        else:
            elev = "   || || [{0}] || ||       || || ".format(self.persons[self.elev_fill])
        return elev

    def draw_top(self):
        return "___________________________________\n" + "`._______________________________.'"

    def draw_floor(self, floor):
        if floor == self.floors-1:
            return "  _||_||_______||_||_______||_||_"
        else:
            return "   || ||       || ||       || || "

    def draw_bot(self):
        return ".'_______________________________`."

    def draw_build(self):
        print(self.draw_top())
        for floor in range(self.floors):
            if floor == (self.floors-1)-self.elev_level:  #program draws from up to down -> lift position must be substracted from floors
                print(self.draw_elev())
            else:
                print(self.draw_floor(floor))
        print(self.draw_bot())

    def up_elev(self):
        if self.elev_level < self.floors-1:
            self.elev_level += 1

    def down_elev(self):
        if self.elev_level > 0:
            self.elev_level -= 1

    def get_in(self):
        if self.elev_fill < len(self.persons)-1:
            self.elev_fill += 1

    def get_out(self):
        if self.elev_fill > 0:
            self.elev_fill -= 1

elevator = ElevatorModel(0, 0)

import os
import sys

while True:
    action = input('Press key!\n')
    os.system('clear')
    if action == "8":
        elevator.up_elev()
    elif action == "2":
        elevator.down_elev()
    elif action == "+":
        elevator.get_in()
    elif action == "-":
        elevator.get_out()
    elif action == "q":
        sys.exit()
    elevator.draw_build()
