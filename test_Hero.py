import unittest
from Hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero1 = Hero()

    def test_constructor(self):
        self.assertIsInstance(self.hero1, Hero)

    def test_known_as(self):
        self.assertEqual(self.hero1.known_as(), 'Bron the Dragonslayer')

    def test_take_damage(self):
        self.hero1.take_damage(10)
        self.assertEqual(self.hero1.get_health(), 90)

    def test_take_massive_damage(self):
        self.hero1.take_damage(999)
        self.assertEqual(self.hero1.get_health(), 0)


if __name__ == "__main__":
    unittest.main()
