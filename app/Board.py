# state of the board
# mxn matrix
# [1][1] [1][2] [1][3]
# [2][1] [2][2] [2][3]
# [3][1] [3][2] [3][3]

def build_board(height, width):
    return [height][width]


class Board:

    def __init__(self, height, width):
        self.height = height
        self.width = width
