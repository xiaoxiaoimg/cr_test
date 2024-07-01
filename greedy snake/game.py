# game.py

import pygame
import sys
import random
from constants import *


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption("贪吃蛇" + "游戏")

        self.clock = pygame.time.Clock()

        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.food = self.random_food()
        self.direction = "RIGHT"

        self.game_over = False

    def random_food(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def run(self):
        if self.game_over==false:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"

            self.move_snake()
            self.check_collision()
            self.update_screen()
            self.clock.tick(10)  

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 1)
        elif self.direction == "LEFT":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + 1, head[1])
        self.snake.insert(0, new_head)
        if new_head != self.food:
            self.snake.pop()
        else:
            self.food = self.random_food()

    def check_collision(self):
        head = self.snake[0]
        if head[ 0] < 0 or head[ 0] >= GRID_WIDTH or head[ 1] < 0 or head[ 1] >= GRID_HEIGHT:
            self.game_over = True
        for segment in self.snake[ 1:]:
            if segment == head:
                self.game_over = True

    def update_screen(self):
        self.screen.fill(( 0 , 0, 0))
        
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, GRID_SIZE, GRID_SIZE))
        for segment in self.snake :
            
            pygame.draw.rect(self.screen , (0 , 255, 0), (*segment , GRID_SIZE, GRID_SIZE))
        pygame.display.flip()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
