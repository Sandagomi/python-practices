import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load("AutomationScripts/assests/player.png")
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.image.load("AutomationScripts/assests/enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
laser_img = pygame.image.load("AutomationScripts/assests/laser.png")
laser_img = pygame.transform.scale(laser_img, (6, 15))

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
BLACK = (10, 10, 20)

# Player
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 80, 50, 50)
player_speed = 6

# Bullets
bullets = []
bullet_speed = 7

# Enemies
enemies = []
enemy_speed = 3

# Particles (explosions)
particles = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 72)

# Game state
game_started = False

# Start button
button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 25, 150, 50)
YELLOW = (255, 255, 0)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def draw_title(text, x, y):
    img = title_font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def draw_start_screen():
    draw_title("SPACE SHOOTER", 50, 150)
    pygame.draw.rect(screen, YELLOW, button_rect)
    pygame.draw.rect(screen, WHITE, button_rect, 2)
    button_text = font.render("START", True, BLACK)
    screen.blit(button_text, (button_rect.centerx - 35, button_rect.centery - 18))

def spawn_enemy():
    x = random.randint(20, WIDTH - 40)
    enemies.append(pygame.Rect(x, -50, 40, 40))

def create_explosion(x, y):
    for _ in range(15):
        particles.append([
            [x, y],
            [random.uniform(-2, 2), random.uniform(-2, 2)],
            random.randint(3, 6)
        ])

def update_particles():
    for p in particles[:]:
        p[0][0] += p[1][0]
        p[0][1] += p[1][1]
        p[2] -= 0.2
        if p[2] <= 0:
            particles.remove(p)

def draw_particles():
    for p in particles:
        pygame.draw.circle(screen, RED, (int(p[0][0]), int(p[0][1])), int(p[2]))

SPAWN = pygame.USEREVENT
pygame.time.set_timer(SPAWN, 800)

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            mouse_pos = event.pos
            if button_rect.collidepoint(mouse_pos):
                game_started = True

        if event.type == SPAWN and game_started:
            spawn_enemy()

        if event.type == pygame.KEYDOWN and game_started:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - 3, player.y, 6, 15))
    
    if not game_started:
        draw_start_screen()
    else:
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Bullets
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # Enemies
        for enemy in enemies[:]:
            enemy.y += enemy_speed

            # Collision
            for bullet in bullets[:]:
                if enemy.colliderect(bullet):
                    create_explosion(enemy.centerx, enemy.centery)
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
                    break

            if enemy.top > HEIGHT:
                enemies.remove(enemy)

            if enemy.colliderect(player):
                print("GAME OVER")
                pygame.quit()
                sys.exit()

        # Draw player
        screen.blit(player_img, player)

        # Draw bullets
        for bullet in bullets:
            screen.blit(laser_img, bullet)

        # Draw enemies
        for enemy in enemies:
            screen.blit(enemy_img, enemy)

        # Particles
        update_particles()
        draw_particles()

        # Score
        draw_text(f"Score: {score}", 10, 10)

    pygame.display.update()