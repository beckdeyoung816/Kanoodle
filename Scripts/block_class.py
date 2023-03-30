import pygame
## Write a class for a tetris block
class block():
    def __init__(self, color):
        # self.x = x
        # self.y = y
        self.color = color
        
        if color == 'Purple':
            self.shape = [[1, 1, 1, 1]]
            self.coords = [(0, 0), (1, 0), (2, 0), (3, 0)]
            self.rgb = (128, 0, 128)
        elif color == 'Dark Green':
            self.shape = [[0, 0, 1, 1], 
                          [1, 1, 1]]
            self.coords = [(2,1), (3,1),
                           (0, 0), (1, 0), (2, 0)]
            self.rgb = (0, 128, 0)
        elif color == 'Dark Blue':
            self.shape = [[1, 0, 0, 0], 
                          [1, 1, 1, 1]]
            self.coords = [(0, 1), 
                           (0, 0), (1, 0), (2, 0), (3, 0)]
            self.rgb = (0, 0, 128)
        elif color == "Orange":
            self.shape = [[1, 0, 0], 
                          [1, 1, 1]]
            self.coords = [(0, 1), 
                           (0, 0), (1, 0), (2, 0)]
            self.rgb = (255, 165, 0)
        elif color == "Red":
            self.shape = [[0, 1, 1], 
                          [1, 1, 1]]
            self.coords = [(1, 1), (2, 1), 
                           (0, 0), (1, 0), (2, 0)]
            self.rgb = (255, 0, 0)
        elif color == "Yellow":
            self.shape = [[1, 0, 1], 
                          [1, 1, 1]]
            self.coords = [(0, 1), (2, 1), 
                           (0, 0), (1, 0), (2, 0)]
            self.rgb = (255, 255, 0)
        elif color == "Light Green": 
            self.shape = [[1, 1], 
                          [1, 1]]
            self.coords = [(0, 1), (1, 1), 
                           (0, 0), (1, 0)]
            self.rgb = (0, 255, 0)
        elif color == "White":
            self.shape = [[1, 1], 
                          [1, 0]]
            self.coords = [(0, 1), (1, 1),
                            (0, 0)]
            self.rgb = (255, 255, 255)
        elif color == "Gray":
            self.shape = [[0, 1, 0], 
                          [1, 1, 1], 
                          [0, 1, 0]]
            self.coords = [(1, 2), 
                           (0, 1), (1, 1), (2, 1),
                           (1, 0)]
            self.rgb = (128, 128, 128)
        elif color == "Light Pink":
            self.shape  = [[0, 1, 0, 0], 
                           [1, 1, 1, 1]]
            self.coords = [(0, 1), 
                           (0, 0), (1, 0), (2, 0), (3, 0)]
            self.rgb = (255, 192, 203)
        elif color == "Light Blue":
            self.shape = [[1, 0, 0], 
                          [1, 0, 0], 
                          [1, 1, 1]]
            self.coords = [(0, 2),
                           (0, 1),
                           (0, 0), (1, 0), (2, 0)]
            self.rgb = (0, 255, 255)
        elif color == "Dark Pink":
            self.shape = [[1, 0, 0], 
                          [1, 1, 0], 
                          [0, 1, 1]]
            self.coords = [(0, 2),
                           (0, 1), (1, 1),
                           (1, 0), (2, 0)]
            self.rgb = (255, 20, 147)
        
        # Define Rectangles for shape
        self.rects = [pygame.Rect(x, y, 1, 1) for x,y in self.coords]
        
    def rotate(self):
        self.shape = zip(*self.shape[::-1])
    
    def draw(self, screen):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    pygame.draw.rect(screen, self.color, (self.x + j * 20, self.y + i * 20, 20, 20))
                    
                    

