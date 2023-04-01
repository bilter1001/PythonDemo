# 1. Try generating with command K. Ask for a pytorch script of a feedforward neural network
# 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
# 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.import pygame
# Initialize pygame
import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food_pos = [300, 300]
food_spawn = False
snake_size = 10
food_size = 10

# 添加时钟控制
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed[1] != 10:
                snake_speed = [0, -10]
            if event.key == pygame.K_DOWN and snake_speed[1] != -10:
                snake_speed = [0, 10]
            if event.key == pygame.K_LEFT and snake_speed[0] != 10:
                snake_speed = [-10, 0]
            if event.key == pygame.K_RIGHT and snake_speed[0] != -10:
                snake_speed = [10, 0]


    # Snake movement
    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

    # Check for collisions
    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        food_spawn = True

    # Draw snake and food
    win.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

    # Update display
    pygame.display.flip()

    # 添加时钟控制
    clock.tick(10)  # 设置帧率为10

# Quit pygame
pygame.quit()
