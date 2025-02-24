import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First-Person Shooter")

# Load assets
crosshair_img = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(crosshair_img, BLACK, (25, 25), 10, 2)
pygame.draw.line(crosshair_img, BLACK, (25, 5), (25, 45), 2)
pygame.draw.line(crosshair_img, BLACK, (5, 25), (45, 25), 2)

# Player settings
ammo = 10
health = 100

# Enemy settings
enemy_size = 40
num_enemies = 5
enemies = [{"pos": [random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)], "alive": True} for _ in range(num_enemies)]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click to shoot
            if ammo > 0:
                ammo -= 1
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for enemy in enemies:
                    if enemy["alive"]:
                        ex, ey = enemy["pos"]
                        if abs(mouse_x - ex) < enemy_size and abs(mouse_y - ey) < enemy_size:
                            enemy["alive"] = False  # Enemy hit

    # Draw enemies
    for enemy in enemies:
        if enemy["alive"]:
            pygame.draw.rect(screen, RED, (enemy["pos"][0], enemy["pos"][1], enemy_size, enemy_size))

    # Draw HUD
    pygame.draw.rect(screen, GREEN, (10, 10, health, 20))  # Health bar
    font = pygame.font.Font(None, 36)
    ammo_text = font.render(f"Ammo: {ammo}", True, BLACK)
    screen.blit(ammo_text, (WIDTH - 150, 10))

    # Draw crosshair
    mx, my = pygame.mouse.get_pos()
    screen.blit(crosshair_img, (mx - 25, my - 25))

    pygame.display.flip()

pygame.quit()
