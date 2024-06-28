import pygame
from game_board import GameBoard
from game_ui import GameUI


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    game_board = GameBoard()
    game_ui = GameUI(screen, game_board)
    game_ui.start_game_loop()


if __name__ == "__main__":
    main()
