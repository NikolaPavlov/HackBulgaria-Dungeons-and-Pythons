import sys
import unittest
sys.path.insert(0, '../Engine')
sys.path.insert(0, '../resources')
from Fight import Fight
from Hero import Hero
from Spell import Spell
from Weapon import Weapon
# WTF IS HAPPANANNASDANSDS ALA BALa TEST !!!!

class TestFight(unittest.TestCase):

    def setUp(self):
        self.pudge = Hero()
        self.magic = Spell(mana_cost=5, damage=33)
        self.sword = Weapon(damage=30)
        self.pudge.learn(self.magic)
        self.pudge.equip(self.sword)
        self.battle = Fight(self.pudge, (4, 6), (4, 5), 'walk')

    def test_direct_and_dist(self):
        direct_and_dist = self.battle.find_direct_and_dist()
        self.assertEqual(direct_and_dist[0], 'right')
        self.assertEqual(direct_and_dist[1], 1)

    def test_is_spell_more_eq_dmg(self):
        self.assertTrue(self.battle.is_spell_more_eq_dmg())

    def test_fight_scenario(self):
        self.assertTrue(self.battle.fight_scenario())
        print (self.battle)

    def test_combat_logg(self):
        pass



if __name__ == '__main__':
    unittest.main()
