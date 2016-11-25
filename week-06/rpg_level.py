import rpg_model
import rpg_view
import rpg_characters
import random
import sys

class Level:

    def __init__(self):
        self.round = 0
        self.char_coords = {}

        self.model = rpg_model.Model()
        self.view = rpg_view.View()
        self.available_tiles = self.view.available_tiles
        self.hero = rpg_characters.Hero()
        self.hero_generator()
        self.view.draw_hero_stats(self.hero)
        self.enemies = []
        self.enemy_generator()

        self.keyboard_bind()
        self.view.root.mainloop()

    def hero_generator(self):
        self.hero_direction = 'down'
        self.view.draw_hero(self.hero_direction, [0, 0])
        self.char_coords[self.hero.id] = self.hero.pos

    def coord_generator(self):
        result = False
        while result == False:
            coords = [random.randint(0, 10), random.randint(0, 9)]
            if coords in self.available_tiles and coords not in self.char_coords.values():
                result = coords
            else:
                result = False
        return result

    def enemy_generator(self):
        self.enemies.append(rpg_characters.Boss(self.coord_generator()))
        self.view.draw_enemy(self.enemies[0])
        self.char_coords[self.enemies[0].id] = self.enemies[0].pos
        skeleton_num = random.randint(3, 5)
        skeleton_key_random = random.randint(1, skeleton_num)
        for i in range(1, skeleton_num+1):  #boss has list[0]
            self.enemies.append(rpg_characters.Skeleton(self.coord_generator()))
            self.view.draw_enemy(self.enemies[i])
            self.char_coords[self.enemies[i].id] = self.enemies[i].pos
            if i == skeleton_key_random:
                self.enemies[i].has_key = True

        print('char_coords:', self.char_coords)
        print('enemies_list:', self.enemies)

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

    def keyboard_bind(self):
        self.view.canvas.bind('<Left>', self.left_key)
        self.view.canvas.bind('<Right>', self.right_key)
        self.view.canvas.bind('<Up>', self.up_key)
        self.view.canvas.bind('<Down>', self.down_key)
        self.view.canvas.bind('<space>', self.space_key)
        self.view.canvas.bind('<Escape>', self.escape_key)

    def move_events(self, coord, pos_step):
        self.view.canvas.delete(self, self.view.hero_figure)
        hero_move_test = self.hero.pos[:]
        hero_move_test[coord] += pos_step
        if hero_move_test in self.available_tiles:
            if hero_move_test not in self.char_coords.values():
                self.hero.pos[coord] += pos_step
        self.view.draw_hero(self.hero_direction, self.hero.pos)
        self.char_coords[self.hero.id] = self.hero.pos
        self.enemy_move_events()

    def enemy_move_events(self):
        if self.round % 2 == 0:
            for enemy in self.enemies:
                self.view.canvas.delete(self, enemy.id)
                enemy.pos = self.enemy_move(enemy)
                self.view.draw_enemy(enemy)
                self.char_coords[enemy.id] = enemy.pos
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

    def escape_key(self, event):
        sys.exit()

    def target_event(self, coord, direct):
            try:
                self.view.canvas.delete(self.view.enemy_stat, self.view.enemy_stat_img)
            except AttributeError:
                pass
            target_pos = self.hero.pos[:]
            target_pos[coord] += direct
            if target_pos in self.char_coords.values():
                for name, pos in self.char_coords.items():
                    if pos == target_pos:
                        for enemy in self.enemies:
                            if enemy.id == name:
                                self.param_enemy = enemy
                                self.param_name = name
                self.battle(self.param_enemy, self.param_name)

    def battle(self, character, name):
        hero_strike = self.hero.strike()
        enemy_strike = character.strike() #because of random
        if hero_strike > character.dp:
            character.current_hp -= hero_strike
            if character.current_hp <= 0:
                character.status = "dead"
                if character.has_key == True:
                    self.view.draw_key()
                    self.level_condition_key = True
                if character.is_boss == True:
                    self.level_condition_boss = True
                self.hero.level_up()
                self.view.canvas.delete(self, character.id)
                del self.char_coords[name]
                self.enemies.remove(character)
            else:
                self.hero.current_hp -= enemy_strike
                if self.hero.current_hp <= 0:
                    self.hero.status = "dead"
                    print("Game over")
        self.view.canvas.delete(self.view.hero_stat, self.view.hero_stat_img)
        self.view.draw_hero_stats(self.hero)
        self.view.draw_enemy_stats(character)
