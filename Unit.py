from Weapon import Weapon
from Spell import Spell


class Unit:

    def __init__(self, health, mana):
        '''
        rename damage to attack points for
        better understanding
        '''
        self.health = health
        self.mana = mana
        self.attack_points = 0
        self.current_health = health
        self.current_mana = mana
        self.has_weapon = {}
        self.has_spell = {}

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

    def take_damage(self, damage_points):
        self.current_health -= damage_points
        if self.current_health < 0:
            self.current_health = 0

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.has_weapon = weapon.get_properties()

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.has_spell = spell.get_properties()

    # enemy can attack withowth weapon or spell
    def attack(self, by):
        if by == 'weapon':
            if 'damage' in self.has_weapon:
                return self.has_weapon['damage']
            else:
                return int(self.attack_points)
        if by == 'spell':
            if 'damage' in self.has_spell:
                return self.has_spell['damage']
            else:
                return self.attack_points
