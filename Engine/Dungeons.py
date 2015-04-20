from Hero import Hero
from Spell import Spell
from Weapon import Weapon
from Fight import Fight
import json
import random


class Dungeon:
    WALL = "#"
    SPAWNING_POINT = "S"
    ENEMY = "E"
    EXIT = "G"
    TREASURE = "T"
    WALKABLE_PATH = "."
    HERO = "H"
    POSSIBLE_DIRECTIONS = set(["up", "down", "left", "right"])

    @staticmethod
    def load_level(level_path="../resources/level1.txt"):
        with open(level_path) as f:
            contents = f.read().split("\n")
            dungeon_lvl = [list(line) for line in contents if line.strip() != ""]

        return Dungeon(dungeon_lvl)

    def __init__(self, dung_map):
        self.dungeon_map = dung_map
        self.hero_position = None

    def show_map(self):
        for map_path in self.dungeon_map:
            print(''.join(map_path))

    def spawn(self, hero_to_spawn):

        if type(hero_to_spawn) is not Hero:
            raise ThisIsNotAHero

        for cuurent_row, row in enumerate(self.dungeon_map):
            for current_col, col in enumerate(row):
                if col == Dungeon.SPAWNING_POINT:
                    self.dungeon_map[cuurent_row][current_col] = Dungeon.HERO
                    self.hero_position = (cuurent_row, current_col)
                    self.hero = hero_to_spawn
                    return True
        return False

    def move_hero(self, direction):

        if not self.hero_position:
            raise NoHeroOnTheMap

        if direction not in Dungeon.POSSIBLE_DIRECTIONS:
            raise WrongDirection

        future_position = tuple([ny + nx for ny, nx in zip(self.get_direct(direction), self.hero_position)])
        future_row = future_position[0]
        future_col = future_position[1]
        # print(self.hero_position)  Debugg Prints
        # print(future_position)       Debugg Prints

        if self.path_find(future_position):
            if self.dungeon_map[future_row][future_col] == Dungeon.WALKABLE_PATH:
                self.update_map(future_position)

            elif self.dungeon_map[future_row][future_col] == Dungeon.TREASURE:
                self.pick_treasure()
                self.update_map(future_position)

            elif self.dungeon_map[future_row][future_col] == Dungeon.ENEMY:
                self.start_fight()
                print("You Started a Fight with an Enemy")

            elif self.dungeon_map[future_row][future_col] == Dungeon.EXIT:
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

        elif self.dungeon_map[yh][xh] == Dungeon.WALL:
            return False

        return True

    def update_map(self, position):
        self.dungeon_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.WALKABLE_PATH
        self.hero_position = position
        self.dungeon_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.HERO
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
        attack_type = {'spell': self.hero.has_spell['cast_range'], 'weapon': 1}
        if (by == 'spell' and self.hero.has_spell) or by == 'weapon':
            attack_range = attack_type[by]
            if self.find_enemy_in_range(attack_range):
                return True
        return False

    def find_enemy_in_range(self, attack_range):
            for direction in Dungeon.POSSIBLE_DIRECTIONS:
                enemy_possition = self.hero_position
                for incr_range in range(attack_range):
                    enemy_possition = tuple([ny + nx for ny, nx in zip(self.get_direct(direction), enemy_possition)])
                    if self.path_find(enemy_possition):
                        if self.dungeon_map[enemy_possition[0]][enemy_possition[1]] == Dungeon.ENEMY:
                            return enemy_possition
                    else:
                        break
            return False


class ThisIsNotAHero(Exception):
    pass


class WrongDirection(Exception):
    pass


class NoHeroOnTheMap(Exception):
    pass
