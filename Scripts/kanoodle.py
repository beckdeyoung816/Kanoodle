import pygame
from block_class import block

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set the size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the size of the grid
GRID_WIDTH = 10
GRID_HEIGHT = 6

# Set the size of each block
BLOCK_SIZE = 40

# Set the size of the margin between blocks
MARGIN = 5

# Set the size of the board
BOARD_WIDTH = (BLOCK_SIZE + MARGIN) * GRID_WIDTH + MARGIN

# Create a grid
grid = [pygame.Rect(MARGIN + (MARGIN + BLOCK_SIZE) * x, MARGIN + (MARGIN + BLOCK_SIZE) * y, BLOCK_SIZE, BLOCK_SIZE) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Kanoodle")

# Loop until the user clicks the close button
while True:
    screen.fill(pygame.Color('black'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Draw the grid
    [pygame.draw.rect(screen, GRAY, rect, 1) for rect in grid]
            
    pygame.display.flip()
    clock.tick()

