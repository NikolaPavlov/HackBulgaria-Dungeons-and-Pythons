from Unit import Unit


class Hero(Unit):

    def __init__(
        self, \
        name="Bron", \
        title="Dragonslayer", \
        health=100, \
        mana=100, \
        mana_regeneration_rate=2):
        Unit.__init__(self, health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def take_damage(self, damage_points):
        self.current_health -= damage_points
        if self.current_health < 0:
            self.current_health = 0
