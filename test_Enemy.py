import unittest

from Enemy import Enemy


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy1 = Enemy()

    def test_constructor(self):
        self.assertIsInstance(self.enemy1, Enemy)


if __name__ == "__main__":
    unittest.main()
