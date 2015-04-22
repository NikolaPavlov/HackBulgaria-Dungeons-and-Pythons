from Enemy import Enemy


class Fight:

    def __init__(self, hero, hero_pos, enemy_pos, fight_type='walk'):
        self.hero = hero
        self.hero_pos = hero_pos
        self.enemy_pos = enemy_pos
        self.fight_type = fight_type
        self.enemy = Enemy(100, 100, 30)
        self.distfight = True
        self.hero_drect_dist = self.find_direct_and_dist()

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

    def hero_fight_from_distance(self):
        if (self.fight_type == 'spell' and self.hero.can_cast()) or self.fight_type == 'weapon':
            dmg_done = self.hero.attack(by=self.fight_type)
            self.enemy.take_damage(dmg_done)
            msg = 'Hero hit the enemy with {}-{}for {} dmg'.format(self.fight_type, self.hero.has_spell['name'], dmg_done)
            return msg
        msg = 'Hero have no mana to cast the spell or weapon has not enough range to atack the enemy. Standing still.'
        return msg

    def hero_close_fight(self):
        if self.is_spell_more_eq_dmg() and self.hero.can_cast():
            self.enemy.take_damage(self.hero.attack(by='spell'))
        self.enemy.take_damage(self.hero.attack(by='weapon'))

    def is_spell_more_eq_dmg(self):
        return self.hero.attack(by='spell') >= self.hero.attack(by='weapon')

    def enemy_move(self):
        if self.hero_drect_dist[1] > 1:
            self.hero_drect_dist[1] -= 1
            print('Enemy moves one step to the {} in order to get to the hero. This is his move.'.format(self.hero_drect_dist[0]))
            return True
        return False

    def fight_scenario(self):
        while self.distfight:
            if self.hero_drect_dist[1] >= 2:
                print(self.hero_fight_from_distance())
            self.distfight = self.enemy_move()


