import sys, pygame, time, random
from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

def print_game_over():
    text = pygame.font.SysFont(None, 50).render('GAME OVER', True, color_red)
    display.blit(text, [screen_width / 2 - 100, screen_height / 2])

# Some useful colors
color_black = 0, 0, 0
color_red = 255, 0, 0
color_green = 0, 255, 0

# Variables for the display
display_size = screen_width, screen_height = 600, 600
unit_size = 20
game_over = False

# Variables for the snake
direction = Direction.RIGHT
x_change = 0
y_change = 0
x_snake = [round(screen_width / 2)]
y_snake = [round(screen_height / 2)]
body_parts = len(x_snake)

# Variables for the food
apples_eaten = 0
apple_x = round(random.randrange(0, screen_width - unit_size) / unit_size) * unit_size
apple_y = round(random.randrange(0, screen_height - unit_size) / unit_size) * unit_size

# Initialize the PyGame module
pygame.init()

# Generate the screen
display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Snake Game")

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

    # Get the change in movement
    if (direction == Direction.RIGHT):
        x_change = unit_size
        y_change = 0
    elif (direction == Direction.LEFT):
        x_change = -unit_size
        y_change = 0
    elif (direction == Direction.UP):
        x_change = 0
        y_change = -unit_size
    else:
        x_change = 0
        y_change = unit_size

    if body_parts > len(x_snake):
        x_snake.append(0)
        y_snake.append(0)

    # Move the snake
    for i in range(body_parts - 1, 1, -1):
        x_snake[i] = x_snake[i-1]
        y_snake[i] = y_snake[i-1]
    x_snake[0] += x_change
    y_snake[0] += y_change

    # Check for snake collision
    for i in range(body_parts-1, 1, -1):
        if x_snake[i] == x_snake[0] and y_snake[i] == y_snake[0]:
            game_over = True

    # Check for border collisions
    if x_snake[0] < 0 or x_snake[0] > screen_width or y_snake[0] < 0 or y_snake[0] > screen_height:
        game_over = True

    # Clear the screen
    display.fill(color_black) 

    # Draw the food
    pygame.draw.rect(display, color_red, [apple_x, apple_y, unit_size, unit_size])

    # Draw the snake
    for i in range(body_parts):
        pygame.draw.rect(display, color_green, [x_snake[i], y_snake[i], unit_size, unit_size])

    # Check if the apple was eaten
    if x_snake[0] == apple_x and y_snake[0] == apple_y:
        apples_eaten += 1
        body_parts += 1
        apple_x = round(random.randrange(0, screen_width - unit_size) / unit_size) * unit_size
        apple_y = round(random.randrange(0, screen_height - unit_size) / unit_size) * unit_size

    # Update the screen
    pygame.display.update()

    # Update timer
    clock.tick(20)

# After we exit the game
print_game_over()
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
