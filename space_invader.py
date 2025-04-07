import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width, player_height = 50, 30
player = pygame.Rect(WIDTH//2 - player_width//2, HEIGHT - player_height - 20, player_width, player_height)
player_speed = 5

# Bullets
bullets = []
bullet_width, bullet_height = 5, 15
bullet_speed = 7

# Enemies
enemies = []
enemy_width, enemy_height = 40, 30
enemy_rows = 5
enemy_cols = 10
enemy_speed = 1
enemy_direction = 1
enemy_move_down = False

for row in range(enemy_rows):
    for col in range(enemy_cols):
        enemy = pygame.Rect(
            100 + col * (enemy_width + 20),
            50 + row * (enemy_height + 20),
            enemy_width,
            enemy_height
        )
        enemies.append(enemy)


# Enemy bullets
enemy_bullets = []
enemy_bullet_speed = 5
enemy_shoot_chance = 0.01  # 1% chance per frame per enemy

# Game variables
score = 0
lives = 3
font = pygame.font.Font(None, 36)
game_over = False

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = pygame.Rect(
                    player.x + player_width//2 - bullet_width//2,
                    player.y,
                    bullet_width,
                    bullet_height
                )
                bullets.append(bullet)
            if event.key == pygame.K_r and game_over:
                # Reset game
                enemies = []
                for row in range(enemy_rows):
                    for col in range(enemy_cols):
                        enemy = pygame.Rect(
                            100 + col * (enemy_width + 20),
                            50 + row * (enemy_height + 20),
                            enemy_width,
                            enemy_height
                        )
                        enemies.append(enemy)
                bullets = []
                enemy_bullets = []
                score = 0
                lives = 3
                game_over = False