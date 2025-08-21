import pygame
import random

pygame.init()

# Screen dimensions and setup
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooter Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Player setup
player_width, player_height = 50, 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Bullet setup
bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullets = []

# Enemy setup
enemy_width, enemy_height = 50, 50
enemy_speed = 3
enemies = []

# Game variables
score = 0
running = True

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Movement flags
move_left = False
move_right = False
fire = False  # Track if spacebar is held

# Fire cooldown variables (milliseconds)
fire_cooldown = 100  # fire once every 300 ms (adjust to your liking)
last_fire_time = 0  # stores the time when last bullet was fired

clock = pygame.time.Clock()


def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))


def draw_bullet(bullet):
    pygame.draw.rect(screen, YELLOW, (bullet[0], bullet[1], bullet_width, bullet_height))


def draw_enemy(enemy):
    pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))


def check_collision(bullet, enemy):
    bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
    enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
    return bullet_rect.colliderect(enemy_rect)


def spawn_enemy():
    x = random.randint(0, screen_width - enemy_width)
    y = random.randint(-100, -40)
    return [x, y]


def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


while running:
    dt = clock.tick(60)  # time elapsed since last frame in ms
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_SPACE:
                fire = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_SPACE:
                fire = False

    # Continuous movement
    if move_left:
        player_x -= player_speed
    if move_right:
        player_x += player_speed

    # Keep player inside screen bounds
    player_x = max(0, min(player_x, screen_width - player_width))

    # Fire bullets continuously with cooldown
    current_time = pygame.time.get_ticks()
    if fire and current_time - last_fire_time > fire_cooldown:
        bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])
        last_fire_time = current_time

    # Move bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn enemies randomly
    if random.randint(1, 100) < 10:
        enemies.append(spawn_enemy())

    # Move enemies and check collisions
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemies.remove(enemy)

        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(
                pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)):
            print(f"Game Over! Final Score: {score}")
            running = False

        for bullet in bullets[:]:
            if check_collision(bullet, enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # Draw everything
    draw_player(player_x, player_y)
    for bullet in bullets:
        draw_bullet(bullet)
    for enemy in enemies:
        draw_enemy(enemy)
    display_score()

    pygame.display.update()

pygame.quit()
