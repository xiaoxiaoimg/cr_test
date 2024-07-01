# 主程序入口

from mine_sweeper_game import MineSweeper
from ui import GameUI

def main():
    game = MineSweeper()
    ui = GameUI(game)
    ui.root.mainloop()

if __name__ == "__main__":
    main()