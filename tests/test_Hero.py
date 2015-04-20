import sys
sys.path.insert(0, '../Engine')
import unittest
from Hero import Hero
from Weapon import Weapon
from Spell import Spell


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero1 = Hero()
        self.weapon1 = Weapon()
        self.spell1 = Spell()
        self.dead_hero = Hero()
        self.dead_hero.current_health = 0
        self.dead_hero.current_mana = 0
        self.injured_hero = Hero()
        self.injured_hero.current_health = 10
        self.injured_hero.current_mana = 10

        # print(self.hero1.can_cast())
        # print(self.dead_hero.can_cast())

    def test_constructor(self):
        self.assertIsInstance(self.hero1, Hero)

    def test_known_as(self):
        self.assertEqual(self.hero1.known_as(), 'Bron the Dragonslayer')

    def test_is_alive(self):
        self.assertTrue(self.hero1.is_alive())

    def test_is_alive_false(self):
        self.assertFalse(self.dead_hero.is_alive())

    def test_get_health(self):
        self.assertEqual(self.dead_hero.get_health(), 0)
        self.assertEqual(self.hero1.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.dead_hero.get_mana(), 0)
        self.assertEqual(self.hero1.get_mana(), 100)

    def can_cast(self):
        self.assertFalse(self.hero1.can_cast())

    def can_cast_false(self):
        self.assertFalse(self.dead_hero.can_cast())

    def test_take_healing(self):
        self.injured_hero.take_healing(20)
        self.assertEqual(self.injured_hero.get_health(), 30)

    def test_take_healing_dead_hero(self):
        self.assertFalse(self.dead_hero.take_healing(20))

    def test_take_healing_massive_health(self):
        self.assertTrue(self.injured_hero.take_healing(999))
        self.assertEqual(self.injured_hero.get_health(), 100)

    def test_take_mana(self):
        self.hero1.learn(self.spell1)
        self.hero1.attack(by='spell')
        self.hero1.regen_mana()
        self.assertEqual(self.hero1.get_mana(), 52)
        self.hero1.take_mana(99)
        self.assertEqual(self.hero1.get_mana(), 100)

    def test_equip(self):
        self.hero1.equip(self.weapon1)
        self.assertEqual(self.hero1.has_weapon, {'damage': 20, 'name': 'The Axe of Destiny'})

    def test_learn(self):
        self.hero1.learn(self.spell1)
        self.assertEqual(self.hero1.has_spell, {'name': 'Fireball', 'damage': 30, 'mana_cost': 50, 'cast_range': 2})

    def test_attack_with_weapon(self):
        self.hero1.equip(self.weapon1)
        self.assertEqual(self.hero1.attack(by='weapon'), 20)

    def test_attack_with_spell(self):
        self.hero1.learn(self.spell1)
        self.assertEqual(self.hero1.attack(by='spell'), 30)

    def test_attack_with_no_weapon_no_spell(self):
        self.assertEqual(self.hero1.attack(by='weapon'), 0)


if __name__ == "__main__":
    unittest.main()
