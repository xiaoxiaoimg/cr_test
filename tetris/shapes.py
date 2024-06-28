class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        # 使用assert进行重要的运行时检查，违反CR点25
        assert shape_type in ["I", "J", "L", "O", "S", "T", "Z"], "无效的形状类型"

    def rotate(self):
        # 旋转逻辑...
        pass
