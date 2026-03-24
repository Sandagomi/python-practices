import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 600
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game ....")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# =========================
# BUTTON FUNCTION
# =========================
def draw_button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)

    # Hover effect
    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, GREEN, rect)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, GRAY, rect)

    label = font.render(text, True, WHITE)
    screen.blit(label, (x + 20, y + 10))

    return False


# =========================
# START SCREEN
# =========================
def start_screen():
    while True:
        screen.fill(BLACK)

        title = font.render("Snake Game ....", True, WHITE)
        screen.blit(title, (180, 200))

        if draw_button("START", 230, 300, 140, 50):
            return

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# =========================
# GAME LOOP
# =========================
def game_loop():
    snake = [(100, 100)]
    direction = (BLOCK, 0)

    food = (random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK))

    score = 0

    running = True

    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -BLOCK)
                elif event.key == pygame.K_DOWN:
                    direction = (0, BLOCK)
                elif event.key == pygame.K_LEFT:
                    direction = (-BLOCK, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (BLOCK, 0)

        # Move
        head = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])

        snake.insert(0, head)

        # Eat food
        if head == food:
            score += 1
            food = (random.randrange(0, WIDTH, BLOCK),
                    random.randrange(0, HEIGHT, BLOCK))
        else:
            snake.pop()

        # Collision
        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]):
            running = False

        # Draw
        screen.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

        pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()


# =========================
# MAIN FLOW
# =========================
start_screen()
game_loop()

pygame.quit()