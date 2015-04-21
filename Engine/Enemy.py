from Unit import Unit


class Enemy(Unit):

    def __init__(self, health=100, mana=100, damage=20):
        Unit.__init__(self, health, mana)
        self.attack_points = damage

    def __repr__(self):
        return '{} with {}/{} health/mana'.format(Enemy.__name__, self.current_health, self.current_mana)
