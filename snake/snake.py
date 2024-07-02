import pygame
from game_utils import load_image


class Snake:
    def __init__(self):
        self.segments = [pygame.Rect(50, 50, 10, 10)]  # 初始位置
        self.direction = 0, -10  # 初始方向

    def change_direction(self, x, y):
        assert (x, y) != (-self.direction[0], -self.direction[1]), "相反方向"
        self.direction = x, y

    def move(self):
        # 移动蛇
        head_x = self.segments[0].x + self.direction[0]
        head_y = self.segments[0].y + self.direction[1]
        new_segment = pygame.Rect(head_x, head_y, 10, 10)

        # 检查碰撞边界
        if new_segment.left < 0 or new_segment.right > screen_width:
            raise Exception("撞到边界")
        if new_segment.top < 0 or new_segment.bottom > screen_height:
            raise Exception("撞到边界")

        self.segments.insert(0, new_segment)
        if len(self.segments) > 1:
            last_segment = self.segments.pop()

    def grow(self):
        # 增加蛇的长度
        tail_segment = self.segments[-1]
        new_segment = pygame.Rect(tail_segment.x, tail_segment.y, 10, 10)
        self.segments.append(new_segment)
