import sys
sys.path.insert(0, '../Engine')
import unittest

from Enemy import Enemy
from Weapon import Weapon
from Spell import Spell


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy1 = Enemy()
        self.weapon1 = Weapon()
        self.spell1 = Spell()
        self.injured_enemy = Enemy()
        self.injured_enemy.current_health = 30
        self.injured_enemy.current_mana = 30
        self.dead_enemy = Enemy()
        self.dead_enemy.current_health = 0
        self.dead_enemy.current_mana = 0

    def test_constructor(self):
        self.assertIsInstance(self.enemy1, Enemy)

    def test_is_alive(self):
        self.assertTrue(self.enemy1.is_alive())

    def test_is_alive_false(self):
        self.assertFalse(self.dead_enemy.is_alive())

    def test_can_cast(self):
        self.assertTrue(self.enemy1.can_cast())

    def test_can_cast_false(self):
        self.assertFalse(self.dead_enemy.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy1.get_health(), 100)
        self.assertEqual(self.dead_enemy.get_health(), 0)

    def test_get_mana(self):
        self.assertEqual(self.enemy1.get_mana(), 100)
        self.assertEqual(self.dead_enemy.get_mana(), 0)

    def test_take_healing(self):
        self.injured_enemy.take_healing(20)
        self.assertEqual(self.injured_enemy.get_health(), 50)

    def test_take_healing_dead_enemy(self):
        self.assertFalse(self.dead_enemy.take_healing(20))

    def test_take_healing_massive_health(self):
        self.assertTrue(self.injured_enemy.take_healing(999))
        self.assertEqual(self.injured_enemy.get_health(), 100)

    def test_take_mana(self):
        pass

    def test_attack_with_weapon(self):
        self.enemy1.equip(self.weapon1)
        self.assertEqual(self.enemy1.attack(by='weapon'), 20)

    def test_attack_with_spell(self):
        self.enemy1.learn(self.spell1)
        self.assertEqual(self.enemy1.attack(by='spell'), 30)

    def test_attack_with_no_weapon_no_spell(self):
        self.assertEqual(self.enemy1.attack(by='weapon'), 20)


if __name__ == "__main__":
    unittest.main()
