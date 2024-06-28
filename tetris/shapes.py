class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        assert shape_type in ["I", "J", "L", "O", "S", "T", "Z"], "无效的形状类型"

    def rotate(self):
        pass
