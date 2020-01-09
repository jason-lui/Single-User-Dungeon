from unittest import TestCase
from character import move_character


class TestMove_character(TestCase):

    def test_move_character_north(self):
        test_char = {'coords': (2, 2)}
        test_move = (0, -1)
        expected = {'coords': (2, 1)}
        self.assertEqual(expected, move_character(test_char, test_move))
        
    def test_move_character_east(self):
        test_char = {'coords': (2, 2)}
        test_move = (1, 0)
        expected = {'coords': (3, 2)}
        self.assertEqual(expected, move_character(test_char, test_move))
        
    def test_move_character_south(self):
        test_char = {'coords': (2, 2)}
        test_move = (0, 1)
        expected = {'coords': (2, 3)}
        self.assertEqual(expected, move_character(test_char, test_move))
        
    def test_move_character_west(self):
        test_char = {'coords': (2, 2)}
        test_move = (-1, 0)
        expected = {'coords': (1, 2)}
        self.assertEqual(expected, move_character(test_char, test_move))
        
    def test_move_character_north_out_of_bounds(self):
        test_char = {'coords': (0, 0)}
        test_move = (0, -1)
        expected = {'coords': (0, -1)}
        self.assertEqual(expected, move_character(test_char, test_move))
