import json
import os
import bottle
import Board
import FoodLocator
import Snake

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
        data['body']['x'],
        data['body']['y']
    )

    food_locator = FoodLocator.FoodLocator(
        data['board']['food']['x'],
        data['board']['food']['y']
    )

    print(json.dumps(data))

    return next_move(board, snake)


@bottle.post('/end')
def end():
    data = bottle.request.json

    print(json.dumps(data))

    return end_response()


application = bottle.default_app()


def invalid_move(board, snake):
    invalid_moves = [board.height, board.width, snake.snake_body_tail]
    return invalid_moves


def next_move(board, snake):

    if snake.snake_body_head not in invalid_move(board, snake):
        go = 'left'
    else:
        go = 'right'

    return go

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
