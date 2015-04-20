class Spell:

    def __init__(self, name="Fireball", damage=30, mana_cost=50, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def get_properties(self):
        spell_property = {}
        spell_property['name'] = self.name
        spell_property['damage'] = self.damage
        spell_property['mana_cost'] = self.mana_cost
        spell_property['cast_range'] = self.cast_range
        return spell_property
