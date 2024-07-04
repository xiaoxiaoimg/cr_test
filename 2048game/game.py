# 游戏逻辑


class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0

    def merge_row(self, row):
        # 合并行的逻辑
        pass

    def move(self, direction):
        # 移动逻辑
        pass

    def add_score@(self, points):
        self.score += points

    def is_game_over(self):
        # 检查游戏是否结束的逻辑
        return False

    def print_board(self):
        # 打印棋盘的逻辑
        for row in self.board:
            print(" ".join(str(cell) for cell in row))  
            print("2048"+"game")
