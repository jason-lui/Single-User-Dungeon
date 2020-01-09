from unittest import TestCase
from unittest.mock import patch
from sud import describe
import io

board_descriptions = {(0, 0): 'You wake up. You realize that you are in a maze of some sort. There are 2 doorways '
                              'in this room: south and east.',
                      (0, 1): 'You enter a dimly lit room. You see some symbols on the wall and a broken sword.',
                      (0, 2): 'You slowly walk into a room. There was a trap hole! You narrowly avoid it. Phew!',
                      (0, 3): 'You find a room with some rats. Despite being rats, they\'re quite friendly.',
                      (0, 4): 'You are the corner of the maze. Nothing interesting here.',
                      (1, 0): 'You find a treasure chest in this room. You open the chest. Only a few gold '
                              'coins... Bummer.',
                      (1, 1): 'You find a treasure chest in this room. You open the chest. You find a new car! '
                              'You don\'t have your license though.',
                      (1, 2): 'You find a treasure chest in this room. You open the chest. You find purpose in '
                              'life. Wow, that was deep!',
                      (1, 3): 'You find a treasure chest in this room. You open the chest. Empty... Rats!',
                      (1, 4): 'You find a treasure chest in this room. You open the chest. It\'s full of treasure! '
                              'Gems, jewellery, gold bars, doubloons, and trinkets. How lucky!',
                      (2, 0): 'You decide to continue on the top side of the maze. You find some writing on the '
                              'wall. It says "The exit is at (4, ...". You can\'t make out the rest.',
                      (2, 1): 'You enter a room with a table with bread and water. The bread looks stale, but the '
                              'water is clean... or at least you think it is. You eat the bread anyways and you '
                              'take a mouthful of water.',
                      (2, 2): 'You are at the center of maze now. You see a skeleton with a book next to it. '
                              'You open the book. In large sans serif font "DO YOUR UNIT TESTS OR YOU WILL '
                              'END UP LIKE ME". Yeesh! You drop the book.',
                      (2, 3): 'You enter a room with some lit candles. These candles look like they\'ve been '
                              'burning for a while now.',
                      (2, 4): 'You walk along the east side of the maze. You hear a noise that sounds like '
                              'chatting. You wonder if someone else is in here with you.',
                      (3, 0): 'You walk along the west side of the maze. You see a window to the outside world. '
                              'You try to squeeze through the window. You\'re too big to make it through. Darn it! '
                              'You shouldn\'t have eaten so many donuts.',
                      (3, 1): 'You fall into a trap hole! You feel around the dark for anything to climb on. '
                              'You press a button that drops a rope down from the ceiling. You climb out of the '
                              'pit. Phew that was close.',
                      (3, 2): 'You step on a pressure plate as your enter this room. A large boulder falls from '
                              'the ceiling. Oh no! You narrowly evade the falling boulder. Phew that was a close '
                              'one.',
                      (3, 3): 'You enter a bedroom. You see a large comfy bed. You decide to take a nap in it. '
                              'You sleep for a bit and wake up refreshed.',
                      (3, 4): 'You enter a room with a black cat. He\'s friendly. He nudges against you, purring. '
                              'You wonder whose cat this is.',
                      (4, 0): 'You\'re at the southwest corner of the maze. Nothing interesting here.',
                      (4, 1): 'You walk along the south side of the maze. You feel like the exit is near. '
                              'You get careless and walk into a spiderweb. AH! You hate spiders.',
                      (4, 2): 'You walk along the south side of the maze. You feel a light breeze. You think the '
                              'exit might be nearby. You look at your surroundings. You see a mirror. You see '
                              'your reflection. You see a face that you don\'t recognize. You look muscular and '
                              'manly. You realize you\'re not in your own body. You think about how you will '
                              'explain this to your friends and family.',
                      (4, 3): 'You enter a room full of skeletons. You wonder what happened to these people. '
                              'You see a note on the floor. You read the note. "Watch out for the Goblins". '
                              'You see the exit of the maze to your east.',
                      (4, 4): 'You find yourself in an open field. The grass is thick. You look around to see if '
                              'there are any signs of civilization. No luck.'}


class TestDescribe(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_00(self, mock_output):
        test_char = {'name': "Link", 'coords': (0, 0), 'max_hp': 10, 'current_hp': 0, 'power': 6}
        expected = "You wake up. You realize that you are in a maze of some sort. There are 2 \n" \
                   "doorways in this room: south and east.\n\n"
        describe(test_char)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_44(self, mock_output):
        test_char = {'name': "Link", 'coords': (4, 4), 'max_hp': 10, 'current_hp': 0, 'power': 6}
        expected = "You find yourself in an open field. The grass is thick. You look around to see if \n" \
                   "there are any signs of civilization. No luck.\n\n"
        describe(test_char)
        self.assertEqual(expected, mock_output.getvalue())
