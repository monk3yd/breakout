import pygame
import os

# Window
WIDTH, HEIGHT = 500, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Title
pygame.display.set_caption("Breakout Game")
# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frames Per Second
FPS = 60

# Border
BORDER = pygame.Rect(0, 0,  WIDTH, 20)

# Bar Dimensions
BAR_WIDTH, BAR_HEIGHT = (150, 20)

# BAR SPEED
VEL = 3


def draw_window(bar):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    pygame.draw.rect(WIN, WHITE, bar)
    pygame.display.update()


def handle_bar_movement(keys, bar):
    if keys[pygame.K_LEFT] and bar.x >= 0:
        bar.x -= VEL

    if keys[pygame.K_RIGHT] and bar.x + bar.width <= WIDTH:
        bar.x += VEL


def main():
    bar = pygame.Rect(WIDTH/2 - 75, 650, BAR_WIDTH, BAR_HEIGHT)
    # TODO - ball

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        handle_bar_movement(keys_pressed, bar)
        draw_window(bar)


if __name__ == "__main__":
    main()
