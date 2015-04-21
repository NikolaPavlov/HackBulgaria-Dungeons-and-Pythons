from Enemy import Enemy


class Fight:

    def __init__(self, hero, hero_pos, enemy_pos, fight_type='walk'):
        self.hero = hero
        self.hero_pos = hero_pos
        self.enemy_pos = enemy_pos
        self.fight_type = fight_type
        self.enemy = Enemy(100, 100, 30)
        self.hero_direct = None

    def find_direct_and_dist(self):
        new_pos = tuple([ny - nx for ny, nx in zip(self.hero_pos, self.enemy_pos)])
        if new_pos[0] == 0:
            if new_pos[1] < 0:
                return ['left', abs(new_pos[1])]
            return ['right', abs(new_pos[1])]

        if new_pos[1] == 0:
            if new_pos[0] < 0:
                return ['up', abs(new_pos[0])]
            return ['down', abs(new_pos[0])]

    def fight_scenario(self):
        if self.fight_type == 'spell' or self.fight_type == 'weapon':
            if self.hero.can_cast():
                self.enemy.take_damage(self.hero.attack(by=self.fight_type))

