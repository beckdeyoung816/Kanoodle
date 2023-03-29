import pygame
## Write a class for a tetris block
class block():
    def init(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
        if color == 'Purple':
            self.shape = [[1, 1, 1, 1]]
            self.rgb = (128, 0, 128)
        elif color == 'Dark Green':
            self.shape = [[0, 0, 1, 1], [0, 1, 1, 1]]
            self.rgb = (0, 128, 0)
        elif color == 'Dark Blue':
            self.shape = [[1, 1, 1, 1], [1, 0, 0, 0]]
            self.rgb = (0, 0, 128)
        elif color == "Orange":
            self.shape = [[1, 1, 1], [1, 0, 0]]
            self.rgb = (255, 165, 0)
        elif color == "Red":
            self.shape = [[1, 1, 1], [0, 1, 1]]
            self.rgb = (255, 0, 0)
        elif color == "Yellow":
            self.shape = [[1, 0, 1], [1, 1, 1]]
            self.rgb = (255, 255, 0)
        elif color == "Light Green": 
            self.shape = [[1, 1], [1, 1]]
            self.rgb = (0, 255, 0)
        elif color == "White":
            self.shape = [[1, 1], [1, 0]]
            self.rgb = (255, 255, 255)
        elif color == "Gray":
            self.shape = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
            self.rgb = (128, 128, 128)
        elif color == "Light Pink":
            self.shape  = [[1, 1, 1, 1], [0, 1, 0, 0]]
            self.rgb = (255, 192, 203)
        elif color == "Light Blue":
            self.shape = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
            self.rgb = (0, 255, 255)
        elif color == "Dark Pink":
            self.shape = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
            self.rgb = (255, 20, 147)
        
    def rotate(self):
        self.shape = zip(*self.shape[::-1])
    
    def draw(self, screen):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    pygame.draw.rect(screen, self.color, (self.x + j * 20, self.y + i * 20, 20, 20))
                    
                    

# Create list of items where each item is the set of coordinates for a given kanoodle piece where the first index is the center of rotation for the piece
pieces = [[(0,0), (0,-1), (0,-2), (0,1)], # Purple
          [(0,0), (0,-1), (0,-2), (1,-2)], # Dark Green
          ]