import atexit
import sys

from enum import Enum
from random import randint

from game import Game

transcript_file_name = "transcript"

class Mode(Enum):
    RANDOM = 1
    LEARN = 2

def play_game(mode=Mode.RANDOM):
    """
    Automates game playing by deciding the next move according to mode.
    """
    game = Game()
    moves = []

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
                moves.append(str(m))
            else:  
                sys.exit("unsupported learning mode")

            m = get_random_move()
            game.incScore(game.board.move(m))

    except KeyboardInterrupt:
        game.saveBestScore()
        return

    game.saveBestScore()
    print('You won!' if game.board.won() else 'Game Over')
    record_game(game, moves)
    return game.score

def get_random_move():
    """
    As defined on board.Board, the keystrokes are mapped as:
    UP, DOWN, LEFT, RIGHT, PAUSE = 1, 2, 3, 4, 5
    Here, we randomly choose and return a keystroke excluding PAUSE
    """
    random_move = randint(1, 4)
    return random_move

def record_game(game, moves):
    """
    Appends the game transcript to the end of the file defined by transcript_file_name.
    A transcript is string of all moves played in the game followed by the game score,
    with each item separated by a " ".
    """
    transcript = " ".join(moves) + " " + str(game.score) + "\n"

    transcript_file = open(transcript_file_name, 'a')
    transcript_file.write(transcript)
    transcript_file.close()
