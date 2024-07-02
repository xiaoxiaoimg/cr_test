import pygame
import random
from game_utils import load_image


class Food:
    def __init__(self):
        self.image = load_image("food.png")
        self.rect = pygame.Rect(0, 0, 10, 10)

    def respawn(self, width, height):
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(0, height - self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
