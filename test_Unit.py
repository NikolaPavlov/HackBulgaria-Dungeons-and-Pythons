import unittest
from Unit import Unit
from Weapon import Weapon
from Spell import Spell


class TestUnit(unittest.TestCase):

    def setUp(self):
        self.unit1 = Unit(100, 100)
        self.injured_unit = Unit(50, 50)
        self.dead_unit = Unit(0, 0)
        self.weapon1 = Weapon()
        self.spell1 = Spell()

        # print(self.unit1.has_weapon)

    def test_constructor(self):
        self.assertIsInstance(self.unit1, Unit)

    def test_is_alive(self):
        self.assertTrue(self.unit1.is_alive())

    def test_is_alive_false(self):
        self.assertFalse(self.dead_unit.is_alive())

    def test_get_health(self):
        self.assertEqual(self.unit1.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.unit1.get_mana(), 100)

    def test_can_cast(self):
        self.assertTrue(self.unit1.can_cast())

    def test_can_cast_false(self):
        self.assertFalse(self.dead_unit.can_cast())

    def test_take_healing(self):
        self.injured_unit.current_health = 1
        self.injured_unit.take_healing(10)
        self.assertEqual(self.injured_unit.get_health(), 11)

    def test_take_healing_to_max1(self):
        self.injured_unit.take_healing(999)
        self.assertEqual(self.injured_unit.get_health(), 50)

    def test_take_healing_to_max2(self):
        self.injured_unit.current_health = 1
        self.injured_unit.take_healing(999)
        self.assertEqual(self.injured_unit.get_health(), 50)

    def test_take_mana(self):
        pass

    def test_equip(self):
        self.unit1.equip(self.weapon1)
        self.assertEqual(self.unit1.has_weapon, {'damage': 20, 'name': 'The Axe of Destiny'})

    def test_learn(self):
        self.unit1.learn(self.spell1)
        self.assertEqual(self.unit1.has_spell, {'name': 'Fireball', 'damage': 30, 'mana_cost': 50, 'cast_range': 2})

    def test_attack_by_weapon(self):
        self.unit1.equip(self.weapon1)
        self.assertEqual(self.unit1.attack(by="weapon"), 20)

    def test_attack_by_spell(self):
        self.unit1.learn(self.spell1)
        self.assertEqual(self.unit1.attack(by="spell"), 30)

if __name__ == "__main__":
    unittest.main()