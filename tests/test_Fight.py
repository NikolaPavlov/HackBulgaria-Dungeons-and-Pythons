import sys
import unittest
sys.path.insert(0, '../Engine')
sys.path.insert(0, '../resources')
from Fight import Fight
from Hero import Hero
from Spell import Spell
from Weapon import Weapon


class TestFight(unittest.TestCase):

    def setUp(self):
        self.pudge = Hero()
        self.magic = Spell(mana_cost=1)
        self.sword = Weapon(damage=60)
        self.pudge.learn(self.magic)
        self.pudge.equip(self.sword)
        self.battle = Fight(self.pudge, (4, 8), (4, 5), 'spell')

    def test_direct_and_dist(self):
        direct_and_dist = self.battle.find_direct_and_dist()
        self.assertEqual(direct_and_dist[0], 'right')
        self.assertEqual(direct_and_dist[1], 3)

    def test_is_spell_more_eq_dmg(self):
        self.assertFalse(self.battle.is_spell_more_eq_dmg())

    def test_fight_scenario(self):
        self.battle.fight_scenario()


if __name__ == '__main__':
    unittest.main()
