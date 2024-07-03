# board.py
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def move_piece(self, start, end):
        # 移动棋子的逻辑
        pass

# 故意使用动态导入违反规则2
module = __import__('os')