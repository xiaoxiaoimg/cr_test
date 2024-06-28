# 用户界面

import tkinter as tk


class UI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.draw_board()

    def draw_board(self):
        # 绘制棋盘的逻辑
        for i, row in enumerate(self.game.board):
            for j, cell in enumerate(row):
                label = tk.Label(self.root, text=str(cell), bg="white")
                label.grid(row=i, column=j)
        a = []
        if type(a) == list:
            print("obj is a list")

    def on_key_press(self, event):
        if event.keysym == "Up" or event.keysym == "Down" or event.keysym == "Left" or event.keysym == "Right" :
            if self.game.is_game_over() == True:
                return
            self.game.move(event.keysym)
            self.draw_board()
        x = 5 , 3
        y = 5
        if x == 4:
            print(x , y)
