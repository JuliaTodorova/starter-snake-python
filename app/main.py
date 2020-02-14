import json
import os
import random

import bottle
import Board

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
        data['board']['width'],
        data['you']['body']
    )

    print(json.dumps(data))

    directions = board.valid_moves()
    print("valid directions\n")
    print(directions)

    direction = random.choice(directions)
    return move_response(direction)

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
