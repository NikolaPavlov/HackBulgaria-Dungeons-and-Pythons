from Weapon import Weapon
from Spell import Spell


class Unit:

    def __init__(self, health, mana):
        self.max_health = health
        self.mana = mana
        self.attack_points = 0
        self.current_health = self.max_health
        self.current_mana = mana
        self.has_weapon = {'name': 'Fist', 'damage': 0}
        self.has_spell = {}

    def is_alive(self):
        return self.current_health > 0

    def get_health(self):
        return self.current_health

    def get_mana(self):
        return self.current_mana

    def can_cast(self):
        if self.has_spell:
            return self.current_mana >= self.has_spell['mana_cost']
        else:
            return False

    def take_healing(self, healing_points):
        if self.current_health <= 0:
            return False
        self.current_health += healing_points
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        return True

    def take_mana(self, mana_points=0):
        self.current_mana += mana_points
        if self.current_mana > self.mana:
            self.current_mana = self.mana
        return True

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
    def attack(self, by='fist'):
        if by == 'weapon':
            if 'damage' in self.has_weapon:
                return self.has_weapon['damage']
            else:
                return self.attack_points

        if by == 'spell':
            if 'damage' in self.has_spell:
                self.current_mana -= self.has_spell['mana_cost']
                return self.has_spell['damage']
            else:
                return self.attack_points

        return self.attack_points
