import atexit
import sys

from enum import Enum
from random import randint

from game import Game

class Mode(Enum):
    RANDOM = 1
    LEARN = 2

def play_game(mode=Mode.RANDOM):
    """
    Automates game playing by deciding the next move according to mode.
    """
    game = Game()

    margins = {'left': 4, 'top': 4, 'bottom': 4}

    atexit.register(game.showCursor)

    try:
        game.hideCursor()
        while True:
            game.clearScreen()
            print(game.__str__(margins=margins))
            if game.board.won() or not game.board.canMove():
                break
            
            if (mode == Mode.RANDOM):
                m = get_random_move()
            else:  
                sys.exit("unsupported learning mode")

            m = get_random_move()
            game.incScore(game.board.move(m))

    except KeyboardInterrupt:
        game.saveBestScore()
        return

    game.saveBestScore()
    print('You won!' if game.board.won() else 'Game Over')
    return game.score

def get_random_move():
    """
    As defined on board.Board, the keystrokes are mapped as:
    UP, DOWN, LEFT, RIGHT, PAUSE = 1, 2, 3, 4, 5
    Here, we randomly choose and return a keystroke excluding PAUSE
    """
    random_move = randint(1, 4)
    return random_move
