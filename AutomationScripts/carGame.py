import pygame
import random
import sys
import os

pygame.init()

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodging Game")

clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load(os.path.join(script_dir, "assests/player.png"))
enemy_img = pygame.image.load(os.path.join(script_dir, "assests/enemy.png"))
road_img = pygame.image.load(os.path.join(script_dir, "assests/road.png"))

# Resize images
player_img = pygame.transform.scale(player_img, (50, 80))
enemy_img = pygame.transform.scale(enemy_img, (50, 80))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Player
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 5

# Enemy
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -100
enemy_speed = 6

# Road animation
road_y1 = 0
road_y2 = -HEIGHT
road_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 36)

game_over = False


def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


def reset():
    global enemy_x, enemy_y, enemy_speed, score, game_over
    enemy_x = random.randint(0, WIDTH - 50)
    enemy_y = -100
    enemy_speed = 6
    score = 0
    game_over = False


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                reset()

    if not game_over:

        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
            player_x += player_speed

        # Move enemy
        enemy_y += enemy_speed

        if enemy_y > HEIGHT:
            enemy_y = -100
            enemy_x = random.randint(0, WIDTH - 50)
            score += 1
            enemy_speed += 0.4

        # Collision
        player_rect = pygame.Rect(player_x, player_y, 50, 80)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 80)

        if player_rect.colliderect(enemy_rect):
            game_over = True

        # Animate road
        road_y1 += road_speed
        road_y2 += road_speed

        if road_y1 >= HEIGHT:
            road_y1 = -HEIGHT
        if road_y2 >= HEIGHT:
            road_y2 = -HEIGHT

        # Draw road
        screen.blit(road_img, (0, road_y1))
        screen.blit(road_img, (0, road_y2))

        # Draw cars
        screen.blit(player_img, (player_x, player_y))
        screen.blit(enemy_img, (enemy_x, enemy_y))

        # Score
        draw_text(f"Score: {score}", 10, 10)

    else:
        screen.fill((0, 0, 0))
        draw_text("GAME OVER", 120, 250)
        draw_text("Press SPACE to restart", 60, 300)

    pygame.display.update()