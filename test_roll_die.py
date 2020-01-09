from unittest import TestCase
from sud import roll_die


class TestRoll_die(TestCase):

    def test_roll_10_0(self):
        number_of_rolls = 10
        number_of_sides = 0
        expected = 0
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))

    def test_roll_0_10(self):
        number_of_rolls = 0
        number_of_sides = 10
        expected = 0
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))

    def test_roll_true(self):
        number_of_rolls = 10
        number_of_sides = 10
        res = roll_die(number_of_rolls, number_of_sides)
        self.assertTrue(number_of_rolls <= res <= number_of_rolls * number_of_sides)
