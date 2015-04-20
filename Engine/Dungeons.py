from Hero import Hero
from Spell import Spell
from Weapon import Weapon
import json
import random


class Dungeon:

    def __init__(self, level="../resources/level1.txt"):
        self.level = level
        self.dungeon_map = []
        self.load_level()
        self.hero_yx = None

    def load_level(self):
        with open(self.level) as f:
            for line in f:
                self.dungeon_map.append(list(line.strip()))

    def show_map(self):
        for map_path in self.dungeon_map:
            print(''.join(map_path))

    def spawn(self, hero_to_spawn):

        if type(hero_to_spawn) is not Hero:
            raise ThisIsNotAHero

        for path_y, path in enumerate(self.dungeon_map):
            for step_x, step in enumerate(path):
                if step == 'S':
                    self.dungeon_map[path_y][step_x] = 'H'
                    self.hero_yx = (path_y, step_x)
                    self.hero = hero_to_spawn
                    return True
        return False

    def move_hero(self, direction):
        possible_directions = set(["up", "down", "left", "right"])

        if not self.hero_yx:
            raise NoHeroOnTheMap

        if direction not in possible_directions:
            raise WrongDirection

        new_pos = tuple([ny + nx for ny, nx in zip(self.get_direct(direction), self.hero_yx)])
        new_y = new_pos[0]
        new_x = new_pos[1]
        # print(self.hero_yx)  Debugg Prints
        # print(new_pos)       Debugg Prints

        if self.path_find(new_pos):
            if self.dungeon_map[new_y][new_x] == '.':
                self.update_map(new_pos)

            elif self.dungeon_map[new_y][new_x] == 'T':
                self.pick_treasure()
                self.update_map(new_pos)

            elif self.dungeon_map[new_y][new_x] == 'E':
                self.start_fight()
                print("You Started a Fight with an Enemy")

            elif self.dungeon_map[new_y][new_x] == 'G':
                print("You reached the Gate to the next Dungeon")

            return True

    def get_direct(self, direction):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'right': (0, 1),
            'left': (0, -1)
        }
        return directions[direction]

    def path_find(self, position):
        xh = position[1]
        yh = position[0]
        Y = len(self.dungeon_map)
        X = len(self.dungeon_map[yh])

        if not (-1 < xh <= X and -1 < yh <= Y):
            return False

        elif self.dungeon_map[yh][xh] == '#':
            return False

        return True

    def update_map(self, position):
        self.dungeon_map[self.hero_yx[0]][self.hero_yx[1]] = '.'
        self.hero_yx = position
        self.dungeon_map[self.hero_yx[0]][self.hero_yx[1]] = 'H'
        self.hero.regen_mana()
        return True

    def pick_treasure(self):
        self.treasure_chest = {}

        with open('../resources/treasures.json', 'r') as fp:
            self.treasure_chest = json.load(fp)

        treasure = random.choice(list(self.treasure_chest.keys()))
        item = random.choice(self.treasure_chest[treasure])
        print("{} Found a {} chest!!!".format(self.hero.name, treasure))

        if treasure == 'mana':
            self.hero.take_mana(item)
            print("{} + {} {}".format(self.hero.name, item, treasure))

        elif treasure == 'health':
            self.hero.take_healing(item)
            print("{} + {} {}".format(self.hero.name, item, treasure))

        elif treasure == 'weapons':
            weapon = eval(item)
            self.hero.equip(weapon)
            print("{} has equipped {}".format(self.hero.name, weapon.name))

        elif treasure == 'spells':
            spell = eval(item)
            self.hero.learn(spell)
            print("{} has learned {}".format(self.hero.name, spell.name))

    def start_fight(self):
        pass

    def hero_attack(self, by):
        if by == 'spell' and self.hero.has_spell:
            for enemy_dist in range(1, self.hero.has_spell['cast_range']+1):
                print(enemy_dist)


class ThisIsNotAHero(Exception):
    pass


class WrongDirection(Exception):
    pass


class NoHeroOnTheMap(Exception):
    pass
