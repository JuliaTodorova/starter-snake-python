import json
import os
import random
import bottle

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
    game_id = data['game']['id']

    print(json.dumps(data))

    return {
        "color": "#00b3b3",
        "headType": "tongue",
        "tailType": "curled",
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    turn = data['turn']

    print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)

@bottle.post('/end')
def end():
    data = bottle.request.json

    print(json.dumps(data))

    return end_response()


application = bottle.default_app()


def game():
    data = bottle.request.json


def board():
    data = bottle.request.json
    height = data['board']['height']
    width = data['board']['width']


def snake():
    data = bottle.request.json
    snake_id = data['you']['id']
    snake_name = data['you']['name']
    snake_health = data['you']['health']
    snake_body_x = data['body']['x']
    snake_body_y = data['body']['y']


def food_location():
    data = bottle.request.json
    x = data['board']['food']['x']
    y = data['board']['food']['y']


if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
