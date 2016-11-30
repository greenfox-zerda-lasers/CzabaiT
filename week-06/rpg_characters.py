import random
import math

class Character:

    def __init__(self, pos=[0, 0], max_hp=2, dp=1, sp=1, level=1, status='alive', has_key=False, is_boss=False):
        self.pos = pos
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.dp = dp
        self.sp = sp
        self.level = level
        self.status = status
        self.has_key = has_key
        self.is_boss = is_boss

    @property
    def stat_rand(self):
        return random.randint(1,6)

    def strike(self):
        return (2 * self.stat_rand + self.sp)

class Hero(Character):
    count = 1

    def __init__(self, pos=[0, 0], max_hp=20, level=1, status='alive', has_key=False, is_boss=False):
        Character.__init__(self, pos, max_hp, level, status, has_key, is_boss)
        self.level = level
        self.max_hp = 20 + 3 * self.stat_rand
        self.current_hp = self.max_hp
        self.dp = 2 * self.stat_rand
        self.sp = 5 + self.stat_rand
        self.id = "hero{0}".format(Hero.count)
        Hero.count += 1

    def level_up(self):
        self.level += 1
        self.hp_increase = self.stat_rand
        self.max_hp += self.hp_increase
        self.current_hp += self.hp_increase
        self.dp += self.stat_rand
        self.sp += self.stat_rand

class Skeleton(Character):
    count = 1

    def __init__(self, pos=[0, 0], max_hp=2, level=1, status='alive', has_key=False, is_boss=False):
        Character.__init__(self, pos, max_hp, level, status, has_key, is_boss)
        self.level = level
        self.max_hp = 3 * self.level * self.stat_rand
        self.current_hp = self.max_hp
        self.dp = math.ceil(self.level / 2 * self.stat_rand)
        self.sp = self.level * self.stat_rand
        self.image = 'skeleton'
        self.id = "skeleton{0}".format(Skeleton.count)
        Skeleton.count += 1


class Boss(Character):
    count = 1

    def __init__(self, pos=[0, 0], max_hp=2, level=1, status='alive', has_key=False, is_boss=True):
        Character.__init__(self, pos, max_hp, level, status, has_key, is_boss)
        self.level = level
        self.max_hp = 3 * self.level * self.stat_rand +  2* self.stat_rand
        self.current_hp = self.max_hp
        self.dp = math.ceil(self.level / 2 * self.stat_rand + (self.stat_rand / 2))
        self.sp = self.level * self.stat_rand + self.level
        self.image = 'boss'
        self.id = "boss{0}".format(Boss.count)
        Boss.count += 1
        self.is_boss = is_boss

if __name__ == "__main__":
    skeleton = Skeleton()
    print(skeleton.level)