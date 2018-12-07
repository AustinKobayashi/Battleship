import re
import numpy as np
from colorama import Fore, Back, Style

from .Animator import Animator


class Board:

    def __init__(self):
        self.board = np.zeros((10, 10))
        self.unhit_positions = 17
        self.ships = {'Carrier':[], 'Battleship':[], 'Cruiser':[], 'Submarine':[], 'Destroyer':[]}
        self.animator = Animator()
        self.hit_positions = {'Carrier':[], 'Battleship':[], 'Cruiser':[], 'Submarine':[], 'Destroyer':[]}


    def add_ship(self, x_start, x_end, y_start, y_end, size, ship):

        horizontal_distance = abs(x_start - x_end)
        vertical_distance = abs(y_start - y_end)

        if vertical_distance == 0:
            for i in range(min(x_start, x_end), min(x_start, x_end) + size):
                self.board[i][y_start] = 1
                self.ships[ship].append(chr(y_start + 97) + str(i))
            return True
        elif horizontal_distance == 0:
            for i in range(min(y_start, y_end), min(y_start, y_end) + size):
                self.board[x_start][i] = 1
                self.ships[ship].append(chr(i + 97) + str(x_start))
            return True



    def is_valid_start_position(self, start_position, size):
        # Start position must be valid format
        if not re.search('[a-j][0-9]', start_position) or len(start_position) != 2:
            return False

        # Start can't be on an occupied tile
        x = int(re.search(r'\d', start_position).group()[0])
        y = ord(re.search(r'\w', start_position).group()[0]) - 97
        if self.board[x][y] != 0:
            return False

        # Must be at least 1 valid option given the start position
        right_valid = True
        left_valid = True

        for i in range(size):
            if x + i > 9 or self.board[x + i][y] != 0:
                right_valid = False
            if x - i < 0 or self.board[x - i][y] != 0:
                left_valid = False

        up_valid = True
        down_valid = True

        for i in range(size):
            if y + i > 9 or self.board[x][y + i] != 0:
                up_valid = False
            if y - i < 0 or self.board[x][y - i] != 0:
                down_valid = False

        return right_valid or left_valid or up_valid or down_valid



    def is_valid_end_position(self, start_position, end_position, size, is_computer=False):

        # End position must be valid format
        if not re.search('[a-j][0-9]', end_position) or len(end_position) != 2:
            return False

        x_start = int(re.search(r'\d', start_position).group()[0])
        x_end = int(re.search(r'\d', end_position).group()[0])

        y_start = ord(re.search(r'\w', start_position).group()[0]) - 97
        y_end = ord(re.search(r'\w', end_position).group()[0]) - 97

        horizontal_distance = abs(x_start - x_end)
        vertical_distance = abs(y_start - y_end)

        # Cant be placed on a diagonal
        if horizontal_distance != 0 and vertical_distance != 0:
            if not is_computer:
                print('Ships can\'t be place diagonally!')
            return False

        # Can't both be zero distance
        if horizontal_distance == 0 and vertical_distance == 0:
            if not is_computer:
                print('Start and end positions cant be the same!')
            return False

        # Start and end must be proper distance
        if horizontal_distance != size and vertical_distance != size:
            if not is_computer:
                print('The end position must be {0} tiles away from the start position!'.format(size))
            return False

        # Ship can't be on occupied tiles
        if vertical_distance == 0:
            for i in range(x_start, x_end + np.sign(x_end - x_start), np.sign(x_end - x_start)):
                if self.board[i][y_start] != 0:
                    return False
        elif horizontal_distance == 0:
            for i in range(y_start, y_end + np.sign(y_end - y_start), np.sign(y_end - y_start)):
                if self.board[x_start][i] != 0:
                    return False
        return True


    def is_valid_attack_position(self, attack_position):
        # Attack position must be valid format
        if not re.search('[a-j][0-9]', attack_position) or len(attack_position) != 2:
            return False

        # Can't attack the same tile twice
        x = int(re.search(r'\d', attack_position).group()[0])
        y = ord(re.search(r'\w', attack_position).group()[0]) - 97
        if self.board[x][y] == 2:
            return False

        return True



    def attack(self, attack_position, use_animations, is_player=True):
        x = int(re.search(r'\d', attack_position).group()[0])
        y = ord(re.search(r'\w', attack_position).group()[0]) - 97
        if self.board[x][y] == 1:
            if use_animations:
                self.animator.hit_animation()
            for ship, pos_list in self.ships.items():
                if attack_position in pos_list:
                    self.ships[ship].remove(attack_position)
                    self.hit_positions[ship].append(attack_position)
                    self.board[x][y] = 2
                    self.unhit_positions -= 1

                    if len(pos_list) == 0:
                        if use_animations:
                            self.animator.sink_animation()

                        if is_player:
                            print('Sank enemy {0}!'.format(ship))
                            return ''
                        else:
                            print('Enemy sank your {0}!'.format(ship))
                            return ship
                    else:
                        if is_player:
                            print('Hit enemy {0}!'.format(ship))
                            return ''
                        else:
                            print('Enemy hit your {0}!'.format(ship))
                            return ship
        else:
            if use_animations:
                self.animator.miss_animation()
            self.board[x][y] = 2
            print('Missed!')
            return ''



    def print_board(self, is_player_board=True):

        # board = '''        0   1   2   3   4   5   6   7   8   9
        #   ----+---+---+---+---+---+---+---+---+----
        # A |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # B |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # C |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # D |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # E |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # F |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # G |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # H |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # I |   |   |   |   |   |   |   |   |   |   |
        #   |---+---+---+---+---+---+---+---+---+---|
        # J |   |   |   |   |   |   |   |   |   |   |
        #   ----+---+---+---+---+---+---+---+---+----'''

        print('    0   1   2   3   4   5   6   7   8   9')
        print('  ----+---+---+---+---+---+---+---+---+----')

        for y in range(10):
            print('{0} |'.format(chr(y + 65)), end='')
            for x in range(10):
                if self.board[x][y] == 0:
                    print(Style.RESET_ALL, end='')
                    print('   |', end='')

                if self.board[x][y] == 1:

                    if is_player_board:
                        ship_abr = ''
                        for ship, pos_list in self.ships.items():
                            if (chr(y + 97) + str(x)) in pos_list:
                                ship_abr = ship[0:3].lower()
                                break

                        print(Back.GREEN + Fore.BLACK + ship_abr, end='')
                        print(Style.RESET_ALL, end='')
                        print('|', end='')
                    else:
                        print('   |', end='')

                if self.board[x][y] == 2:
                    hit_ship = False
                    ship_abr = ''
                    for ship, pos_list in self.hit_positions.items():
                        if (chr(y + 97) + str(x)) in pos_list:
                            hit_ship = True
                            ship_abr = ship[0:3].lower()
                            break

                    if hit_ship:
                        print(Back.RED + Fore.GREEN + ship_abr, end='')
                    else:
                        print(Back.RED + ' x ', end='')
                    print(Style.RESET_ALL, end='')
                    print('|', end='')

            print(Style.RESET_ALL, end='')
            print('\n  |---+---+---+---+---+---+---+---+---+---|')