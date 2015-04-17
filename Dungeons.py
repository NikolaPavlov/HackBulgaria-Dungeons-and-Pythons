from Hero import Hero


class Dungeon:

    def __init__(self, level="level1.txt"):
        self.level = level
        self.dungeon_map = []
        self.load_level()
        self.hero_yx = None

    def load_level(self):
        with open(self.level) as f:
            for line in f:
                self.dungeon_map.append(line.strip().split(','))

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
                    return True
        return False

    def move_hero(self, direction):
        possible_directions = set(["up", "down", "left", "right"])

        if direction not in possible_directions:
            raise WrongDirection

        new_pos = tuple([ny + nx for ny, nx in zip(self.get_direct(direction), self.hero_yx)])
        print(self.hero_yx)
        print (new_pos)
        if self.path_find(new_pos):
            self.dungeon_map[self.hero_yx[0]][self.hero_yx[1]] = '.'
            self.hero_yx = new_pos
            self.dungeon_map[self.hero_yx[0]][self.hero_yx[1]] = 'H'
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
        if position[0] > len(self.dungeon_map) or position[0] < 0:
            return False
        if position[1] > len(self.dungeon_map[position[0]]) or position[1] < 0:
            return False
        return True


class ThisIsNotAHero(Exception):
    pass


class WrongDirection(Exception):
    pass
