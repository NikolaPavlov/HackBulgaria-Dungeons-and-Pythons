import unittest

from Weapon import Weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.weapon1 = Weapon()

    def test_constructor(self):
        self.assertIsInstance(self.weapon1, Weapon)

if __name__ == "__main__":
    unittest.main()
