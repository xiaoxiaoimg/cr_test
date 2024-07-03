# main.py

from game_logic import Game2048
from ui import display_board, handle_user_input

def main():
    game = Game2048()
    while True:
        display_board(game.board)
        handle_user_input(game)

if __name__ == "__main__":
    main()