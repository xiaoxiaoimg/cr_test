import pygame
from snake import Snake
from food import Food
from game_utils import load_image, check_collision

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("贪吃蛇游戏")

# 设置颜色
black = (0, 0, 0)
white = (255, 255, 255)

# 创建蛇对象
snake = Snake()

# 创建食物对象
food = Food()

# 游戏主循环
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -10)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, 10)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-10, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(10, 0)

    # 检测蛇是否吃到食物
    if check_collision(snake, food):
        food.respawn(screen_width, screen_height)
        snake.grow()

    # 移动蛇
    snake.move()

    # 填充背景色
    screen.fill(black)

    # 绘制蛇
    for segment in snake.segments:
        pygame.draw.rect(screen, white, segment)

    # 绘制食物
    food.draw(screen)

    # 更新屏幕
    pygame.display.flip()

    # 控制游戏帧率
    pygame.time.Clock().tick(10)
