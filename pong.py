import pygame
import random

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_SPEED = 5
PADDLE_SPEED = 5
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
BALL_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Set up the clock
clock = pygame.time.Clock()

# Create the paddles
player_paddle = pygame.Rect(10, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(SCREEN_WIDTH / 2 - BALL_SIZE / 2, SCREEN_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)

# Set the initial velocity of the ball
ball_velocity = [random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])]

# Game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_s] and player_paddle.bottom < SCREEN_HEIGHT:
        player_paddle.move_ip(0, PADDLE_SPEED)
    if keys[pygame.K_UP] and computer_paddle.top > 0:
        computer_paddle.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_DOWN] and computer_paddle.bottom < SCREEN_HEIGHT:
        computer_paddle.move_ip(0, PADDLE_SPEED)

    # Move the ball
    ball.move_ip(ball_velocity[0], ball_velocity[1])

    # Check for collisions with the walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_velocity[1] = -ball_velocity[1]
    if ball.left <= 0:
        ball_velocity[0] = BALL_SPEED
        ball_velocity[1] = random.choice([-BALL_SPEED, BALL_SPEED])
    if ball.right >= SCREEN_WIDTH:
        ball_velocity[0] = -BALL_SPEED
        ball_velocity[1] = random.choice([-BALL_SPEED, BALL_SPEED])

    # Check for collisions with the paddles
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_velocity[0] = -ball_velocity[0]
        ball_velocity[1] = random.choice([-BALL_SPEED, BALL_SPEED])

    # Draw the paddles and ball
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
