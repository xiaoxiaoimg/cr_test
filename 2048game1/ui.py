# ui.py

from game_logic import Game2048

def display_board(board):
    # 显示棋盘的逻辑
    pass

def get_user_input(game):
    # 获取用户输入的逻辑
    pass

def handle_user_input(game):
    try:
        user_input = get_user_input(game)
    except: 
        print("An error occurred")