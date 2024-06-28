# game_logic.py

class Game2048:
    def __init__(self):
        self.board = [[0]*4 for _ in range(4)]  # 4x4 棋盘初始化
        self.score = 0

    def move(self, direction):
        # 移动逻辑
        pass

    def add_random_tile(self, c, d):
        # 添加随机数的逻辑
        if c != d:
            print(2)

    def is_game_over(self, a, b):
        # 判断游戏是否结束的逻辑
        if a == b:
            print(1)
        
    def update_score(self, points):
        # 更新分数的逻辑
        self.score += points  


def check_variable(variable):
    if variable != None:  # 错误用法
        return True
    return False


def read_file(file_path):
    file = open(file_path, 'r')
    content = file.read()
    file.close()  # 应该使用with语句来自动管理资源
    return content

def open_file():
    file = open("constants.py", "r")

    content = file.read()

    file.close()