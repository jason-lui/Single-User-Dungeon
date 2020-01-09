from unittest import TestCase
from sud import update_board


class TestUpdate_board(TestCase):

    def test_update_board_char_0_0_exit_4_4(self):
        char = {'coords': (0, 0)}
        expected = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(expected, update_board(char))

    def test_update_board_char_4_4_exit_4_4(self):
        char = {'coords': (4, 4)}
        expected = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
        self.assertEqual(expected, update_board(char))

    def test_update_board_char_1_1_exit_4_4(self):
        char = {'coords': (1, 1)}
        expected = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(expected, update_board(char))

    def test_update_board_char_error_negative_out_of_bounds(self):
        char = {'coords': (-10, -10)}
        expected = IndexError
        self.assertRaises(expected, update_board, char)

    def test_update_board_char_error_positive_out_of_bounds(self):
        char = {'coords': (10, 10)}
        expected = IndexError
        self.assertRaises(expected, update_board, char)
