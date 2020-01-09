from unittest import TestCase
from sud import validate_move

top_left = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
top_right = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
bot_left = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 2]]
bot_right = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]


class TestValidate_move(TestCase):

    def test_validate_move_0_0_move_east(self):
        test_board = top_left
        test_char = {'coords': (0, 0)}
        test_move = (1, 0)
        expected = True
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_0_0_move_south(self):
        test_board = top_left
        test_char = {'coords': (0, 0)}
        test_move = (0, 1)
        expected = True
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_0_0_move_north(self):
        test_board = top_left
        test_char = {'coords': (0, 0)}
        test_move = (0, -1)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_0_0_move_west(self):
        test_board = top_left
        test_char = {'coords': (0, 0)}
        test_move = (-1, 0)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_4_0_move_north(self):
        test_board = top_right
        test_char = {'coords': (4, 0)}
        test_move = (0, -1)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_4_0_move_east(self):
        test_board = top_right
        test_char = {'coords': (4, 0)}
        test_move = (1, 0)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_0_4_move_west(self):
        test_board = bot_left
        test_char = {'coords': (0, 4)}
        test_move = (-1, 0)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_0_4_move_south(self):
        test_board = bot_left
        test_char = {'coords': (0, 4)}
        test_move = (0, 1)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_4_4_move_south(self):
        test_board = bot_right
        test_char = {'coords': (4, 4)}
        test_move = (0, 1)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))

    def test_validate_move_4_4_move_east(self):
        test_board = bot_right
        test_char = {'coords': (4, 4)}
        test_move = (1, 0)
        expected = False
        self.assertEqual(expected, validate_move(test_board, test_char, test_move))
