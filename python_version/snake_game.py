import sys, pygame
from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

# Initialize the module
pygame.init()

# Variables for the colors
color_black = 0, 0, 0
color_green = 0, 255, 0

# Variables for the display
display_size = screen_width, screen_height = 600, 600
game_over = False

# Variables for the snake
bodyParts = 1
x_snake = [150]
y_snake = [150]
direction = Direction.RIGHT

# Generate the screen
display = pygame.display.set_mode(display_size)

# Variables for the change in direction
x_change = 0
y_change = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # Handle arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != Direction.RIGHT:
                direction = Direction.LEFT
            if event.key == pygame.K_RIGHT and direction != Direction.LEFT:
                direction = Direction.RIGHT
            if event.key == pygame.K_UP and direction != Direction.DOWN:
                direction = Direction.UP
            if event.key == pygame.K_DOWN and direction != Direction.UP:
                direction = Direction.DOWN

    # Move the snake -- probably will implement a switch statement manually for this later
    if (direction == Direction.RIGHT):
        x_change = 10
        y_change = 0
    elif (direction == Direction.LEFT):
        x_change = -10
        y_change = 0
    elif (direction == Direction.UP):
        x_change = 0
        y_change = -10
    else:
        x_change = 0
        y_change = 10

    for i in range(bodyParts-1, 1, -1):
        x_snake[i] = x_snake[i-1]
        y_snake[i] = y_snake[i-1]

    # Draw the snake
    for i in range(bodyParts):
        x = x_snake[i]
        y = y_snake[i]
        pygame.draw.rect(display, color_green, [x, y, 25, 25])
    pygame.display.update()

# After we exit the game
pygame.quit()
quit()

