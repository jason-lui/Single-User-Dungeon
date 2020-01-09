from unittest import TestCase
from unittest.mock import patch
from sud import roll_order
import io


class TestRoll_order(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[20, 1])
    def test_roll_order_print_1(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 10, 'power': 6, 'backstab': 4}
        expected = "\nLink will go first.\n"
        roll_order(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 1, 1, 20])
    def test_roll_order_roll_again_print(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 10, 'power': 6, 'backstab': 4}
        expected = "Both players rolled 1! Rolling again...\n\nGoblin will go first.\n"
        roll_order(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[20, 1])
    def test_roll_order_roll_1(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 10, 'power': 6, 'backstab': 4}
        expected = [test_char, test_monster]
        self.assertEqual(expected, roll_order(test_char, test_monster))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 20])
    def test_roll_order_roll_2(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 10, 'power': 6, 'backstab': 4}
        expected = [test_monster, test_char]
        self.assertEqual(expected, roll_order(test_char, test_monster))
