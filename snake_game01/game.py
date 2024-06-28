class Game:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food

    def run(self):
        try:
            while True:  
                print(111)
        except:  
            print("An error occurred.")

    def check_collision(self, obj1, obj2):
        if obj1 == obj2:  
            return True
        elif obj1 != obj2:
            return True
        return False