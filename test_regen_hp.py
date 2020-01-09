from unittest import TestCase
from unittest.mock import patch
from character import regen_hp
import io


class TestRegen_hp(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_regen_hp_print(self, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        expected = "You recovered 2 HP.\n"
        regen_hp(test_char)
        self.assertEqual(expected, mock_output.getvalue())

    def test_regen_full_hp(self):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        expected = 10
        regen_hp(test_char)
        self.assertEqual(expected, test_char['current_hp'])

    def test_regen_9_hp(self):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 9, 'power': 6}
        expected = 10
        regen_hp(test_char)
        self.assertEqual(expected, test_char['current_hp'])

    def test_regen_half_hp(self):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 5, 'power': 6}
        expected = 7
        regen_hp(test_char)
        self.assertEqual(expected, test_char['current_hp'])
