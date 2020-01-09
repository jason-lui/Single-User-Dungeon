from unittest import TestCase
from sud import make_board


class TestMake_board(TestCase):

    def test_make_board(self):
        expected = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(expected, make_board())
