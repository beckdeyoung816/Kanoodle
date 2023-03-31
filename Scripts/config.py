# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Colors
COLORS = ["Purple", "Dark Green", "Light Green", "Red", "Yellow", "Dark Blue", "Orange", "Dark Pink", "Light Blue", "White", "Gray", "Light Pink"]
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

# Grid borders
GRID_BORDER_X_LEFT = 0

# Set the size of the board
BOARD_WIDTH = (BLOCK_SIZE + MARGIN) * W + MARGIN

# Buttons
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_SPACING = 10
FONT_SIZE = 10
