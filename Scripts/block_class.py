import pygame
from config import BLACK, WHITE, GRAY, W, H, BLOCK_SIZE, MARGIN, RES_W, RES_H, X_MARGIN, Y_MARGIN, BOARD_WIDTH
from copy import deepcopy
import numpy as np
## Write a class for a tetris block
class block():
    def __init__(self, color):
        self.color = color
        
        if self.color == 'Purple':
            self.coords = [(0, 0), (1, 0), (2, 0), (3, 0)]
            self.center_coord = (0,0) # Center of rotation
            self.rgb = (128, 0, 128)
        elif self.color == 'Dark Green':
            self.coords = [(2,1), (3,1),
                           (0, 0), (1, 0), (2, 0)]
            self.center_coord = (1,0)
            self.rgb = (0, 128, 0)
        elif self.color == 'Dark Blue':
            self.coords = [(0, 1), 
                           (0, 0), (1, 0), (2, 0), (3, 0)]
            self.center_coord = (0,0)
            self.rgb = (0, 0, 128)
        elif self.color == "Orange":
            self.coords = [(0, 1), 
                           (0, 0), (1, 0), (2, 0)]
            self.center_coord = (0,0)
            self.rgb = (255, 165, 0)
        elif self.color == "Red":
            self.coords = [(1, 1), (2, 1), 
                           (0, 0), (1, 0), (2, 0)]
            self.center_coord = (0,0)
            self.rgb = (255, 0, 0)
        elif self.color == "Yellow":
            self.coords = [(0, 1), (2, 1), 
                           (0, 0), (1, 0), (2, 0)]
            self.center_coord = (1,0)
            self.rgb = (255, 255, 0)
        elif self.color == "Light Green": 
            self.coords = [(0, 1), (1, 1), 
                           (0, 0), (1, 0)]
            self.center_coord = (0,0)
            self.rgb = (0, 255, 0)
        elif self.color == "White":
            self.coords = [(0, 1), (1, 1),
                           (0, 0)]
            self.center_coord = (0,0)
            self.rgb = (255, 255, 255)
        elif self.color == "Gray":
            self.coords = [(1, 2), 
                           (0, 1), (1, 1), (2, 1),
                           (1, 0)]
            self.center_coord = (1,1)
            self.rgb = (128, 128, 128)
        elif self.color == "Light Pink":
            self.coords = [(0, 1), 
                           (0, 0), (1, 0), (2, 0), (3, 0)]
            self.center_coord = (0,0)
            self.rgb = (255, 192, 203)
        elif self.color == "Light Blue":
            self.coords = [(0, 2),
                           (0, 1),
                           (0, 0), (1, 0), (2, 0)]
            self.center_coord = (0,0)
            self.rgb = (0, 255, 255)
        elif self.color == "Dark Pink":
            self.coords = [(0, 2),
                           (0, 1), (1, 1),
                           (1, 0), (2, 0)]
            self.center_coord = (1,0)
            
            self.rgb = (255, 20, 147)
        
        # Define Rectangles for shape
        self.rects = [pygame.Rect(x, y, 1, 1) for x,y in self.coords]
        
        center = self.coords.index(self.center_coord)
        self.rects[0], self.rects[center] = self.rects[center], self.rects[0]
        
        self.set_orientation()
    
    def set_orientation(self):
        self.height = max([y for x,y in self.coords])
        self.width = max([x for x,y in self.coords])
        self.x_mid = self.width // 2
        self.y_mid = self.height // 2
    
    def check_borders(self, field):
        for i in range(len(self.rects)):
            x = self.rects[i].x
            y = self.rects[i].y
            # Return false if the block is out of bounds
            if x < 0 or x >= W or y >= H or y < 0:
                return False
            # Return false if there is a block in the way
            elif field[y][x] == 1:
                return False
        return True
    
    def shift(self, dx, dy, field):
        rects_old = deepcopy(self.rects)
        if dx == 0 and dy == 0:
            pass
        elif dx == 1:
            self.shift_right()
        elif dx == -1:
            self.shift_left()
        elif dy == 1:
            self.shift_up()
        elif dy == -1:
            self.shift_down()
        
        if not self.check_borders(field):
            self.rects = rects_old
     
    def shift_up(self):
        for i in range(len(self.rects)):
            self.rects[i].y -= 1 
    
    def shift_down(self):
        for i in range(len(self.rects)):
            self.rects[i].y += 1
            
    def shift_right(self):
        for i in range(len(self.rects)):
            self.rects[i].x += 1

    def shift_left(self):
        for i in range(len(self.rects)):
            self.rects[i].x -= 1
    
    def flip(self, direction, field):
        rects_old = deepcopy(self.rects)
        if direction == "X":
            self.rotate_90(1)
        elif direction == "Y":
            self.rotate_90(-1)
    
        if not self.check_borders(field):
            self.rects = rects_old
    # Reflect about the x-axis of the shape itself not the grid
    
    def rotate_90(self, direction):
        center_coord = self.coords[0]
        
        # Define the angle of rotation (in radians)
        theta = np.pi / 4 * direction

        # Define the center point of the shape
        center = np.array(center_coord).reshape((1, 2))

        # Define the rotation matrix
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        rotation_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

        # Rotate each point around the center of the shape
        rotated_shape = np.dot(np.array(self.coords) - center, rotation_matrix) + center

        # Round the coordinates to the nearest integer
        rotated_shape = np.round(rotated_shape).astype(int)
        
        self.coords = rotated_shape.tolist()
        
        self.rects = [pygame.Rect(x, y, 1, 1) for x,y in self.coords]
        
        # for i in range(len(self.rects)):
        #     #self.rects[i].x = self.width - self.rects[i].x - 1
        #     x = self.rects[i].y - center.x
        #     y = self.rects[i].x - center.y
        #     self.rects[i].x = center.x - x
        #     self.rects[i].y = center.y + y
        
        # self.set_orientation()
            
    # Reflect about the y-axis
    def flip_y(self):
        for i in range(len(self.rects)):
            self.rects[i].y = self.height - self.rects[i].y - 1

        self.set_orientation()
    
        
    def draw(self, screen):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    pygame.draw.rect(screen, self.color, (self.x + j * 20, self.y + i * 20, 20, 20))
                    
                    

