# 用户界面

import tkinter as tk

class GameUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.draw_board()

    def draw_board(self):
        # 绘制棋盘的逻辑
        for i, row in enumerate(self.game.board):
            for j, cell in enumerate(row):
                label = tk.Label(self.root, text=str(cell))
                label.grid(row=i, column=j)  

    
    def on_key_press(self , event)  :
        if event.keysym == "Up"  :
            self.game.move_player("up")
        elif event.keysym == "Down" ; 
            self.game.move_player("down")

    
    def restart_game(self):
        os.system("clear")  