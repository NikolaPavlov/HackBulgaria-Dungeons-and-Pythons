import unittest
from Dungeons import Dungeon, ThisIsNotAHero, WrongDirection
from Hero import Hero


class TestDungeons(unittest.TestCase):

    def setUp(self):
        self.outcast_land = Dungeon()
        self.fighter = Hero()
        self.outcast_land.spawn(self.fighter)

    def test_loading_map(self):
        self.assertEqual(type(self.outcast_land.dungeon_map), list)

    def test_show_map(self):
        print ("===== BEFORE ======")
        self.test_land = Dungeon()
        self.test_land.show_map()

    def test_spawn(self):
        alabala = "WTF"
        with self.assertRaises(ThisIsNotAHero):
            self.outcast_land.spawn(alabala)
        print("==== AFTER =====")
        self.outcast_land.show_map()

    def test_move_hero(self):
        with self.assertRaises(WrongDirection):
            self.outcast_land.move_hero("asdad")
        self.assertTrue(self.outcast_land.move_hero("right"), True)
        print ("NEXT MOVE")
        self.outcast_land.show_map()


if __name__ == "__main__":
    unittest.main()