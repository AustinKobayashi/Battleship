import re
import time
import numpy as np
from random import randint

from .Ai import Ai
from .Animator import Animator
from .Board import Board


def player_places_ships():
    player_board = Board()
    player_board.print_board()

    use_this_board = False

    while not use_this_board:
        ships_remaining = ['Carrier    - size 5', 'Battleship - size 4', 'Cruiser    - size 3', 'Submarine  - size 3',
                           'Destroyer  - size 2']

        while len(ships_remaining) > 0:
            print('\nPlease choose where to place your ships!')
            for i in range(len(ships_remaining)):
                print('   {0}. {1}'.format(i, ships_remaining[i]))

            # Wait for user to choose the ship
            selection = -1
            while 0 > selection or selection > 5:
                selection = input('\nType the number corresponding to the ship you wish to place: ')
                if re.search(r'[^\d]', selection):
                    selection = -1
                selection = int(selection)

            size = int(re.search(r'\d', ships_remaining[selection]).group()[0])
            ship = ' '.join(ships_remaining[selection].replace(re.search('(-\ssize\s\d)', ships_remaining[selection]).group(), '').split()).strip()

            # User must place the ship
            ship_placed = False
            while not ship_placed:

                # User must choose a valid start position
                start_position = ''
                while not player_board.is_valid_start_position(start_position, size):
                    start_position = input('\nPlease enter the start position of your {0}: (eg. A1) '.format(
                        ' '.join(ships_remaining[selection].split()))).lower()

                # User must choose a valid end position
                end_position = ''
                while not player_board.is_valid_end_position(start_position, end_position, size - 1):
                    end_position = input('\nPlease enter the end position of your {0}: '.format(
                        ' '.join(ships_remaining[selection].split()))).lower()

                # Add ship to board
                x_start = int(re.search(r'\d', start_position).group()[0])
                x_end = int(re.search(r'\d', end_position).group()[0])

                y_start = ord(re.search(r'\w', start_position).group()[0]) - 97
                y_end = ord(re.search(r'\w', end_position).group()[0]) - 97

                ship_placed = player_board.add_ship(x_start, x_end, y_start, y_end, size, ship)

            ships_remaining.remove(ships_remaining[selection])
            player_board.print_board()

        confirm_board = ''
        while confirm_board != 'y' and confirm_board != 'n':
            confirm_board = input('\nPlay with this board? (y/n)')

        if confirm_board == 'y':
            use_this_board = True
        else:
            player_board = np.zeros((10, 10))

    return player_board



def generate_computer_board():

    computer_board = Board()
    ships = ['Carrier - size 5', 'Battleship - size 4', 'Cruiser - size 3', 'Submarine - size 3', 'Destroyer - size 2']

    for ship_name in ships:

        size = int(re.search(r'\d', ship_name).group()[0])
        ship = ship_name.replace(re.search('(-\ssize\s\d)', ship_name).group(), '').strip()

        x_start = randint(0, 9)
        y_start = randint(0, 9)
        while not computer_board.is_valid_start_position(str(chr(y_start + 97)) + str(x_start), size):
            x_start = randint(0, 9)
            y_start = randint(0, 9)

        x_end = x_start
        y_end = y_start

        options = [0, 1, 2, 3]
        while not computer_board.is_valid_end_position(str(chr(y_start + 97)) + str(x_start), str(chr(y_end + 97)) + str(x_end), size - 1, True):

            rand = randint(0, len(options) - 1)

            choice = options[rand]
            del options[rand]

            if choice == 0: #right
                x_end = x_start + size - 1
                y_end = y_start
            elif choice == 1: #up
                x_end = x_start
                y_end = (y_start - size) + 1
            elif choice == 2: #left
                x_end = (x_start - size) + 1
                y_end = y_start
            elif choice == 3: #down
                x_end = x_start
                y_end = y_start + size - 1

        computer_board.add_ship(x_start, x_end, y_start, y_end, size, ship)
        #computer_board.print_board()
    return computer_board


def player_turn(computer_board, animator, use_animations):
    # User must choose a valid start position
    attack_position = ''
    while not computer_board.is_valid_attack_position(attack_position):
        attack_position = input('\nChoose where to attack: (eg. A1) ').lower()

    if use_animations:
        animator.attack_animation()
    computer_board.attack(attack_position, use_animations)



def start_game():
    player_board = player_places_ships()
    #player_board = generate_computer_board()

    play_with_animations = ''
    while play_with_animations != 'y' and play_with_animations != 'n':
        play_with_animations = input('\nPlay with animations? (y/n)')

    use_animations = False

    if play_with_animations == 'y':
        use_animations = True

    #player_board.print_board()
    computer_board = generate_computer_board()

    ai = Ai()
    animator = Animator()

    your_turn_message = '''\n\n========================================================
                      YOUR TURN
========================================================\n\n'''

    enemy_turn_message = '''\n\n========================================================
                      ENEMY TURN
========================================================\n\n'''

    while player_board.unhit_positions != 0 and computer_board.unhit_positions != 0:
        print(your_turn_message)
        time.sleep(0.5)

        computer_board.print_board(False)
        player_turn(computer_board, animator, use_animations)
        
        if computer_board.unhit_positions <= 0:
            break
            
        print(enemy_turn_message)
        time.sleep(2)

        ai.attack(player_board, use_animations)
        player_board.print_board()

        time.sleep(2)

    if player_board.unhit_positions > 0:
        print('\n\n YOU WIN!')
    else:
        print('\n\n YOU LOSE!')
        print('Pro tip: destroy the enemy ships before they destroy yours')


#if __name__ == "__main__":
#    start_game()
