
import pygame

import random

import sys

# Initialize Pygame

pygame.init()
pygame.font.init()



# Set up the screen

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Alien Shooter")



# Set up colors

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)



# Set up the player

player_img = pygame.image.load('spaceship.png')

player_rect = player_img.get_rect()

player_rect.centerx = WIDTH // 2

player_rect.bottom = HEIGHT - 10



# Set up the bullet

bullet_img = pygame.image.load('bullet.png')

# bullet_img.fill(RED)

bullet_rect = bullet_img.get_rect()

bullet_speed = -5

bullet_list = []



# Set up the enemy

enemy_img = pygame.image.load('ufo.png')

enemy_rect = enemy_img.get_rect()

enemy_speed = 2

enemy_spawn_delay = 1000  # milliseconds

last_enemy_spawn = pygame.time.get_ticks()

enemies = []



# Set up the game clock

clock = pygame.time.Clock()


# Creating Score Board
score = 0

score_increment = 1

font = pygame.font.Font(None, 48)

# Game loop

while True:

    # Event handling

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullet = bullet_rect.copy()

                bullet.centerx = player_rect.centerx

                bullet.bottom = player_rect.top

                bullet_list.append(bullet)



    # Move the player

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:

        player_rect.x -= 5

    if keys[pygame.K_RIGHT]:

        player_rect.x += 5



    # Move the bullet

    for bullet in bullet_list:

        bullet.y += bullet_speed

        if bullet.y < 0:

            bullet_list.remove(bullet)



    # Spawn enemies

    now = pygame.time.get_ticks()

    if now - last_enemy_spawn > enemy_spawn_delay:

        enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)

        enemy_rect.y = -enemy_rect.height

        enemies.append(enemy_rect.copy())

        last_enemy_spawn = now



    # Move enemies

    for enemy in enemies:

        enemy.y += enemy_speed

        if enemy.y > HEIGHT:

            enemies.remove(enemy)



    # Collision detection

    for bullet in bullet_list:

        for enemy in enemies:

            if bullet.colliderect(enemy):

                bullet_list.remove(bullet)

                enemies.remove(enemy)

                score += score_increment



    # Draw everything

    screen.fill(WHITE)

    screen.blit(player_img, player_rect)

    score_text = font.render(f'Score: {score}', True, (255, 0, 0))

    screen.blit(score_text, (0, 0))

    for bullet in bullet_list:

        screen.blit(bullet_img, bullet)

    for enemy in enemies:

        screen.blit(enemy_img, enemy)



    # Update the display

    pygame.display.flip()



    # Cap the frame rate

    clock.tick(60)