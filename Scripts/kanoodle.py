import pygame
from block_class import block

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set the size of the grid
W,H = 10, 6

# Set the size of each block
BLOCK_SIZE = 45

# Set the size of the margin between blocks
MARGIN = 5 #5

RES_W, RES_H = 800, 600
FPS = 60

# Set the margin between the board and the edge of the screen
# The x margin should center the board
X_MARGIN = (RES_W - (BLOCK_SIZE + MARGIN) * W - MARGIN) // 2
Y_MARGIN = 20

# Set the size of the board
BOARD_WIDTH = (BLOCK_SIZE + MARGIN) * W + MARGIN

# Create list of items where each item is the set of coordinates for a given kanoodle piece where the first index is the center of rotation for the piece

blocks = [[(0,0), (1,0), (2,0), (3,0)], # Purple
          [(0,0), (0,-1), (0,-2), (1,-2)], # Dark Green
          [(0,0), (1, 1), (1,-1), (-1,-1)] # Light Green
          ]

blocks = [block(color) for color in ["Purple", "Dark Green", "Light Green", "Red", "Yellow", "Dark Blue", "Orange", "Dark Pink", "Light Blue", "White", "Gray", "Light Pink"]]

#figures = [[pygame.Rect(x + RES_W // 2 + X_MARGIN, y + 1 + Y_MARGIN, 1, 1) for x, y in fig_pos] for fig_pos in pieces]

figure_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)

# Create a grid
grid = [pygame.Rect(X_MARGIN + (MARGIN + BLOCK_SIZE) * x, Y_MARGIN + (MARGIN + BLOCK_SIZE) * y, BLOCK_SIZE, BLOCK_SIZE) for x in range(W) for y in range(H)]


block_1 = blocks[2]
# Initialize Pygame
pygame.init()

# Set the size of the screen
sc = pygame.display.set_mode((RES_W, RES_H))
# game_sc = pygame.Surface(RES_W, RES_H)
clock = pygame.time.Clock()
pygame.display.set_caption("Kanoodle")

# Loop until the user clicks the close button
while True:
    sc.fill(pygame.Color('black'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Draw the grid
    [pygame.draw.rect(sc, GRAY, rect, 1) for rect in grid]
    
    # Draw the figure
    for i in range(len(block_1.rects)):
        figure_rect.x = X_MARGIN + block_1.rects[i].x * (BLOCK_SIZE + MARGIN)
        figure_rect.y = Y_MARGIN + block_1.rects[i].y * (BLOCK_SIZE + MARGIN) 
        pygame.draw.rect(sc, block_1.rgb, figure_rect)

            
    pygame.display.flip()
    clock.tick()

