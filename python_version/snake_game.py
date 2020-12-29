import sys, pygame
from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

# Initialize the module
pygame.init()

# Some useful colors
color_black = 0, 0, 0
color_green = 0, 255, 0

# Variables for the display
display_size = screen_width, screen_height = 600, 600
game_over = False

# Variables for the snake
bodyParts = 1
x_snake = 300
y_snake = 300
direction = Direction.RIGHT
x_change = 0
y_change = 0

# Generate the screen
display = pygame.display.set_mode(display_size)

# Timer
clock = pygame.time.Clock()

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

    # Update the position of the snake
    x_snake += x_change
    y_snake += y_change

    # Clear the screen
    display.fill(color_black) 

    # Draw the snake
    pygame.draw.rect(display, color_green, [x_snake, y_snake, 20, 20])

    # Update the screen
    pygame.display.update()

    # Update timer
    clock.tick(30)

# After we exit the game
pygame.quit()
quit()

