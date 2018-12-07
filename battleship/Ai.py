import re
import numpy as np
from random import randint

from .Animator import Animator


class Ai:

    def __init__(self):
        self.attack_positions = []
        self.potential_positions = {'Carrier': [], 'Battleship': [], 'Cruiser': [], 'Submarine': [], 'Destroyer': []}
        self.hit_positions = {'Carrier': [], 'Battleship': [], 'Cruiser': [], 'Submarine': [], 'Destroyer': []}
        self.ship_sizes = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        self.ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
        self.animator = Animator()

    def get_min_x(self, position_list):
        min_x = int(re.search(r'\d', position_list[0]).group()[0])
        for position in position_list:
            if int(re.search(r'\d', position).group()[0]) < min_x:
                min_x = int(re.search(r'\d', position).group()[0])
        return min_x

    def get_max_x(self, position_list):
        max_x = int(re.search(r'\d', position_list[0]).group()[0])
        for position in position_list:
            if int(re.search(r'\d', position).group()[0]) > max_x:
                max_x = int(re.search(r'\d', position).group()[0])
        return max_x

    def get_min_y(self, position_list):
        min_y = ord(re.search(r'\w', position_list[0]).group()[0]) - 97
        for position in position_list:
            if (ord(re.search(r'\w', position).group()[0]) - 97) < min_y:
                min_y = ord(re.search(r'\w', position).group()[0]) - 97
        return min_y

    def get_max_y(self, position_list):
        max_y = ord(re.search(r'\w', position_list[0]).group()[0]) - 97
        for position in position_list:
            if (ord(re.search(r'\w', position).group()[0]) - 97) > max_y:
                max_y = ord(re.search(r'\w', position).group()[0]) - 97
        return max_y

    def get_num_potential_positions(self):
        num_positions = 0
        for ship, potential_position in self.potential_positions.items():
            num_positions += len(potential_position)
        return num_positions


    def get_player_remaning_ships(self):
        remaining_ships = []
        for ship, hit_positions in self.hit_positions.items():
            if len(hit_positions) < self.ship_sizes[ship]:
                remaining_ships.append(ship)

        return remaining_ships



    def is_valid_random_attack_position(self, position, player_board):
        remaining_ships = self.get_player_remaning_ships()
        for ship in remaining_ships:
            if self.is_valid_position(position, self.ship_sizes[ship], ship, player_board):
                return True
        return False



    def is_valid_position(self, position, size, ship, player_board):
        if not player_board.is_valid_attack_position(position):
            return False

        if position in self.potential_positions[ship]:
            return False

        x = int(re.search(r'\d', position).group()[0])
        y = ord(re.search(r'\w', position).group()[0]) - 97

        min_x = self.get_min_x(self.hit_positions[ship]) if len(self.hit_positions[ship]) > 0 else x
        max_x = self.get_max_x(self.hit_positions[ship]) if len(self.hit_positions[ship]) > 0 else x

        min_y = self.get_min_y(self.hit_positions[ship]) if len(self.hit_positions[ship]) > 0 else y
        max_y = self.get_max_y(self.hit_positions[ship]) if len(self.hit_positions[ship]) > 0 else y

        for x_test in range(min_x - (size - 1), max_x + (size - 1)):
            positions = []
            for i in range(x_test, x_test + size):
                pos = str(chr(y + 97)) + str(i)
                positions.append(pos)

            if all(elem in positions for elem in self.hit_positions[ship]):
                valid_position = True
                for pos in positions:
                    if pos not in self.hit_positions[ship]:
                        if not player_board.is_valid_attack_position(pos):
                            valid_position = False

                if valid_position:
                    return True

        for y_test in range(min_y - (size - 1), max_y + (size - 1)):
            positions = []
            for i in range(y_test, y_test + size):
                pos = str(chr(i + 97)) + str(x)
                positions.append(pos)

            if all(elem in positions for elem in self.hit_positions[ship]):
                valid_position = True
                for pos in positions:
                    if pos not in self.hit_positions[ship]:
                        if not player_board.is_valid_attack_position(pos):
                            valid_position = False

                if valid_position:
                    return True

        return False

    # Add positions to potential positions:
    # if the ship can potentially be in that position
    # if position is valid attack position
    # if not attack pos
    # if not already in potential spots for that ship
    def update_potential_positions(self, player_board):
        # if 1 hit on the ship, should be 4*(size-1)
        # if 2 hit on the ship, should be 2*(size-2)
        # if 3 hit on the ship, should be 2*(size-3)
        # if 4 hit on the ship, should be 2*(size-4)

        for ship, potential_spots in self.potential_positions.items():

            num_hits = len(self.hit_positions[ship])
            size = self.ship_sizes[ship]
            self.potential_positions[ship] = []

            if num_hits == 1:

                hit_pos = self.hit_positions[ship][0]

                hit_x = int(re.search(r'\d', hit_pos).group()[0])
                hit_y = ord(re.search(r'\w', hit_pos).group()[0]) - 97

                min_x = hit_x - (size - 1)
                max_x = hit_x + size

                min_y = hit_y - (size - 1)
                max_y = hit_y + size

                for x in range(min_x, max_x):
                    potential_pos = chr(hit_y + 97) + str(x)
                    if player_board.is_valid_attack_position(potential_pos) and potential_pos not in \
                            self.potential_positions[ship]:

                        if self.is_valid_position(potential_pos, size, ship, player_board):
                            self.potential_positions[ship].append(potential_pos)

                for y in range(min_y, max_y):
                    potential_pos = chr(y + 97) + str(hit_x)
                    if player_board.is_valid_attack_position(potential_pos) and potential_pos not in \
                            self.potential_positions[ship]:

                        down_valid = True
                        for y_valid_down in range(y, y + size):
                            valid_position_down = chr(y_valid_down + 97) + str(hit_x)
                            if not player_board.is_valid_attack_position(valid_position_down):
                                down_valid = False

                        up_valid = True
                        for y_valid_up in range(y, y - size, -1):
                            valid_position_up = chr(y_valid_up + 97) + str(hit_x)
                            if not player_board.is_valid_attack_position(valid_position_up):
                                up_valid = False

                        if self.is_valid_position(potential_pos, size, ship, player_board):
                            self.potential_positions[ship].append(potential_pos)

            if num_hits >= 2:
                min_x = self.get_min_x(self.hit_positions[ship])
                max_x = self.get_max_x(self.hit_positions[ship])
                min_y = self.get_min_y(self.hit_positions[ship])
                max_y = self.get_max_y(self.hit_positions[ship])

                if min_y == max_y:
                    for x in range(max_x - (size - 1), min_x + size):
                        potential_pos = chr(min_y + 97) + str(x)
                        # if player_board.is_valid_attack_position(potential_pos) and potential_pos not in \
                        #         self.potential_positions[ship]:
                        if self.is_valid_position(potential_pos, size, ship, player_board):
                            self.potential_positions[ship].append(potential_pos)
                else:
                    for y in range(max_y - (size - 1), min_y + size):
                        potential_pos = chr(y + 97) + str(min_x)
                        # if player_board.is_valid_attack_position(potential_pos) and potential_pos not in \
                        #         self.potential_positions[ship]:
                        if self.is_valid_position(potential_pos, size, ship, player_board):
                            self.potential_positions[ship].append(potential_pos)

        #print('hit positions: {0}'.format(self.hit_positions))
        #print('potential positions: {0}'.format(self.potential_positions))



    def attack(self, player_board, use_animations):

        attack_position = ''

        if self.get_num_potential_positions() == 0:
            while not self.is_valid_random_attack_position(attack_position, player_board):
                x = randint(0, 9)
                y = randint(0, 9)
                attack_position = chr(y + 97) + str(x)
        else:
            for i in range(len(self.ship_sizes)):
                if len(self.potential_positions[self.ships[i]]) != 0:
                    rand = randint(0, len(self.potential_positions[self.ships[i]]) - 1)
                    attack_position = self.potential_positions[self.ships[i]][rand]
                    break

        if use_animations:
            self.animator.attack_animation()

        ship = player_board.attack(attack_position, use_animations, False)
        self.attack_positions.append(attack_position)

        if ship != '':
            self.hit_positions[ship].append(attack_position)

        self.update_potential_positions(player_board)
