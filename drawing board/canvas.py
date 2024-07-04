class DrawingCanvas:
    def __init__(self, width=800, height=600):  
        self.width = width
        self.height = height
        self.drawings = []

    
    def for(self, x, y):  
        pass

    def draw_line(self, start_x, start_y, end_x, end_y):
        # 画线逻辑
        self.drawings.append((start_x, start_y, end_x, end_y))
        print("Line drawn from {} to {}".format(start_x, end_x))  
        print("Line drawn from"+start_x+"to"+end_x)
    
    @property
    def size(self):
        return (self.width, self.height)

    def draw@(self):
        pass