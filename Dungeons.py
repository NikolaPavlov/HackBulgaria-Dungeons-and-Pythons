from Hero import Hero


class Dungeon:
    def __init__(self, level="level1.txt"):
        self.level = level
        self.dungeon_map = []
        self.load_level()
        self.hero_current_position = None

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

        for path_num, path in enumerate(self.dungeon_map):
            for step_num, step in enumerate(path):
                if step == 'S':
                    self.dungeon_map[path_num][step_num] = 'H'
                    self.hero_current_position = (path_num, step_num)
                    return True
        return False

    def move_hero(self, direction):
        possible_directions = set(["up", "down", "left", "right"])

        if direction not in possible_directions:
            raise WrongDirection

        if direction == "up":
            return self.move_up()

        elif direction == "left":
            return self.move_left()

        elif direction == "right":
            return self.move_right()

        elif direction == "down":
            return self.move_down()

    def move_up(self):
        if self.hero_current_position[0] - 1 < 0:
            return False
        return True

    def move_down(self):
        if self.hero_current_position[0] + 1 > len(self.dungeon_map):
            return False
        return True

    def move_right(self):
        num_path = self.hero_current_position[0]
        if self.hero_current_position[1] + 1 > len(self.dungeon_map[num_path]):
            return False
        return True

    def move_left(self):
        if self.hero_current_position[1] - 1 < 0:
            return False
        return True



class ThisIsNotAHero(Exception):
    pass

class WrongDirection(Exception):
    pass
