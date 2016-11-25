import random

class Character:
    def __init__(self, pos_x=0, pos_y=0, max_hp=2, dp=1, sp=1, level=1, status='alive'):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = [self.pos_x, self.pos_y]
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.dp = dp
        self.sp = sp
        self.level = level
        self.status = status

    @property
    def stat_rand(self):
        return random.randint(1,6)

    def strike(self):
        return (2 * self.stat_rand + self.sp)

class Hero(Character):
    def __init__(self, pos_x=0, pos_y=0, max_hp=20, level=1, status='alive'):
        Character.__init__(self, pos_x, pos_y, max_hp, level, status)
        self.max_hp = 20 + 3 * self.stat_rand
        self.dp = 2 * self.stat_rand
        self.sp = 5 + self.stat_rand

    def level_up(self):
        self.level += 1
        self.hp_increase = self.stat_rand
        self.max_hp += self.hp_increase
        self.current_hp += self.hp_increase
        self.dp += self.stat_rand
        self.sp += self.stat_rand

class Skeleton(Character):
    def __init__(self, pos_x=4, pos_y=7, max_hp=2, level=1, status='alive'):
        Character.__init__(self, pos_x, pos_y, max_hp, level, status)
        self.level = level
        self.max_hp = 2 * self.level * self.stat_rand
        self.current_hp = self.max_hp
        self.dp = self.level / 2 * self.stat_rand
        self.sp = self.level * self.stat_rand

class Boss(Character):
    def __init__(self, pos_x=0, pos_y=9, max_hp=2, level=1, status='alive'):
        Character.__init__(self, pos_x, pos_y, max_hp, level, status)
        self.level = level
        self.max_hp = 2 * self.level * self.stat_rand + self.stat_rand
        self.current_hp = self.max_hp
        self.dp = self.level / 2 * self.stat_rand + (self.stat_rand / 2)
        self.sp = self.level * self.stat_rand + self.level

"""
hero = Hero()
print(hero.current_hp)
hero.level_up()
print(hero.current_hp)

print(hero.strike())
print(hero.status)
"""