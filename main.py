import pygame

import random
import os

pygame.font.init()  # Initialize PyGame Font Library

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

# Fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
START_FONT = pygame.font.SysFont('comicsans', 30)
PAUSE_FONT = pygame.font.SysFont('comicsans', 30)
GAMEOVER_FONT = pygame.font.SysFont('comicsans', 30)

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

# Blocks
BLOCK_WIDTH, BLOCK_HEIGHT = (30, 10)
BLOCK_DIST = 6
BLOCK_ROWS = 8
BLOCK_COLS = 13

# Score Up
SCORE_UP = pygame.USEREVENT + 1

# Out of Bounds
OUT_OF_BOUND = pygame.USEREVENT + 2


class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def draw_window(bar, ball, blocks, show_start_text, score, paused, gameover):
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
        pygame.draw.rect(WIN, block.color, block)

    # Draw Score
    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (20, 20))

    # Draw Start Text
    if show_start_text:
        start_text = START_FONT.render("Please Press SPACE to Start the Game :)", 1, WHITE)
        WIN.blit(start_text, (50, 300))

    if paused:
        paused_text = PAUSE_FONT.render("Game is Paused. Press P to Resume.", 1, WHITE)
        WIN.blit(paused_text, (80, 300))

    # Draw Game Over Text
    if gameover:
        gameover_text = GAMEOVER_FONT.render("Ball out of bounds. Game Over.", 1, WHITE)
        WIN.blit(gameover_text, (80, 300))
        reset_and_quit_text = GAMEOVER_FONT.render("Game will Restart in 3 seconds...", 1 , WHITE)
        WIN.blit(reset_and_quit_text, (80, 350))
        pygame.display.update()
        pygame.time.delay(3000)
        WIN.fill(BLACK)

    # Update Frame
    pygame.display.update()


def handle_bar_movement(keys, bar):
    if keys[pygame.K_LEFT] and bar.x >= 0:
        bar.x -= VEL

    if keys[pygame.K_RIGHT] and bar.x + bar.width <= WIDTH:
        bar.x += VEL


def handle_ball_movement(ball, bar, blocks, ball_velocity):
    # Movement
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # TODO - Improve Bounce Randomness and Speed by Score
    # Bounce Collision with Wall
    if LEFT_BORDER.colliderect(ball) or RIGHT_BORDER.colliderect(ball):
        ball_velocity[0] *= -1

    if TOP_BORDER.colliderect(ball):
        ball_velocity[1] *= -1

    # Bounce Collision with Bar
    if bar.colliderect(ball):
        ball_velocity[1] *= -1

    # Bounce Collision with Blocks
    for block in blocks:
        if block.rect.colliderect(ball):
            ball_velocity[1] *= -1
            # Score Up
            pygame.event.post(pygame.event.Event(SCORE_UP))
            blocks.remove(block)

    # Ball out of Bounds
    if ball.y >= HEIGHT:
        pygame.event.post(pygame.event.Event(OUT_OF_BOUND))


def main():
    # Bar Rectangle
    bar = pygame.Rect(WIDTH/2 - 75, HEIGHT - 50, BAR_WIDTH, BAR_HEIGHT)  # x, y, width, height
    # Ball Rectangle
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_WIDTH, BALL_HEIGHT)
    # Blocks Rectangles
    blocks = []
    for i in range(BLOCK_COLS):
        for j in range(BLOCK_ROWS):
            color = ()
            # Check for block's color
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

    # Variables
    ball_velocity = [0, 0]  # x, y

    score = 0

    show_start_text = True
    paused = False
    gameover = False

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
                    ball_velocity[0] = 3
                    ball_velocity[1] = 3

                    show_start_text = False  # Remove Starting Text from Screen
                    print("Game Starting.")

                # Pause
                if event.key == pygame.K_p:
                    if not paused:
                        vx, vy = ball_velocity
                        print(vx, vy)
                        paused = True
                        ball_velocity = [0, 0]
                        print("Pause.")
                    else:
                        paused = False
                        ball_velocity = [vx, vy]
                        print("Unpaused.")

            # TODO - Increase More Score if Block is from the Back
            if event.type == SCORE_UP:
                score += 1

            # Game Over
            if event.type == OUT_OF_BOUND:
                gameover = True
                ball_velocity = [0, 0]
                print("Out of Bounds.")
                ball.x = WIDTH // 2
                ball.y = HEIGHT // 2
                

        keys_pressed = pygame.key.get_pressed()
        handle_bar_movement(keys_pressed, bar)
        handle_ball_movement(ball, bar, blocks, ball_velocity)
        draw_window(bar, ball, blocks, show_start_text, score, paused, gameover)

        if gameover:
            gameover = False
            break
    main()


if __name__ == "__main__":
    main()
