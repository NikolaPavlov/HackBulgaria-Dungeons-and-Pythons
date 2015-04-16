from Unit import Unit


class Enemy(Unit):

    def __init__(self, health=100, mana=100, damage=20):
        Unit.__init__(self, health, mana)
        self.damage = damage

