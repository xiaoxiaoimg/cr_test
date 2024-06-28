class GameBoard:
    def __init__(self):
        self.grid = [[0] * 10 for _ in range(20)]  # 10列20行

    def add_shape(self, shape):
        # 模拟异常抛出，违反CR点24
        try:
            # 假设这里有代码抛出异常
            raise Exception("形状添加失败")
        except Exception as e:
            pass  # 使用pass忽略了异常

    # 其他游戏板相关的方法...
