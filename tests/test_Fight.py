import sys
import unittest
sys.path.insert(0, '../Engine')
sys.path.insert(0, '../resources')
from Fight import Fight
from Hero import Hero


class TestFight(unittest.TestCase):

    def setUp(self):
        self.pudge = Hero()
        self.battle = Fight(self.pudge, (4, 6), (4, 5), 'spell')

    def test_determinate_hero_direct(self):
        direct_and_dist = self.battle.find_direct_and_dist()
        self.assertEqual(direct_and_dist[0], 'right')
        self.assertEqual(direct_and_dist[1], 1)

    def test_fight_scenario(self):
        pass


if __name__ == '__main__':
    unittest.main()
