import random

class Game(object):

    state = "playing"

    def __init__(self):
        self.random()

    def guess(self,guess):
        self.random_number



        result = "Fasza vagy Jani!"
        self.state = "finished"
        return result

    def random(self):
        self.random_number = [random.randrange(0,10) for _ in range(4)]



    guess_input()

game = Game()
while game.state != "finished"
    print(game.guess(input("Guess with a 4 digit number:")))