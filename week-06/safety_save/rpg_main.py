import rpg_model
import rpg_view
import rpg_characters
import random

class Main:

    def __init__(self):
        self.round = 0
        self.char_coords = {}
        self.hero_direction = 'down'

        self.model = rpg_model.Model()
        self.view = rpg_view.View()
        self.hero = rpg_characters.Hero()
        self.skeleton1 = rpg_characters.Skeleton(10, 9)
#        self.skeleton2 = rpg_characters.Skeleton(5, 0)
#        self.skeleton3 = rpg_characters.Skeleton(0, 4)
#        self.skeleton4 = rpg_characters.Skeleton(5, 7)
#        self.skeletons = [self.skeleton1, self.skeleton2, self.skeleton3, self.skeleton4]

        self.boss = rpg_characters.Boss(0, 9)

        self.available_tiles = self.view.available_tiles
        self.draw_init_characters() #init pos
        self.keyboard_bind()

        self.view.root.mainloop()

    def move_direction_generator(self, character_pos):
        char_move_test = character_pos[:]
        move = random.choice(['left', 'right', 'up', 'down'])
        if move == 'up' and char_move_test[0] > 0:
            char_move_test[0] -= 1
        elif move == 'down' and char_move_test[0] < self.view.num_of_rows-1:
            char_move_test[0] += 1
        elif move == 'left' and char_move_test[1] > 0:
            char_move_test[1] -= 1
        elif move == 'right' and char_move_test[1] < self.view.num_of_columns-1:
            char_move_test[1] += 1
        if char_move_test in self.char_coords.values():
            return character_pos
        else:
            return char_move_test

    def enemy_move(self, enemy):
        for _ in range(4):
            pos_change = self.move_direction_generator(enemy.pos[:])
            if pos_change in self.available_tiles:
                return pos_change
        return enemy.pos

    def draw_init_characters(self):
        self.view.draw_hero(self.hero_direction, self.hero.pos)
        self.char_coords['hero'] = self.hero.pos
        self.view.draw_boss(self.boss.pos)
        self.char_coords['boss'] = self.boss.pos
        self.view.draw_skeleton1(self.skeleton1.pos)
        self.char_coords['skeleton1'] = self.skeleton1.pos

    def keyboard_bind(self):
        self.view.canvas.bind('<Left>', self.left_key)
        self.view.canvas.bind('<Right>', self.right_key)
        self.view.canvas.bind('<Up>', self.up_key)
        self.view.canvas.bind('<Down>', self.down_key)
        self.view.canvas.bind('<space>', self.space_key)

    def move_events(self, coord, pos_step):
        self.view.canvas.delete(self, self.view.hero_figure)
        hero_move_test = self.hero.pos[:]
        hero_move_test[coord] += pos_step
        if hero_move_test in self.available_tiles:
            if hero_move_test in self.char_coords.values():
                print("Itt állnak")
            else:
                self.hero.pos[coord] += pos_step
        self.view.draw_hero(self.hero_direction, self.hero.pos)
        self.char_coords['hero'] = self.hero.pos
        self.enemy_move_events()

    def enemy_move_events(self):
        if self.round % 2 == 0:
            self.view.canvas.delete(self, self.view.boss_figure, self.view.skeleton1)
#del            if self.boss.status == 'alive':
            self.boss.pos = self.enemy_move(self.boss)
            self.view.draw_boss(self.boss.pos)
            self.char_coords['boss'] = self.boss.pos
#del            else:
#del                del self.char_coords['boss']

#del            if self.skeleton1.status == 'alive':
            self.skeleton1.pos = self.enemy_move(self.skeleton1)
            self.view.draw_skeleton1(self.skeleton1.pos)
            self.char_coords['skeleton1'] = self.skeleton1.pos
#del            else:
#del                del self.char_coords['boss']
        self.round += 1

    def left_key(self, event):
        self.hero_direction = 'left'
        self.move_events(1, -1)

    def right_key(self, event):
        self.hero_direction = 'right'
        self.move_events(1, 1)

    def up_key(self, event):
        self.hero_direction = 'up'
        self.move_events(0, -1)

    def down_key(self, event):
        self.hero_direction = 'down'
        self.move_events(0, 1)

    def space_key(self, event):
        if self.hero_direction == 'right':
            self.target_event(1, 1)
        if self.hero_direction == 'left':
            self.target_event(1, -1)
        if self.hero_direction == 'up':
            self.target_event(0, -1)
        if self.hero_direction == 'down':
            self.target_event(0, 1)

    def target_event(self, coord, direct):
            target_pos = self.hero.pos[:]
            target_pos[coord] += direct
            if target_pos in self.char_coords.values():
                for name, pos in self.char_coords.items():
                    if pos == target_pos:
                        print(name)
                        if name == 'hero':
                            self.battle(self.hero, name)
                        elif name == 'boss':
                            self.battle(self.boss, name)
                        elif name == 'skeleton1':
                            self.battle(self.skeleton1, name)

    def battle(self, character, name):
        hero_strike = self.hero.strike()
        enemy_strike = character.strike() #because of random
        if hero_strike > character.dp:
            character.current_hp -= hero_strike
            print(character.current_hp)
            if character.current_hp <= 0:
                character.status = "dead"
#del                self.view.canvas.delete(self, !!!!!!4IDEMEGMIT!!!!!!!!!)
                print(name, 'status:', character.status)
                self.hero.level_up()
                print("hero.level:", self.hero.level)
            else:
                self.hero.current_hp -= enemy_strike
                if self.hero.current_hp <= 0:
                    self.hero.status = "dead"
#del                    self.view.canvas.delete(self, self.view.hero_figure)
                    print("Game over")

game = Main()
