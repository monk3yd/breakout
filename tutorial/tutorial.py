import pygame
import os

# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Title
pygame.display.set_caption("PyGame Tutorial")
# Background RGB Color
WHITE = (255, 255, 255)
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
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def handle_yellow_movement(keys, yellow):
    if keys[pygame.K_w]:  # UP
        yellow.y -= VEL

    if keys[pygame.K_s]:  # DOWN
        yellow.y += VEL

    if keys[pygame.K_a]:  # LEFT
        yellow.x -= VEL

    if keys[pygame.K_d]:  # RIGHT
        yellow.x += VEL


def handle_red_movement(keys, red):
    if keys[pygame.K_UP]:  # UP
        red.y -= VEL

    if keys[pygame.K_DOWN]:  # DOWN
        red.y += VEL

    if keys[pygame.K_LEFT]:  # LEFT
        red.x -= VEL

    if keys[pygame.K_RIGHT]:  # RIGHT
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
