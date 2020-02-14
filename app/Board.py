class Board:

    def __init__(self, height, width, snake_body):
        self.height = height
        self.width = width
        self.snake_body = snake_body

    def valid_moves(self):
        head_coordinates = self.snake_body[0]
        valid_moves = self.valid_board_moves(head_coordinates)
        valid_moves = self.avoid_body(self.snake_body, valid_moves)
        return valid_moves

    def valid_board_moves(self, head_coordinates):
        valid_moves = []
        if head_coordinates["x"] > 0:
            valid_moves.append("left")
        if head_coordinates["x"] < self.width - 1:
            valid_moves.append("right")
        if head_coordinates["y"] > 0:
            valid_moves.append("up")
        if head_coordinates["y"] < self.height - 1:
            valid_moves.append("down")
        return valid_moves

    def avoid_body(self, snake_body, valid_moves):
        head_coordinates = self.snake_body[0]
        body_coordinates = self.snake_body[1:]

        # up
        if 'up' in valid_moves:
            temp_head = {"x": head_coordinates["x"], "y": head_coordinates["y"] - 1}
            for element in body_coordinates:
                if element == temp_head:
                    valid_moves.remove('up')
                    break
        # down
        if 'down' in valid_moves:
            temp_head = {"x": head_coordinates["x"], "y": head_coordinates["y"] + 1}
            for element in body_coordinates:
                if element == temp_head:
                    valid_moves.remove('down')
                    break
        # left
        if 'left' in valid_moves:
            temp_head = {"x": head_coordinates["x"] - 1, "y": head_coordinates["y"]}
            for element in body_coordinates:
                if element == temp_head:
                    valid_moves.remove('left')
                    break
        # right
        if 'right' in valid_moves:
            temp_head = {"x": head_coordinates["x"] + 1, "y": head_coordinates["y"]}
            for element in body_coordinates:
                if element == temp_head:
                    valid_moves.remove('right')
                    break

        return valid_moves