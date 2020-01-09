from unittest import TestCase
from unittest.mock import patch
import io
from sud import get_user_choice


class TestGet_user_choice(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1"])
    def test_get_user_choice_valid_print(self, mock_input, mock_output):
        expected = """Where would you like to move?
1. North, 2. East, 3. South, 4. West or 5. Quit

"""
        get_user_choice()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["c", "1"])
    def test_get_user_choice_invalid_print(self, mock_input, mock_output):
        expected = """Where would you like to move?
1. North, 2. East, 3. South, 4. West or 5. Quit
That is not a valid move.

"""
        get_user_choice()
        self.assertEqual(expected, mock_output.getvalue())

    # Keep stdout so that print statements are not shown while unit testing return values
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value="1")
    def test_get_user_choice_1_return_value(self, mock_input, mock_output):
        expected = (0, -1)
        self.assertEqual(expected, get_user_choice())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value="2")
    def test_get_user_choice_2_return_value(self, mock_input, mock_output):
        expected = (1, 0)
        self.assertEqual(expected, get_user_choice())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value="3")
    def test_get_user_choice_3_return_value(self, mock_input, mock_output):
        expected = (0, 1)
        self.assertEqual(expected, get_user_choice())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value="4")
    def test_get_user_choice_4_return_value(self, mock_input, mock_output):
        expected = (-1, 0)
        self.assertEqual(expected, get_user_choice())
