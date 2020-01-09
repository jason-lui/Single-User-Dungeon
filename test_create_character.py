from unittest import TestCase
from character import create_character


class TestCreate_character(TestCase):

    def test_create_character(self):
        expected = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        self.assertEqual(expected, create_character())
