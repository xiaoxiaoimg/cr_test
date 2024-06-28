from game import *  
from snake import Snake
from food import Food

def main():
    game = Game(Snake(), Food())
    game.run()

if __name__ == "__main__":
    main()