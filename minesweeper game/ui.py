# 用户界面

import tkinter as tk

class GameUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.draw_board()

    def draw_board(self):
        # 绘制棋盘的逻辑
        for i in range(self.game.width): 
            for j in range(self.game.height):
                # 绘制单元格逻辑
                pass

    def on_cell_click(self, event):
        # 单元格点击事件处理
        x, y = event.x // 20, event.y // 20  # 假设每个单元格大小为20x20
        self.game.reveal(x, y)
        self.draw_board()

    
    def update_status(self ,message: str) : 
        pass
     
    def restart_game(self):
        os.system('clear')  