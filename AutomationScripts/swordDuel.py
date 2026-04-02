import pygame
import sys
import random

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sword Duel PRO")

clock = pygame.time.Clock()
#impact
# Load images

p1_img = pygame.image.load("AutomationScripts/assests/player1.png")
p2_img = pygame.image.load("AutomationScripts/assests/player2.png")
slash_img = pygame.image.load("AutomationScripts/assests/player.png")
# Load sounds
p1_img = pygame.transform.scale(p1_img, (80, 120))
p2_img = pygame.transform.scale(p2_img, (80, 120))
slash_img = pygame.transform.scale(slash_img, (100, 100))


# Players
player1 = pygame.Rect(150, 300, 80, 120)
player2 = pygame.Rect(650, 300, 80, 120)

p1_health = 100
p2_health = 100

# States
p1_attack = 0
p2_attack = 0
p1_block = False
p2_block = False

particles = []

font = pygame.font.SysFont(None, 36)


def create_sparks(x, y):
    for _ in range(12):
        particles.append([
            [x, y],
            [random.uniform(-3, 3), random.uniform(-3, 3)],
            random.randint(4, 6)
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
        pygame.draw.circle(screen, (255, 200, 50),
                           (int(p[0][0]), int(p[0][1])), int(p[2]))


def draw_health():
    pygame.draw.rect(screen, (200, 50, 50), (50, 40, p1_health * 2, 20))
    pygame.draw.rect(screen, (50, 100, 255), (WIDTH - 250, 40, p2_health * 2, 20))


running = True
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player 1 controls
    if keys[pygame.K_a]:
        player1.x -= 5
    if keys[pygame.K_d]:
        player1.x += 5

    if keys[pygame.K_w]:
        if p1_attack == 0:
            pass  # swing_sound.play()
        p1_attack = 10
    else:
        p1_attack = max(0, p1_attack - 1)

    p1_block = keys[pygame.K_s]

    # AI Player 2
    if player2.x > player1.x:
        player2.x -= 3
    else:
        player2.x += 3

    if abs(player2.x - player1.x) < 120:
        if p2_attack == 0:
            pass  # swing_sound.play()
        p2_attack = 10
    else:
        p2_attack = max(0, p2_attack - 1)

    p2_block = random.choice([True, False, False])

    # Attacks
    if p1_attack > 0:
        hitbox = pygame.Rect(player1.right, player1.y, 60, player1.height)
        if hitbox.colliderect(player2) and not p2_block:
            p2_health -= 1
            create_sparks(player2.centerx, player2.centery)
            pass  # hit_sound.play()

    if p2_attack > 0:
        hitbox = pygame.Rect(player2.left - 60, player2.y, 60, player2.height)
        if hitbox.colliderect(player1) and not p1_block:
            p1_health -= 1
            create_sparks(player1.centerx, player1.centery)
            pass  # hit_sound.play()

    # Draw players
    screen.blit(p1_img, (player1.x, player1.y))
    screen.blit(p2_img, (player2.x, player2.y))

    # Draw slash
    if p1_attack > 0:
        screen.blit(slash_img, (player1.right - 20, player1.y))

    if p2_attack > 0:
        flipped = pygame.transform.flip(slash_img, True, False)
        screen.blit(flipped, (player2.left - 80, player2.y))

    # Particles
    update_particles()
    draw_particles()

    # Health
    draw_health()

    # Game Over
    if p1_health <= 0:
        screen.blit(font.render("AI Wins!", True, (255,255,255)), (400, 200))
    elif p2_health <= 0:
        screen.blit(font.render("You Win!", True, (255,255,255)), (400, 200))

    pygame.display.update()