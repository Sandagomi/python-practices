import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# Snake setup
snake = [(100, 100)]
direction = (BLOCK, 0)

# Food
food = (random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK))

score = 0

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

running = True

while running:
    clock.tick(10)  # speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -BLOCK)
            elif event.key == pygame.K_DOWN:
                direction = (0, BLOCK)
            elif event.key == pygame.K_LEFT:
                direction = (-BLOCK, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (BLOCK, 0)

    # Move snake
    head = (snake[0][0] + direction[0],
            snake[0][1] + direction[1])

    snake.insert(0, head)

    # Check food collision
    if head == food:
        score += 1
        food = (random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK))
    else:
        snake.pop()

    # Check collisions (wall or self)
    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]):
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    show_score()

    pygame.display.update()

pygame.quit()