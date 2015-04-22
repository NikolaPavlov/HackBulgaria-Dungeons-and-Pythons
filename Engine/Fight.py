from Enemy import Enemy


class Fight:
    COMBATLOG1 = 'Hero hit the enemy with {}-{} for {} dmg!'
    COMBATLOG2 = 'Enemy moves one step to the {} in order to get to the hero. This is his move!'
    COMBATLOG3 = 'Hero have no mana to cast the spell or weapon has not enough range to atack the enemy. Standing still!'
    COMBATLOG4 = 'Enemy hit the Hero with fist for {} dmg!'
    COMBATLOG5 = 'Hero killed the enemy. Enemy is DEAD!!!'
    COMBATLOG6 = '{} current health {}!'
    COMBATLOG7 = 'Enemy killed the Hero. Hero is DEAD!!!'
    COMBATLOG8 = '{} current mana {}!'
    SPELL = 'spell'
    WEAPON = 'weapon'
    ENEMY = 'Enemy'
    HERO = 'Hero'

    def __init__(self, hero, hero_pos, enemy_pos, fight_type='walk'):
        self.hero = hero
        self.hero_pos = hero_pos
        self.enemy_pos = enemy_pos
        self.fight_type = fight_type
        self.enemy = Enemy(100, 100, 8)
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
        if self.fight_type == Fight.SPELL and self.hero.can_cast() and self.hero_drect_dist[1] > 1:
            dmg_done = self.hero.attack(by=self.fight_type)
            self.enemy.take_damage(dmg_done)
            msg = Fight.COMBATLOG1.format(self.fight_type, self.hero.has_spell['name'], dmg_done)
            return msg + Fight.COMBATLOG6.format(Fight.ENEMY, self.enemy.get_health())

        elif self.hero_drect_dist[1] == 1:
            return(self.hero_close_fight())

        elif self.fight_type == Fight.WEAPON:
            dmg_done = self.hero.attack(by=self.fight_type)
            self.enemy.take_damage(dmg_done)
            msg = Fight.COMBATLOG1.format(Fight.WEAPON, self.hero.has_weapon['name'], dmg_done)
            return msg + Fight.COMBATLOG6.format(Fight.ENEMY, self.enemy.get_health())

        else:
            msg = Fight.COMBATLOG3
            return msg + Fight.COMBATLOG8.format(Fight.HERO, self.hero.get_mana())

    def hero_close_fight(self):
        if self.is_spell_more_eq_dmg() and self.hero.can_cast():
            dmg_done = self.hero.attack(by=Fight.SPELL)
            self.enemy.take_damage(dmg_done)
            msg = Fight.COMBATLOG1.format(Fight.SPELL, self.hero.has_spell['name'], dmg_done)
            return msg + Fight.COMBATLOG6.format(Fight.ENEMY, self.enemy.get_health())

        else:
            dmg_done = self.hero.attack(by=Fight.WEAPON)
            self.enemy.take_damage(dmg_done)
            msg = Fight.COMBATLOG1.format(Fight.WEAPON, self.hero.has_weapon['name'], dmg_done)
            return msg + Fight.COMBATLOG6.format(Fight.ENEMY, self.enemy.get_health())

    def is_spell_more_eq_dmg(self):
        if self.hero.has_spell:
            return self.hero.has_spell['damage'] >= self.hero.has_weapon['damage']
        return False

    def enemy_move(self):
        if self.hero_drect_dist[1] > 1:
            self.hero_drect_dist[1] -= 1
            print(Fight.COMBATLOG2.format(self.hero_drect_dist[0]))
            return True
        return False

    def enemy_fight(self):
        dmg_done = self.enemy.attack()
        self.hero.take_damage(dmg_done)
        msg = Fight.COMBATLOG4.format(dmg_done)
        return msg + Fight.COMBATLOG6.format(Fight.HERO, self.hero.get_health())

    def fight_scenario(self):
        while self.distfight:
            if self.hero.is_alive():
                print(self.hero_fight_from_distance())
            if self.enemy.is_alive():
                self.distfight = self.enemy_move()
            else:
                print(Fight.COMBATLOG5)
                self.distfight = False

        while self.hero.is_alive() and self.enemy.is_alive():
            if self.enemy.is_alive():
                print(self.enemy_fight())
            print(self.hero_close_fight())

        if not self.hero.is_alive():
            print (Fight.COMBATLOG7)
            return False
        elif not self.enemy.is_alive():
            return True
            print (Fight.COMBATLOG5)
