import sys
sys.path.insert(0, '../Engine')
sys.path.insert(0, '../resources')
import unittest
from Dungeons import Dungeon, ThisIsNotAHero, WrongDirection
from Hero import Hero


class TestDungeons(unittest.TestCase):

    def setUp(self):
        self.outcast_land = Dungeon()
        self.fighter = Hero(name='Centaur', title='Warrunner')
        self.outcast_land.spawn(self.fighter)

    def test_loading_map(self):
        self.assertEqual(type(self.outcast_land.dungeon_map), list)
        self.assertEqual(len(self.outcast_land.dungeon_map[0]), 10)

    def test_show_map(self):
        # print("===== BEFORE RESP======")
        self.test_land = Dungeon()
        # self.test_land.show_map()

    def test_spawn(self):
        alabala = "WTF"
        with self.assertRaises(ThisIsNotAHero):
            self.outcast_land.spawn(alabala)
        # print("==== AFTER RESP =====")
        # self.outcast_land.show_map()

    def test_move_hero_right_once(self):
        with self.assertRaises(WrongDirection):
            self.outcast_land.move_hero("asdad")
        self.assertTrue(self.outcast_land.move_hero("right"))
        self.assertFalse(self.outcast_land.move_hero("up"))

    def test_move_hero_right_twice_hit_wall(self):
        self.assertTrue(self.outcast_land.move_hero("right"))
        self.assertFalse(self.outcast_land.move_hero("right"))

    def test_move_hero_right_once_down_once(self):
        self.assertTrue(self.outcast_land.move_hero("right"))
        self.assertTrue(self.outcast_land.move_hero("down"))

    def test_move_hero_right_once_down_three(self):
        self.assertTrue(self.outcast_land.move_hero("right"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("down"))

    def test_move_hero_right_once_hit_bottom_wall(self):
        self.assertTrue(self.outcast_land.move_hero("right"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertFalse(self.outcast_land.move_hero("down"))

    def test_first_right_turn(self):
        self.assertTrue(self.outcast_land.move_hero("right"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("down"))
        self.assertTrue(self.outcast_land.move_hero("right"))
        # self.outcast_land.show_map()

    def test_update_map(self):
        self.assertTrue(self.outcast_land.move_hero("right"), True)
        # print("==== Move right ====")
        # self.outcast_land.show_map()


if __name__ == "__main__":
    unittest.main()
