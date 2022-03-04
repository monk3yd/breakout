import pygame
import os

# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Title
pygame.display.set_caption("PyGame Tutorial")
# Background RGB Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# FPS/Refresh Rate
FPS = 60
# Spaceships speed
VEL = 3
# Spaceship dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55, 40)

# Spaceships
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("tutorial/Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("tutorial/Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


# Draw to window
def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def handle_yellow_movement(keys, yellow):
    if keys[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL

    if keys[pygame.K_s] and yellow.y + SPACESHIP_HEIGHT + 16 < HEIGHT:  # DOWN
        yellow.y += VEL

    if keys[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL

    if keys[pygame.K_d] and yellow.x + SPACESHIP_WIDTH - 2 * VEL < WIDTH / 2:  # RIGHT
        yellow.x += VEL


def handle_red_movement(keys, red):
    if keys[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL

    if keys[pygame.K_DOWN] and red.y + SPACESHIP_HEIGHT + 16 < HEIGHT:  # DOWN
        red.y += VEL

    if keys[pygame.K_LEFT] and red.x > WIDTH / 2 + 7:  # LEFT
        red.x -= VEL

    if keys[pygame.K_RIGHT] and red.x + SPACESHIP_WIDTH - 3 * VEL < WIDTH:  # RIGHT
        red.x += VEL


def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
