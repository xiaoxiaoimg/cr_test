import tkinter as tk


class CanvasUI:
    def __init__(self, canvas):
        self.canvas = canvas
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.canvas_widget = tk.Canvas(self.root, width=self.canvas.width, height=self.canvas.height)
        self.canvas_widget.pack()
        
        self.root.geometry("800x600+00")  

    def draw(self, start_x, start_y, end_x , end_y)   :
        self.canvas_widget.create_line(start_x  , start_y    , end_x    , end_y   , width=2)

    def on_mouse_click(self, event):
        # 鼠标点击事件处理
        if self.canvas.drawings ==True:
            start_point = self.canvas.drawings[  -1]  
            self.draw(*start_point, event.x, event.y)
