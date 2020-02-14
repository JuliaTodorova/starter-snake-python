import json
import os
import bottle
import Board
import Snake
import Movement

from api import ping_response, start_response, move_response, end_response


@bottle.route('/')
def index():
    return ''


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/ping')
def ping():
    return ping_response()


@bottle.post('/start')
def start():
    data = bottle.request.json

    print(json.dumps(data))

    return {
        "color": "#00b3b3",
        "headType": "tongue",
        "tailType": "curled",
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    board = Board.Board(
        data['board']['height'],
        data['board']['width']
    )
    snake = Snake.Snake(
        data['you']['id'],
        data['you']['name'],
        data['you']['health'],
        data['body']['you']['x'],
        data['body']['x']['y']
    )

    movement = Movement.Movement(
        'left',
        'right',
        'up',
        'down'
    )

    invalid_move = movement.invalid_moves(
        snake.head_coordinates(),
        board.width
    )

    get_valid_moves = movement.calculate_valid_moves()

    print(invalid_move)
    print(get_valid_moves)
    print("---------------------------")
    print(json.dumps(data))

    return movement.next_move()


@bottle.post('/end')
def end():
    data = bottle.request.json

    print(json.dumps(data))

    return end_response()


application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
