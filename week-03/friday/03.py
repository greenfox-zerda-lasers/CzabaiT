# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate(object):
    drinked_beer = 0

    def __init__(self):
        pass

    def drink_rum(self):
        self.drinked_beer +=1

    def hows_goin_mate(self):
        if self.drinked_beer >= 5:
            return "Arrrr!"
        else:
            return "Nothin'"

kiskaloz = Pirate()
kiskaloz.drink_rum()
kiskaloz.drink_rum()
print(kiskaloz.hows_goin_mate())
kiskaloz.drink_rum()
kiskaloz.drink_rum()
kiskaloz.drink_rum()
kiskaloz.drink_rum()
print(kiskaloz.hows_goin_mate())