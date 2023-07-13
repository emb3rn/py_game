import pygame
from Entity import C_Entity

class C_Player(C_Entity):
    def __init__(self, size, window_size, building_grid):
        super().__init__(size, window_size)
        self.building_grid = building_grid
        self.color = "green"
    
    def move(self, x, y):
        #TODO: Change the self.pos instead and cast the self.pos to an int, which will allow for float values for the position, hence deltaTime. #2
        if (self.rect.x + x > 0 and self.rect.x + x < self.WINDOW_SIZE.x) and (self.rect.y + y > 0 and self.rect.y + y < self.WINDOW_SIZE.y):
            #Building check. I need to make this more normal somehow 
            moved_rect = self.rect.move(x, y)
            blocked = False
            for node in self.building_grid:
                if pygame.Rect.colliderect(moved_rect, node.rect):
                    blocked = True
                    break
            
            if not blocked:
                self.rect = self.rect.move(x, y)
    
    def keyboard_move(self, event):
        multi = 5
        if event[pygame.K_UP]:
            self.move(0, -1*multi)
        if event[pygame.K_DOWN]:
            self.move(0, 1*multi)
        if event[pygame.K_LEFT]:
            self.move(-1*multi, 0)
        if event[pygame.K_RIGHT]:
            self.move(1*multi, 0)

    def build(self, mouse_pos, structure):
        if structure == "wall":
            pass