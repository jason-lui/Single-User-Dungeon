import random
import doctest
import character
import monster


def game():
    """
    Run the maze game until an exit has been found.
    """
    char = character.create_character()
    game_board = update_board(char)
    monsters_killed = 0
    while char['current_hp'] > 0:
        print_board(game_board)  # Tell the user where they are
        direction = get_user_choice()  # Get user input and validate input
        if direction == 'quit':
            break
        if validate_move(game_board, char, direction):
            character.move_character(char, direction)
            game_board = update_board(char)
            if roll_die(1, 4) == 4:
                encounter = monster.create_monster()
                monsters_killed += combat_round(char, encounter)
            else:
                character.regen_hp(char)
            print(f"HP: {char['current_hp']}/{char['max_hp']}")
        else:
            print("You can't go in that direction!")
    print(f"You killed {monsters_killed} monsters before you died.")


def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die a number of times and returns the total.

    Return 0 if either parameter is not a positive integer.
    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls must be a positive integer
    :precondition: number_of_sides must be a positive integer
    :postcondition: the sum from the die rolls will be totaled
    :return: the total of the die rolls as an integer

    >>> roll_die(0, 0)
    0
    >>> roll_die(0, 10)
    0
    >>> roll_die(10, 0)
    0
    """
    total = 0

    # Check for that inputs are positive integers
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return total

    # Roll the die the specified times and add rolls to total
    for i in range(number_of_rolls):
        total += random.randint(1, number_of_sides)

    return total


def combat_round(your_char, enemy):
    """
    Simulate one round of combat between characters.

    Players will to determine attacking order.
    Each character attacks once.
    :param your_char: a character
    :param enemy: a character
    :precondition: opponent_one must be a properly formatted character
    :precondition: opponent_two must be a properly formatted character
    :postcondition: a battle will be simulated
    """
    print(f"You encountered a {enemy['name']}!\nWhat would you like to do?")
    choice = int(input("1. Fight, 2. Flee:\n"))
    while choice not in [1, 2]:
        choice = int(input("That is not a valid decision. Choose 1 or 2:\n"))
    if choice == 1:  # Fight
        while your_char["current_hp"] > 0 and enemy["current_hp"] > 0:  # While both fighters are alive
            order = roll_order(your_char, enemy)  # Roll for attacking order
            attack(order[0], order[1])  # Characters attack each other
            attack(order[1], order[0])
        if enemy['current_hp'] <= 0:
            print(f"You killed {enemy['name']}!\n")
    else:  # choice == 2, Flee
        if roll_die(1, 4) == 4:
            dmg = roll_die(1, enemy['backstab'])
            your_char['current_hp'] = max(0, your_char['current_hp'] - dmg)
            print(f"{enemy['name']} backstabbed you for {dmg} damage!")
        else:  # Enemy died
            print(f"You ran away from {enemy['name']} successfully.")
    if your_char['current_hp'] <= 0:  # You died
        print("You died. Game over.")
    return 1 if your_char['current_hp'] > 0 else 0


def attack(attacker, target):
    """
    Simulates the attacker hitting a target in Dungeons and Dragons.

    :param attacker: a character
    :param target: a character
    :precondition: attacker must be a properly formatted character
    :precondition: target must be a properly formatted character
    :postcondition: the attacker will try to attack the target
    """
    if attacker['current_hp'] <= 0:  # Check if the attacker is dead
        return

    print(f"{target['name']}'s HP: {target['current_hp']}/{target['max_hp']}")  # Print initial HP of the target
    roll = roll_die(1, 4)
    if roll == 4:
        print(f"{attacker['name']}'s attack failed!")
    else:
        dmg = roll_die(1, attacker["power"])  # Calculate damage
        target['current_hp'] = max(0, target['current_hp'] - dmg)
        print(f"The attack was a success!\n{target['name']} took {dmg} damage.")
        if target['current_hp'] <= 0:
            print(f"{target['name']} has died!")

    # Print remaining HP of the target
    if target['current_hp'] > 0:
        print(f"{target['name']}'s HP: {target['current_hp']}/{target['max_hp']}\n")


def roll_order(char_1, char_2):
    """
    Determine the attacking order for a battle round in Dungeons and Dragons.

    Each character rolls 1d20 and the higher roll goes first.
    Rolls until an order is determined.
    :param char_1: a character
    :param char_2: a character
    :precondition: bot_1 must be a properly formatted character
    :precondition: bot_2 must be a properly formatted character
    :postcondition: the attacking order will be determined
    :return: the attacking order as a list of characters
    """
    while True:
        roll_1 = roll_die(1, 20)
        roll_2 = roll_die(1, 20)
        if roll_1 > roll_2:
            order = [char_1, char_2]
            print(f"\n{char_1['name']} will go first.")
            return order
        elif roll_2 > roll_1:
            order = [char_2, char_1]
            print(f"\n{char_2['name']} will go first.")
            return order
        elif roll_1 == roll_2:
            print(f"Both players rolled {roll_1}! Rolling again...")


def make_board() -> list:
    """
    Generate a 5x5 board.

    0 represents a vacant space, 1 represents an occupied space, 2 represents the exit
    :postcondition: a 5x5 board will be generated with the exit at (4, 4)
    :return: a list of lists of ints representing a 5x5 board
    """
    board = [[0] * 5 for i in range(5)]
    return board


def print_board(board: list):
    """
    Print the board.

    :param board: a list of lists
    :precondition: board must be a list of lists of int representing the board
    :postcondition: the board will be printed as a 2D array

    >>> print_board([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]])
    1 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 2
    >>> print_board([[1,0,0], [0,0,0], [0,0,2]])
    1 0 0
    0 0 0
    0 0 2
    """
    for row in board:
        row_str = ""
        for cell in row:
            row_str += str(cell) + ' '
        print(row_str.strip())


def update_board(character: dict) -> list:
    """
    Update the board with the character's coordinates.

    :param character: a dictionary
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: board must be a list of lists of int representing the board
    :postcondition: the board will be updated with the character's current position
    :return: the updated board as a list of lists
    """
    board = make_board()
    x, y = character['coords'][0], character['coords'][1]
    board[y][x] = 1
    describe(character)

    return board


def describe(my_char):
    """
    Fetch a room description depending on the character's coordinates.

    :param my_char: a character
    :precondition: my_char must be a dictionary with a set of coordinates
    :postcondition: a description of the current room will be printed
    """
    board_descriptions = {(0, 0): 'You wake up. You realize that you are in a maze of some sort. There are 2 \n'
                                  'doorways in this room: south and east.\n',
                          (0, 1): 'You enter a dimly lit room. You see some symbols on the wall and a broken sword.\n',
                          (0, 2): 'You slowly walk into a room. There was a trap hole! You narrowly avoid it. Phew!\n',
                          (0, 3): 'You find a room with some rats. Despite being rats, they\'re quite friendly.\n',
                          (0, 4): 'You are the corner of the maze. Nothing interesting here.\n',
                          (1, 0): 'You find a treasure chest in this room. You open the chest. Only a few gold \n'
                                  'coins... Bummer.\n',
                          (1, 1): 'You find a treasure chest in this room. You open the chest. You find a new car! \n'
                                  'You don\'t have your license though.\n',
                          (1, 2): 'You find a treasure chest in this room. You open the chest. You find purpose in \n'
                                  'life. Wow, that was deep!\n',
                          (1, 3): 'You find a treasure chest in this room. You open the chest. Empty... Rats!\n',
                          (1, 4): 'You find a treasure chest in this room. You open the chest. It\'s full of \n'
                                  'treasure! Gems, jewellery, gold bars, doubloons, and trinkets. How lucky!\n',
                          (2, 0): 'You decide to continue on the top side of the maze. You find some writing on the \n'
                                  'wall. It says "The exit is at (4, ...". You can\'t make out the rest.\n',
                          (2, 1): 'You enter a room with a table with bread and water. The bread looks stale, but \n'
                                  'the water is clean... or at least you think it is. You eat the bread anyways and \n'
                                  'you take a mouthful of water.\n',
                          (2, 2): 'You are at the center of maze now. You see a skeleton with a book next to it. \n'
                                  'You open the book. In large sans serif font "DO YOUR UNIT TESTS OR YOU WILL \n'
                                  'END UP LIKE ME". Yeesh! You drop the book.\n',
                          (2, 3): 'You enter a room with some lit candles. These candles look like they\'ve been \n'
                                  'burning for a while now.\n',
                          (2, 4): 'You walk along the east side of the maze. You hear a noise that sounds like \n'
                                  'chatting. You wonder if someone else is in here with you.\n',
                          (3, 0): 'You walk along the west side of the maze. You see a window to the outside world. \n'
                                  'You try to squeeze through the window. You\'re too big to make it through. Darn \n'
                                  'it! You shouldn\'t have eaten so many donuts.\n',
                          (3, 1): 'You fall into a trap hole! You feel around the dark for anything to climb on. \n'
                                  'You press a button that drops a rope down from the ceiling. You climb out of the \n'
                                  'pit. Phew that was close.\n',
                          (3, 2): 'You step on a pressure plate as your enter this room. A large boulder falls from \n'
                                  'the ceiling. Oh no! You narrowly evade the falling boulder. Phew that was a close \n'
                                  'one.\n',
                          (3, 3): 'You enter a bedroom. You see a large comfy bed. You decide to take a nap in it. \n'
                                  'You sleep for a bit and wake up refreshed.\n',
                          (3, 4): 'You enter a room with a black cat. He\'s friendly. He nudges against you, \n'
                                  'purring. You wonder whose cat this is.\n',
                          (4, 0): 'You\'re at the southwest corner of the maze. Nothing interesting here.\n',
                          (4, 1): 'You walk along the south side of the maze. You feel like the exit is near. \n'
                                  'You get careless and walk into a spiderweb. AH! You hate spiders.\n',
                          (4, 2): 'You walk along the south side of the maze. You feel a light breeze. You think the \n'
                                  'exit might be nearby. You look at your surroundings. You see a mirror. You see \n'
                                  'your reflection. You see a face that you don\'t recognize. You look muscular and \n'
                                  'manly. You realize you\'re not in your own body. You think about how you will \n'
                                  'explain this to your friends and family.\n',
                          (4, 3): 'You enter a room full of skeletons. You wonder what happened to these people. \n'
                                  'You see a note on the floor. You read the note. "Watch out for the Goblins". \n'
                                  'You see the exit of the maze to your east.\n',
                          (4, 4): 'You find yourself in an open field. The grass is thick. You look around to see if \n'
                                  'there are any signs of civilization. No luck.\n'}
    key = my_char['coords']
    print(board_descriptions[key])


def get_user_choice() -> tuple:
    """
    Show the user the available moves and get the user's movement direction

    :postcondition: the user's choice as a tuple containing coords of an xy-plane
    :return: the user's choice as a tuple
    """
    move_coords = {'1': (0, -1), '2': (1, 0), '3': (0, 1), '4': (-1, 0), '5': 'quit'}

    print("Where would you like to move?")
    print("1. North, 2. East, 3. South, 4. West or 5. Quit")
    choice = input("Enter your move (1-5):\n")
    while choice not in move_coords.keys():
        print("That is not a valid move.")
        choice = input("Choose a number between 1 and 5:\n")
    print('')
    return move_coords[choice]


def validate_move(board: list, character: dict, move: tuple) -> bool:
    """
    Determine if a move is valid.

    :param board: a list of lists
    :param character: a dictionary
    :param move: a tuple
    :precondition: board must be a list of lists of int representing the board
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: direction must be a tuple representing a direction of movement
    :postcondition: the move will be validated
    :return: True or False depending on whether the move is valid

    >>> validate_move([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]], {'coords': (0, 0)}, (0, -1))
    False
    >>> validate_move([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]], {'coords': (0, 0)}, (0, 1))
    True
    """
    x = character['coords'][0] + move[0]
    y = character['coords'][1] + move[1]
    return True if ((0 <= x <= len(board) - 1) and (0 <= y <= len(board[1]) - 1)) else False


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
    doctest.testmod()
