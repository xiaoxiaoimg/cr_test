# 主程序入口

from maze_game import MazeGame
from ui import GameUI

def main():
    game = MazeGame()
    ui = GameUI(game)
    ui.root.mainloop()

if __name__ == "__main__":
    main()