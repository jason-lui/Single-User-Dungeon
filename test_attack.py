from unittest import TestCase
from unittest.mock import patch
from sud import attack
import io


class TestAttack(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", return_value=1)
    def test_attack_hp_below_0(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 0, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 0, 'power': 6, 'backstab': 4}
        expected = ""
        attack(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", return_value=4)
    def test_attack_attack_fail(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """Goblin's HP: 5/5
Link's attack failed!
Goblin's HP: 5/5

"""
        attack(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 4])
    def test_attack_attack_success_but_no_kill(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """Goblin's HP: 5/5
The attack was a success!
Goblin took 4 damage.
Goblin's HP: 1/5

"""
        attack(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 6])
    def test_attack_attack_success_and_kill(self, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """Goblin's HP: 5/5
The attack was a success!
Goblin took 6 damage.
Goblin has died!
"""
        attack(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())
