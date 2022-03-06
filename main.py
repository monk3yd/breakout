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

COLORS = {
    "red": (255, 0, 0),
    "orange": (255, 126, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0)
}

# Frames Per Second
FPS = 60

# Border
TOP_BORDER = pygame.Rect(0, 0,  WIDTH, 10)
LEFT_BORDER = pygame.Rect(0, 0,  10, HEIGHT-60)
RIGHT_BORDER = pygame.Rect(490, 0,  10, HEIGHT-60)

# Bar
BAR_WIDTH, BAR_HEIGHT = (100, 20)  # Size
VEL = 3  # Speed

# Ball
BALL_WIDTH, BALL_HEIGHT = (15, 15)  # Size
BALL_IMAGE = pygame.image.load(os.path.join("img", "ball.png"))
BALL = pygame.transform.scale(BALL_IMAGE, (BALL_WIDTH, BALL_HEIGHT))
BALL_VEL = [0, 0]  # x, y  # Ball Velocity

# Blocks
BLOCK_WIDTH, BLOCK_HEIGHT = (30, 10)
BLOCK_DIST = 6
BLOCK_ROWS = 8
BLOCK_COLS = 13


class Rect(object):
    def __init__(self, *args):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_value(self, color):
        self.color = color
        self.image.fill(color)


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

    # Draw Blocks
    for block in blocks:
        pygame.draw.rect(WIN, COLORS['red'], block)

    # Update Frame
    pygame.display.update()


def handle_bar_movement(keys, bar):
    if keys[pygame.K_LEFT] and bar.x >= 0:
        bar.x -= VEL

    if keys[pygame.K_RIGHT] and bar.x + bar.width <= WIDTH:
        bar.x += VEL


def handle_ball_movement(ball, bar, blocks):
    # Movement
    ball.x += BALL_VEL[0]
    ball.y += BALL_VEL[1]

    # Bounce Collision with Wall
    if LEFT_BORDER.colliderect(ball) or RIGHT_BORDER.colliderect(ball):
        BALL_VEL[0] *= -1

    if TOP_BORDER.colliderect(ball):
        BALL_VEL[1] *= -1

    # Bounce Collision with Bar
    if bar.colliderect(ball):
        BALL_VEL[1] *= -1

    # Bounce Collision with Blocks
    # for block in blocks:
    #     if block.colliderect(ball):
    #         BALL_VEL[1] *= -1
    #         blocks.remove(block)
    #         # TODO Score++
        # touch = pygame.sprite.collide_rect(block)
        # if touch:


def main():
    # Bar Rectangle
    bar = pygame.Rect(WIDTH/2 - 75, HEIGHT - 50, BAR_WIDTH, BAR_HEIGHT)  # x, y, width, height
    # Ball Rectangle
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_WIDTH, BALL_HEIGHT)
    # Blocks Rectangles
    blocks = []
    for i in range(BLOCK_COLS):
        for j in range(BLOCK_ROWS):
            # Check for Block Color.
            if j < 2:
                color = COLORS["red"]
            elif j >= 2 and j < 4:
                color = COLORS["orange"]
            elif j >= 4 and j < 6:
                color = COLORS["green"]
            else:
                color = COLORS["yellow"]

            x = 20 + i * (BLOCK_DIST + BLOCK_WIDTH)
            y = 20 + j * (BLOCK_DIST + BLOCK_HEIGHT) + 80
            block = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, color)
            blocks.append(block)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Start
                if event.key == pygame.K_SPACE:
                    BALL_VEL[0] = 3
                    BALL_VEL[1] = 3
                    print("Game Start.")
                    # TODO Write Text on Screen
                # TODO Pause
                if event.key == pygame.K_p:
                    print("Pause.")
                    # TODO Write Text on Screen

        gameover_text = ""

        keys_pressed = pygame.key.get_pressed()
        handle_bar_movement(keys_pressed, bar)
        handle_ball_movement(ball, bar, blocks)
        draw_window(bar, ball, blocks)


if __name__ == "__main__":
    main()
