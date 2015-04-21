from Unit import Unit


class Hero(Unit):

    def __init__(
            self,
            name="Bron",
            title="Dragonslayer",
            health=100,
            mana=100,
            mana_regeneration_rate=2):
        Unit.__init__(self, health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def __repr__(self):
        return '{} with {}/{} health/mana'.format(Hero.__name__, self.current_health, self.current_mana)

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def regen_mana(self):
        super(Hero, self).take_mana(self.mana_regeneration_rate)
