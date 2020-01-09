from unittest import TestCase
from unittest.mock import patch
from sud import combat_round
import io


class TestCombat_round(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", return_value=1)
    @patch("builtins.input", side_effect=[2, 3])
    def test_combat_round_flee_no_backstab(self, mock_input, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """You encountered a Goblin!
What would you like to do?
You ran away from Goblin successfully.
"""
        combat_round(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 3])
    @patch("builtins.input", side_effect=[2, 4])
    def test_combat_round_flee_with_backstab(self, mock_input, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 10, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """You encountered a Goblin!
What would you like to do?
You ran away from Goblin successfully.
"""
        combat_round(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[4, 4])
    @patch("builtins.input", side_effect=[2, 4])
    def test_combat_round_flee_with_backstab_and_dies(self, mock_input, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 3, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """You encountered a Goblin!
What would you like to do?
Goblin backstabbed you for 4 damage!
You died. Game over.
"""
        combat_round(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[4, 4])
    @patch("builtins.input", side_effect=[4, 4, 4, 2, 4])
    def test_combat_round_invalid_input_then_backstabbed_and_killed(self, mock_input, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 3, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """You encountered a Goblin!
What would you like to do?
Goblin backstabbed you for 4 damage!
You died. Game over.
"""
        combat_round(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 5, 1, 1, 5, 5])
    @patch("builtins.input", side_effect=[1, 1, 1, 1, 1, 1])
    def test_combat_round_enemy_first_and_kill(self, mock_input, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 3, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """You encountered a Goblin!
What would you like to do?

Goblin will go first.
Link's HP: 3/10
The attack was a success!
Link took 1 damage.
Link's HP: 2/10

Goblin's HP: 5/5
The attack was a success!
Goblin took 5 damage.
Goblin has died!
You killed Goblin!

"""
        combat_round(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("sud.roll_die", side_effect=[1, 1, 6, 1, 5, 5])
    @patch("builtins.input", side_effect=[1, 1, 1, 1, 1, 1])
    def test_combat_round_player_first_and_kill(self, mock_input, mock_roll, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 3, 'power': 6}
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        expected = """You encountered a Goblin!
What would you like to do?
Both players rolled 1! Rolling again...

Link will go first.
Goblin's HP: 5/5
The attack was a success!
Goblin took 5 damage.
Goblin has died!
You killed Goblin!

"""
        combat_round(test_char, test_monster)
        self.assertEqual(expected, mock_output.getvalue())
