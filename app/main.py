import json
import os
import bottle
import Board
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

    print(json.dumps(data))

    return 'left'


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
