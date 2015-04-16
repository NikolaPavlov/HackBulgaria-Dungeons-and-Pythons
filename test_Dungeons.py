import unittest
from Dungeons import Dungeon


class TestDungeons(unittest.TestCase):

    def setUp(self):
        self.outcast_land = Dungeon()

    def test_loading_map(self):
        self.assertEqual(type(self.outcast_land.dungeon_map), list)

    def test_show_map(self):
        self.outcast_land.show_map()


if __name__ == "__main__":
    unittest.main()
