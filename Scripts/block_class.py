import pygame
from config import BLACK, WHITE, GRAY, W, H, BLOCK_SIZE, MARGIN, RES_W, RES_H, X_MARGIN, Y_MARGIN, BOARD_WIDTH
from copy import deepcopy
import numpy as np


## Write a class for a Kanoodle block
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
        
        self.dx, self.dy = 0,0
        self.orientation = 1
        self.board_coords = self.coords
    
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
        elif dx > 0:
            self.shift_right(dx)
        elif dx < 0:
            self.shift_left(-dx)
        elif dy > 0:
            self.shift_up(dy)
        elif dy < 0:
            self.shift_down(-dy)
        
        if self.check_borders(field):
            self.dx += dx
            self.dy -= dy
        else:    
            self.rects = rects_old

    def shift_up(self, amt=1):
        for rect in self.rects:
            rect.y -= amt
    
    def shift_down(self, amt=1):
        for rect in self.rects:
            rect.y += amt
            
    def shift_right(self, amt=1):
        for rect in self.rects:
            rect.x += amt

    def shift_left(self, amt=1):
        for rect in self.rects:
            rect.x -= amt
    
    def rotate(self, direction, field):
        rects_old = deepcopy(self.rects)
        coords_old = deepcopy(self.coords)
        print(f'Old coords: {self.coords}')
        print(f"Old rects: {self.rects}")
        print(f'dx: {self.dx}, dy: {self.dy}')
        if direction == "CW":
            self.rotate_clockwise()
        elif direction == "CCW":
            self.rotate_counterclockwise()

        print(f"Pre-border coords: {self.coords}")
        print(f"Pre-border rects: {self.rects}")
        if not self.check_borders(field):
            self.rects = rects_old
            self.coords = coords_old
        print(f'New coords: {self.coords}')
        print("")

    def rotate_clockwise(self):
        print("Rotating Clockwise")
        self.coords = [(y, -x) for x,y in self.coords]
        for rect, new_coord in zip(self.rects, self.coords):
             rect.x, rect.y = new_coord[0] + self.dx, new_coord[1] + self.dy

    def rotate_counterclockwise(self):
        print("Rotating Counterclockwise")
        self.coords = [(-y, x) for x,y in self.coords]
        for rect, new_coord in zip(self.rects, self.coords):
             rect.x, rect.y = new_coord[0] + self.dx, new_coord[1] + self.dy

            
    # Reflect about the y-axis
    def flip_y(self):
        for i in range(len(self.rects)):
            self.rects[i].y = self.height - self.rects[i].y - 1

        self.set_orientation()

