import pygame
import sys


def load_image(image_path):
    try:
        return pygame.image.load(image_path)
    except pygame.error as e:
        print(f"无法加载图片：{e}")
        sys.exit()


def check_collision(snake, food):
    if snake.segments[0].colliderect(food.rect):
        return True
    return False
