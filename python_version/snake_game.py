import sys, pygame, time, random, colors
from direction import Direction

def print_game_over():
    text = pygame.font.SysFont(None, 50).render('GAME OVER', True, colors.red)
    display.blit(text, [screen_width / 2 - 100, screen_height / 2])

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
body_parts = 1
snake_curr_length = body_parts

# Variables for the food
apples_eaten = 0
apple_x = round(random.randrange(0, screen_width - unit_size) / unit_size) * unit_size
apple_y = round(random.randrange(0, screen_height - unit_size) / unit_size) * unit_size
def new_apple():
    global apple_x
    global apple_y
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

    snake_curr_length = body_parts

    # Move the snake
    for i in range(snake_curr_length-1, 0, -1):
        if len(x_snake) < snake_curr_length:
            x_snake.append(0)
            y_snake.append(0)
        x_snake[i] = x_snake[i-1]
        y_snake[i] = y_snake[i-1]
    x_snake[0] += x_change
    y_snake[0] += y_change

    # Check for border collisions
    if x_snake[0] < 0 or x_snake[0] > screen_width - unit_size or y_snake[0] < 0 or y_snake[0] > screen_height - unit_size:
        game_over = True

    # Check for snake collision
    for  i in range(1, snake_curr_length):
        if x_snake[i] == x_snake[0] and y_snake[i] == y_snake[0]:
            game_over = True

    # Check if the apple was eaten
    if x_snake[0] == apple_x and y_snake[0] == apple_y:
        apples_eaten += 1
        body_parts += 1
        new_apple()

    # Clear the screen
    display.fill(colors.black) 

    # Draw the food
    pygame.draw.rect(display, colors.red, [apple_x, apple_y, unit_size, unit_size])

    # Draw the snake
    for i in range(snake_curr_length):
        if i == 0:
            pygame.draw.rect(display, colors.green, [x_snake[i], y_snake[i], unit_size, unit_size])
        else:
            random_color = colors.get_random_color()
            pygame.draw.rect(display, random_color, [x_snake[i], y_snake[i], unit_size, unit_size])

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
