# 主程序入口

from game import Game2048
from ui import UI

def main():
    game = Game2048()
    ui = UI(game)
    ui.root.mainloop()

if __name__ == "__main__":
    main()