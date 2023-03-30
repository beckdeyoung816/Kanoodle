import pygame
from block_class import block
from copy import deepcopy
from config import BLACK, WHITE, GRAY, COLORS, W, H, BLOCK_SIZE, MARGIN, RES_W, RES_H, X_MARGIN, Y_MARGIN, BOARD_WIDTH

# Create blocks
blocks = [block(color) for color in COLORS]

figure_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)

# Create a grid
grid = [pygame.Rect(X_MARGIN + (MARGIN + BLOCK_SIZE) * x, Y_MARGIN + (MARGIN + BLOCK_SIZE) * y, BLOCK_SIZE, BLOCK_SIZE) for x in range(W) for y in range(H)]

# Create an empty field
field = [[0 for i in range(W)] for j in range(H)]

figure = blocks[3]

# Initialize Pygame
pygame.init()

# Set the size of the screen
sc = pygame.display.set_mode((RES_W, RES_H))
# game_sc = pygame.Surface(RES_W, RES_H)
clock = pygame.time.Clock()
pygame.display.set_caption("Kanoodle")



# Loop until the user clicks the close button
while True:
    dx, dy = 0, 0
    sc.fill(pygame.Color('black'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    figure.flip("X", field)
                elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                    figure.flip("Y", field)
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = 1
            elif event.key == pygame.K_DOWN:
                dy = -1
    # Draw the grid
    [pygame.draw.rect(sc, GRAY, rect, 1) for rect in grid]
    
    # Move figure x position
    figure.shift(dx, dy, field)
        
    # Draw the figure
    for i in range(len(figure.rects)):
        figure_rect.x = X_MARGIN + figure.rects[i].x * (BLOCK_SIZE + MARGIN)
        figure_rect.y = Y_MARGIN + figure.rects[i].y * (BLOCK_SIZE + MARGIN) 
        pygame.draw.rect(sc, figure.rgb, figure_rect)
        
        # Update the field
        #field[figure.rects[i].y][figure.rects[i].x] = 1

            
    pygame.display.flip()
    clock.tick()

