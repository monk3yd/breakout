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
RED = (255, 0, 0)

# Frames Per Second
FPS = 60

# Border
TOP_BORDER = pygame.Rect(0, 0,  WIDTH, 10)
LEFT_BORDER = pygame.Rect(0, 0,  10, HEIGHT-60)
RIGHT_BORDER = pygame.Rect(490, 0,  10, HEIGHT-60)

# Bar Dimensions
BAR_WIDTH, BAR_HEIGHT = (150, 20)
# Bar Speed
VEL = 3

# Ball
BALL_WIDTH, BALL_HEIGHT = (23, 23)
BALL_IMAGE = pygame.image.load(os.path.join("img", "ball.png"))
BALL = pygame.transform.scale(BALL_IMAGE, (BALL_WIDTH, BALL_HEIGHT))
# Ball Speed
BALL_VEL = [2, 2]  # x, y


def draw_window(bar, ball, blocks):
    # Background
    WIN.fill(BLACK)
    # Draw Border
    pygame.draw.rect(WIN, WHITE, TOP_BORDER)
    pygame.draw.rect(WIN, WHITE, LEFT_BORDER)
    pygame.draw.rect(WIN, WHITE, RIGHT_BORDER)

    # Draw Bar
    pygame.draw.rect(WIN, WHITE, bar)

    # Draw Ball
    WIN.blit(BALL, (ball.x, ball.y))
    # pygame.draw.rect(WIN, WHITE, ball)
    # pygame.draw.circle(WIN, WHITE, [WIDTH//2, HEIGHT//2], 5, 0)  # Surface, color, pos, radius, width

    # Draw Blocks
    for block in blocks:
        pygame.draw.rect(WIN, RED, block)
    # Update Frame
    pygame.display.update()


def handle_bar_movement(keys, bar):
    if keys[pygame.K_LEFT] and bar.x >= 0:
        bar.x -= VEL

    if keys[pygame.K_RIGHT] and bar.x + bar.width <= WIDTH:
        bar.x += VEL


def handle_ball_movement(ball, bar):
    ball.x += BALL_VEL[0]
    ball.y += BALL_VEL[1]

    # BOUNCE
    if LEFT_BORDER.colliderect(ball) or RIGHT_BORDER.colliderect(ball):
        BALL_VEL[0] *= -1

    if TOP_BORDER.colliderect(ball):
        BALL_VEL[1] *= -1

    if bar.colliderect(ball):
        BALL_VEL[1] *= -1


def handle_blocks(blocks):
    for block in blocks:
        pass


def main():
    # Bar Rectangle
    bar = pygame.Rect(WIDTH/2 - 75, HEIGHT - 50, BAR_WIDTH, BAR_HEIGHT)  # x, y, width, height
    # Ball Rectangle
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_WIDTH, BALL_HEIGHT)
    # Blocks
    blocks = []
    block = pygame.Rect(20, 80, 50, 20)
    blocks.append(block)

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
        handle_ball_movement(ball, bar)
        handle_blocks(blocks)
        draw_window(bar, ball, blocks)


if __name__ == "__main__":
    main()
