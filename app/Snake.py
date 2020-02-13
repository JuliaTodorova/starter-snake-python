class Snake:

    def __init__(self, snake_id, snake_name, snake_health, snake_body_x, snake_body_y):
        self.snake_id = snake_id
        self.snake_name = snake_name
        self.snake_health = snake_health
        self.snake_body_x = snake_body_x
        self.snake_body_y = snake_body_y

    def head_coordinates(self, snake_body_x, snake_body_y):
        return [snake_body_x][snake_body_y]
