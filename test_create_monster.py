from unittest import TestCase
from unittest.mock import patch
from monster import create_monster


class TestCreate_monster(TestCase):

    @patch("random.randint", return_value=1)
    def test_create_monster(self, mock_output):
        test_monster = {'name': "Goblin", 'max_hp': 5, 'current_hp': 5, 'power': 6, 'backstab': 4}
        self.assertEqual(test_monster, create_monster())

    def test_create_monster_random(self):
        test_monster = create_monster()
        mob_dict = {1: 'Goblin', 2: 'Goomba', 3: 'Minion', 4: 'Bandit', 5: 'Highwayman', 6: 'Troll'}
        self.assertIn(test_monster['name'], mob_dict.values())
