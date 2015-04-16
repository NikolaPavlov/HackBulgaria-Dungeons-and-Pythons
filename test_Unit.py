import unittest
from Unit import Unit


class TestUnit(unittest.TestCase):

    def setUp(self):
        self.unit1 = Unit(100, 100)
        self.injured_unit = Unit(50, 50)
        self.dead_unit = Unit(0, 0)

    def test_constructor(self):
        self.assertIsInstance(self.unit1, Unit)

    def test_is_alive(self):
        self.assertTrue(self.unit1.is_alive())

    def test_is_alive_false(self):
        self.assertFalse(self.dead_unit.is_alive())

    def test_get_health(self):
        self.assertEqual(self.unit1.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.unit1.get_mana(), 100)

    def test_can_cast(self):
        self.assertTrue(self.unit1.can_cast())

    def test_can_cast_false(self):
        self.assertFalse(self.dead_unit.can_cast())

    def test_take_healing(self):
        self.injured_unit.current_health = 1
        self.injured_unit.take_healing(10)
        self.assertEqual(self.injured_unit.get_health(), 11)

    def test_take_healing_to_max1(self):
        self.injured_unit.take_healing(999)
        self.assertEqual(self.injured_unit.get_health(), 50)

    def test_take_healing_to_max2(self):
        self.injured_unit.current_health = 1
        self.injured_unit.take_healing(999)
        self.assertEqual(self.injured_unit.get_health(), 50)

if __name__ == "__main__":
    unittest.main()
