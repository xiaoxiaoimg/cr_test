import pygame
import time


class GameUI:
    def __init__(self, screen, game_board):
        self.screen = screen
        self.game_board = game_board
        self.clock = pygame.time.Clock()

    def start_game_loop(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(10)  # 控制游戏帧率

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        # 更新游戏状态...
        time.sleep(0.1)

    def render(self):
        self.screen.fill((0, 0, 0))
        # 绘制游戏板...
        pygame.display.flip()
