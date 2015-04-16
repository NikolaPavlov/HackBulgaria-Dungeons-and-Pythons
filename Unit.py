class Unit:

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self.current_health = health
        self.current_mana = mana

    def is_alive(self):
        return self.current_health > 0

    def get_health(self):
        return self.current_health

    def get_mana(self):
        return self.current_mana

    def can_cast(self):
        return self.current_mana > 0

    def take_healing(self, healing_points):
        if self.current_health <= 0:
            return False

        # Haling to the max points
        if self.current_health + healing_points > self.health:
            self.current_health = self.health
            return True

        # Just heal
        self.current_health += healing_points
        return True

    def take_mana(self):
        pass

    def attack(self):
        pass

