class Weapon:

    def __init__(self, name="The Axe of Destiny", damage=20):
        self.name = name
        self.damage = damage

    def get_properties(self):
        weapon_property = {}
        weapon_property['name'] = self.name
        weapon_property['damage'] = self.damage
        return weapon_property
