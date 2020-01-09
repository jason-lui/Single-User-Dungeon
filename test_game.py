from unittest import TestCase
from unittest.mock import patch
from sud import game
import io


class TestGame(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=['5'])
    def test_game_instantly_quit(self, mock_input, mock_output):
        expected = "You wake up. You realize that you are in a maze of some " \
                   "sort. There are 2 doorways in this room: south and east.\n" \
                   "1 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "Where would you like to move?\n" \
                   "1. North, 2. East, 3. South, 4. West or 5. Quit\n" \
                   "\n" \
                   "You killed 0 monsters before you died.\n"
        game()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=['5'])
    def test_game_instantly_quit(self, mock_input, mock_output):
        expected = "You wake up. You realize that you are in a maze of some sort. There are 2 " \
                   "\ndoorways in this room: south and east.\n\n" \
                   "1 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "Where would you like to move?\n" \
                   "1. North, 2. East, 3. South, 4. West or 5. Quit\n" \
                   "\n" \
                   "You killed 0 monsters before you died.\n"
        game()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.randint", side_effect=[1])
    @patch("sud.roll_die", side_effect=[4, 20, 1, 4, 3, 10])
    @patch("builtins.input", side_effect=['2', '1'])
    def test_game_instantly_die(self, mock_input, mock_roll, mock_int, mock_output):
        expected = "You wake up. You realize that you are in a maze of some sort. There are 2 \n" \
                   "doorways in this room: south and east.\n" \
                   "\n" \
                   "1 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "Where would you like to move?\n" \
                   "1. North, 2. East, 3. South, 4. West or 5. Quit\n" \
                   "\n" \
                   "You find a treasure chest in this room. You open the chest. Only a few gold \n" \
                   "coins... Bummer.\n" \
                   "\n" \
                   "You encountered a Goblin!\n" \
                   "What would you like to do?\n" \
                   "\n" \
                   "Link will go first.\n" \
                   "Goblin's HP: 5/5\n" \
                   "Link's attack failed!\n" \
                   "Goblin's HP: 5/5\n" \
                   "\n" \
                   "Link's HP: 10/10\n" \
                   "The attack was a success!\n" \
                   "Link took 10 damage.\n" \
                   "Link has died!\n" \
                   "You died. Game over.\n" \
                   "HP: 0/10\n" \
                   "You killed 0 monsters before you died.\n"
        game()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.randint", side_effect=[1, 2])
    @patch("sud.roll_die", side_effect=[4, 20, 1, 3, 6, 4, 20, 1, 4, 3, 10])
    @patch("builtins.input", side_effect=['2', '1', '2', '1'])
    def test_game_kill_1_and_then_die(self, mock_input, mock_roll, mock_int, mock_output):
        expected = "You wake up. You realize that you are in a maze of some sort. There are 2 " \
                   "\ndoorways in this room: south and east.\n" \
                   "\n" \
                   "1 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "Where would you like to move?\n" \
                   "1. North, 2. East, 3. South, 4. West or 5. Quit\n" \
                   "\n" \
                   "You find a treasure chest in this room. You open the chest. Only a few gold \n" \
                   "coins... Bummer.\n" \
                   "\n" \
                   "You encountered a Goblin!\n" \
                   "What would you like to do?\n" \
                   "\n" \
                   "Link will go first.\n" \
                   "Goblin's HP: 5/5\n" \
                   "The attack was a success!\n" \
                   "Goblin took 6 damage.\n" \
                   "Goblin has died!\n" \
                   "You killed Goblin!\n" \
                   "\n" \
                   "HP: 10/10\n" \
                   "0 1 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "0 0 0 0 0\n" \
                   "Where would you like to move?\n" \
                   "1. North, 2. East, 3. South, 4. West or 5. Quit\n" \
                   "\n" \
                   "You decide to continue on the top side of the maze. You find some writing on the " \
                   "\nwall. It says \"The exit is at (4, ...\". You can't make out the rest.\n" \
                   "\n" \
                   "You encountered a Goomba!\n" \
                   "What would you like to do?\n" \
                   "\n" \
                   "Link will go first.\n" \
                   "Goomba's HP: 5/5\n" \
                   "Link's attack failed!\n" \
                   "Goomba's HP: 5/5\n" \
                   "\n" \
                   "Link's HP: 10/10\n" \
                   "The attack was a success!\n" \
                   "Link took 10 damage.\n" \
                   "Link has died!\n" \
                   "You died. Game over.\n" \
                   "HP: 0/10\n" \
                   "You killed 1 monsters before you died.\n"
        game()
        self.assertEqual(expected, mock_output.getvalue())
