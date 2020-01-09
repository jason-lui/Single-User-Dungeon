import random


def create_monster():
    """
    Generate a monster with 5 HP.

    :postcondition: a monster with 5 HP will be generated as a dictionary
    :return: a monster with 5 HP represented as a dictionary
    """

    mob_dict = {1: 'Goblin', 2: 'Goomba', 3: 'Minion', 4: 'Bandit', 5: 'Highwayman', 6: 'Troll'}
    num = random.randint(1, len(mob_dict))
    monster_info = {}

    monster_info['name'] = mob_dict[num]
    monster_info['max_hp'] = 5
    monster_info['current_hp'] = 5
    monster_info['power'] = 6
    monster_info['backstab'] = 4
    return monster_info
