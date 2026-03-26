import pygame
import sys
import random
import os

pygame.init()

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Load assets
bird_img = pygame.image.load(os.path.join(script_dir, "assests/bird.png"))
bg_img = pygame.image.load(os.path.join(script_dir, "assests/bg.png"))
pipe_img = pygame.image.load(os.path.join(script_dir, "assests/pipe.png"))
ground_img = pygame.image.load(os.path.join(script_dir, "assests/ground.png"))

# Resize
bird_img = pygame.transform.scale(bird_img, (40, 30))
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
pipe_img = pygame.transform.scale(pipe_img, (60, 400))
ground_img = pygame.transform.scale(ground_img, (WIDTH, 100))

# Bird
bird_x = 80
bird_y = HEIGHT // 2
velocity = 0
gravity = 0.5
jump = -8

# Pipes
pipes = []
pipe_gap = 150
pipe_speed = 4

# Ground
ground_y = HEIGHT - 100

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Game state
game_active = False
game_over = False


def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


def create_pipe():
    height = random.randint(150, 400)
    top = pipe_img.get_rect(midbottom=(WIDTH + 100, height - pipe_gap // 2))
    bottom = pipe_img.get_rect(midtop=(WIDTH + 100, height + pipe_gap // 2))
    return top, bottom


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    return [pipe for pipe in pipes if pipe.right > -50]


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_img, pipe)
        else:
            flipped = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped, pipe)


def check_collision(pipes):
    bird_rect = pygame.Rect(bird_x, bird_y, 40, 30)
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_y >= ground_y or bird_y <= 0:
        return False
    return True


def reset():
    global bird_y, velocity, pipes, score, game_active, game_over
    bird_y = HEIGHT // 2
    velocity = 0
    pipes.clear()
    score = 0
    game_active = True
    game_over = False


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    velocity = jump
                else:
                    reset()

        if event.type == SPAWNPIPE and game_active:
            pipes.extend(create_pipe())

    # Draw background
    screen.blit(bg_img, (0, 0))

    if game_active:

        # Bird physics
        velocity += gravity
        bird_y += velocity

        # Rotate bird
        rotated_bird = pygame.transform.rotate(bird_img, -velocity * 3)

        # Pipes
        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        # Collision
        game_active = check_collision(pipes)

        # Draw bird
        screen.blit(rotated_bird, (bird_x, bird_y))

        # Score
        score += 0.02
        draw_text(f"Score: {int(score)}", 10, 10)

    else:
        draw_text("Press SPACE to Start", 70, 250)
        if game_over:
            draw_text("Game Over", 120, 300)

    # Ground
    screen.blit(ground_img, (0, ground_y))

    if not game_active and score > 0:
        game_over = True

    pygame.display.update()