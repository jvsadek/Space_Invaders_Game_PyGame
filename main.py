import pygame
import random
import sys

# Initialize pygame
pygame.init()
pygame.font.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player
player_img = pygame.image.load('spaceship.png')
player_width, player_height = player_img.get_size()
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Set up the bullet
bullet_img = pygame.image.load('bullet.png')
bullet_width, bullet_height = bullet_img.get_size()
bullet_speed = 5
bullet_state = "ready"  # ready - ready to fire; fire - bullet is moving
bullet_x = (WIDTH - bullet_width) // 2
bullet_y = HEIGHT - bullet_height - 20

# Set up the alien
alien_img = pygame.image.load('ufo.png')
alien_width, alien_height = alien_img.get_size()
alien_x = random.randint(0, WIDTH - alien_width)
alien_y = random.randint(0, 10)
alien_speed = 2

# Creating Score Board
score = 0
score_increment = 10
font = pygame.font.Font(None, 48)

print(alien_height, alien_width)
print(bullet_height, bullet_width)

# Functions
def player(x, y):
    screen.blit(player_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    global bullet_x
    bullet_x = x
    screen.blit(bullet_img, (x + bullet_width / 2 - bullet_width / 2, y - bullet_height))

def is_collision(alien_x, alien_y, bullet_x, bullet_y):
    distance = ((alien_x - bullet_x) ** 2 + (alien_y - bullet_y) ** 2) ** 0.5
    # print(distance)
    if distance < 25:
        return True
    return False


# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    fire_bullet(player_x, player_y)


    # Bound the player inside the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= WIDTH - player_width:
        player_x = WIDTH - player_width

    # Move the alien
    alien_x += alien_speed
    if alien_x <= 0:
        alien_speed = 2
        alien_y += 20
    elif alien_x >= WIDTH - alien_width:
        alien_speed = -2
        alien_y += 20

    # Check for collision
    collision = is_collision(alien_x, alien_y, bullet_x + bullet_width / 2, bullet_y)
    if collision:
        score += score_increment
        alien_y = random.randint(0, 10)
        # sys.exit()

    # Fire the bullet
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed

        if bullet_y < 0:
            bullet_state = "ready"
            bullet_y = HEIGHT - bullet_height - 20




    # Draw the player, alien, and bullet
    player(player_x, player_y)
    screen.blit(alien_img, (alien_x, alien_y))

    # Draw score board
    score_text = font.render(f'Score: {score}', True, (255, 0, 0))
    screen.blit(score_text, (0, 0))

    pygame.display.update()

pygame.quit()
