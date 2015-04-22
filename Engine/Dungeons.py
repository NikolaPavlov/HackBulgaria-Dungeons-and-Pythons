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
        self.enemy_position = None
        self.spawning_points = self.find_spawining_points()

    def show_map(self):
        return self.__str__()

    def __str__(self):
        return "\n".join(["".join(line) for line in self.dungeon_map])

    def spawn(self, hero_to_spawn):

        if type(hero_to_spawn) is not Hero:
            raise ThisIsNotAHero

        if len(self.spawning_points) == 0:
            raise NoMoreSpawnPoints

        self.hero = hero_to_spawn
        self.hero_position = self.spawning_points.pop(0)
        self.dungeon_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.HERO

    def find_spawining_points(self):
        spawn_points = []
        for cuurent_row, row in enumerate(self.dungeon_map):
            for current_col, col in enumerate(row):
                if col == Dungeon.SPAWNING_POINT:
                    spawn_points.append((cuurent_row, current_col))
        return spawn_points

    def move_hero(self, direction):

        if not self.hero_position:
            raise NoHeroOnTheMap

        if direction not in Dungeon.POSSIBLE_DIRECTIONS:
            raise WrongDirection

        dy, dx = self.get_direct(direction)
        hero_y, hero_x = self.hero_position
        future_position = (hero_y + dy, hero_x + dx)
        future_row, future_col = future_position
        # print(self.hero_position)  Debugg Prints
        # print(future_position)       Debugg Prints

        if self.path_find(future_position):
            if self.dungeon_map[future_row][future_col] == Dungeon.WALKABLE_PATH:
                self.make_move_and_update_map(future_position)

            elif self.dungeon_map[future_row][future_col] == Dungeon.TREASURE:
                self.make_move_and_update_map(future_position)
                print('Treasure found: ', self.pick_treasure())

            elif self.dungeon_map[future_row][future_col] == Dungeon.ENEMY:
                self.enemy_position = future_position
                self.start_fight('walk')

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

    def make_move_and_update_map(self, position):
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

        if treasure == 'mana':
            self.hero.take_mana(item)
            return ("{} + {} {}".format(self.hero.name, item, treasure))

        elif treasure == 'health':
            self.hero.take_healing(item)
            return ("{} + {} {}".format(self.hero.name, item, treasure))

        elif treasure == 'weapons':
            weapon = eval(item)
            self.hero.equip(weapon)
            return ("{} has equipped {}".format(self.hero.name, weapon.name))

        elif treasure == 'spells':
            spell = eval(item)
            self.hero.learn(spell)
            return ("{} has learned {}".format(self.hero.name, spell.name))

    def start_fight(self, fight_type):
        print("You Started a Fight with an Enemy")
        battle = Fight(self.hero, self.hero_position, self.enemy_position, fight_type)

    def hero_attack(self, by):
        attack_type = {'spell': self.hero.has_spell['cast_range'], 'weapon': 1}
        if (by == 'spell' and self.hero.has_spell and self.hero.can_cast()) or by == 'weapon':
            attack_range = attack_type[by]
            if self.find_enemy_in_range(attack_range):
                self.start_fight(by)
                return True
        return False

    def find_enemy_in_range(self, attack_range):
            for direction in Dungeon.POSSIBLE_DIRECTIONS:
                self.enemy_position = self.hero_position
                for incr_range in range(attack_range):
                    dy, dx = self.get_direct(direction)
                    enemy_y, enemy_x = self.enemy_position
                    self.enemy_position = (enemy_y + dy, enemy_x + dx)
                    if self.path_find(self.enemy_position):
                        if self.dungeon_map[self.enemy_position[0]][self.enemy_position[1]] == Dungeon.ENEMY:
                            return self.enemy_position
                    else:
                        break
            return False


class ThisIsNotAHero(Exception):
    pass


class NoMoreSpawnPoints(Exception):
    pass


class WrongDirection(Exception):
    pass


class NoHeroOnTheMap(Exception):
    pass
