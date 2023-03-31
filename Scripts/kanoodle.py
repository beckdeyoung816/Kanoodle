import pygame
from block_class import block
from config import BLACK, WHITE, GRAY, COLORS, W, H, BLOCK_SIZE, MARGIN, RES_W, RES_H, X_MARGIN, Y_MARGIN, BOARD_WIDTH

# Create blocks
blocks = [block(color) for color in COLORS]

figure_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)

# Create a grid
grid = [pygame.Rect(X_MARGIN + (MARGIN + BLOCK_SIZE) * x, Y_MARGIN + (MARGIN + BLOCK_SIZE) * y, BLOCK_SIZE, BLOCK_SIZE) for x in range(W) for y in range(H)]

# Create an empty field
field = [[0 for i in range(W)] for j in range(H)]

figure = blocks[0]

# Initialize Pygame
pygame.init()

# Set the size of the screen
sc = pygame.display.set_mode((RES_W, RES_H))
# game_sc = pygame.Surface(RES_W, RES_H)
clock = pygame.time.Clock()
pygame.display.set_caption("Kanoodle")

# Create buttons
# define constants
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_SPACING = 10
FONT_SIZE = 10
# create font object
font = pygame.font.SysFont('Arial', FONT_SIZE)

# create list to store buttons
buttons = []

# create each button and add it to the list

for i, color in enumerate(COLORS):
    button_x = (RES_W - BUTTON_WIDTH) - 40
    button_y = i * (BUTTON_HEIGHT + BUTTON_SPACING) + BUTTON_SPACING
    button_rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    button_text = font.render(color, True, (0, 0, 0))
    buttons.append((button_rect, button_text, color))

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
                if event.key in [pygame.K_LEFT]:
                    figure.rotate("CW", field)
                elif event.key in [pygame.K_RIGHT]:
                    figure.rotate("CCW", field)
            elif event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = 1
            elif event.key == pygame.K_DOWN:
                dy = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if a button was clicked
            for button_rect, button_text, color in buttons:
                if button_rect.collidepoint(event.pos):
                    figure = block(color)
                    # do something when the button is clicked
    
    # draw buttons
    for button_rect, button_text, color in buttons:
        pygame.draw.rect(sc, pygame.Color(WHITE), button_rect)
        sc.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))

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

