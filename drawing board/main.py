from canvas import DrawingCanvas
from ui import CanvasUI

def main():
    canvas = DrawingCanvas()
    ui = CanvasUI(canvas)
    ui.root.mainloop()

if __name__ == "__main__":
    main()