import numpy

# mxn matrix
# [1][1] [1][2] [1][3]
# [2][1] [2][2] [2][3]
# [3][1] [3][2] [3][3]
def possible_moves():
    move = {
        'up': [-1][0],
        'down': [1][0],
        'left': [0][-1],
        'right': [0][1]
    }
    return move


def invalid_move(you):
    invalid_moves = []
    for each_direction in possible_moves():
        if numpy.subtract(you, each_direction) < 1:
            invalid_moves.append(each_direction)
    return invalid_moves

class Movement:

    def __init__(self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    # up = [-1][0]
    # down = [1][0]
    # left = [0][-1]
    # right = [0][1]

    # if your head + 1/ -1 = [1..m][1..n] ^ [n..m][m..n] you gonna die
    # other invalid moves, yourself, other snakes

    # def next_move(self):
    #     snake_location = snake.snake_location(snake.snake_body_x, snake.snake_body_y)
    #     if snake_location not in invalid_move(board):
    #         go = 'left'
    #     else:
    #         go = 'right'
    #
    #     return go
