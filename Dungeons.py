class Dungeon:
    def __init__(self, level="level1.txt"):
        self.level = level
        self.dungeon_map = []
        self.load_level()

    def load_level(self):
        with open(self.level) as f:
            for line in f:
                self.dungeon_map.append(line.strip().split(','))

    def show_map(self):
        for map_proc in self.dungeon_map:
            print(''.join(map_proc))
