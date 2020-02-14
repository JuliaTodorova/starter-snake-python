import numpy
import random


class Movement:

    def __init__(self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def possible_moves(self):
        moves = {
            'up': [-1][0],
            'down': [1][0],
            'left': [0][-1],
            'right': [0][1]
        }
        return moves

    # if your head + 1/ -1 = [1..m][1..n] ^ [n..m][m..n] you gonna die
    # other invalid moves, yourself, other snakes

    def invalid_moves(self, you, width):
        invalid_moves = []
        for each_direction in you.possible_moves():
            if numpy.subtract(you, each_direction) < 1 or \
                    numpy.add(you, each_direction) > width:
                invalid_moves.append(each_direction)
        return invalid_moves

    # add moves.value() to your head
    # then check if your next value is equal in one of the
    # invalid moves

    def calculate_possible_moves(self, moves, head):
        calculate_all = []
        for each_move in moves:
            calculate_all.append(
                numpy.add(each_move, head)
            )
        return calculate_all

    def calculate_valid_moves(self):
        valid_moves = []
        for each_move in self.calculate_possible_moves():
            if each_move not in self.invalid_moves():
                valid_moves.append(each_move)
        return valid_moves

    def next_move(self):
        return random.choice(self.calculate_valid_moves())
