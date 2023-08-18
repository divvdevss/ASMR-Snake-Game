import pygame
import random

# Initialize the game
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up the snake
snake_block_size = 20
snake_speed = 15
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_x_change = 0
snake_y_change = 0
snake_body = []
snake_length = 1

# Set up the food
food_size = 20
food_x = random.randint(0, screen_width - food_size) // food_size * food_size
food_y = random.randint(0, screen_height - food_size) // food_size * food_size

# Set up the clock
clock = pygame.time.Clock()

# Function to display the snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block_size, snake_block_size])

# Function to display the start screen
def show_start_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 60)
    text = font.render("Snake Game", True, GREEN)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

# Function to display the end screen
def show_end_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

# Start the game
show_start_screen()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keypress events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_x_change == 0:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT and snake_x_change == 0:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP and snake_y_change == 0:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN and snake_y_change == 0:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, screen_width - food_size) // food_size * food_size
        food_y = random.randint(0, screen_height - food_size) // food_size * food_size
        snake_length += 1

    # Update snake body
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for collision with walls or self
    if (
        snake_x < 0
        or snake_x >= screen_width
        or snake_y < 0
        or snake_y >= screen_height
        or snake_head in snake_body[:-1]
    ):
        show_end_screen()
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(screen, RED, [food_x, food_y, food_size, food_size])

    # Draw the snake
    draw_snake(snake_body)

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
