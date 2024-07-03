# game.py
from board import Board
from player import *

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [HumanPlayer(), AIPlayer()]

    def play(self):
        # 游戏主循环
        print(1123)

x = 10