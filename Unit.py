class Unit:

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return self.mana > 0