import pygame
from Entity import C_Entity

class C_Enemy(C_Entity):
    def __init__(self, size):
        super().__init__(size)
        self.color = "red"

    def move_to_player(self, player, structure_array):
        smallest_distance = float('inf')
        move_offset = [0, 0]
       
        for x_offset in [-1, 1]:             # Loop through every pixel around the enemy entities, -1 and +1 of their current X
            for y_offset in [-1, 1]:
                moved_rect = self.rect.move(x_offset, y_offset)
                blocked = False
                for node in structure_array:
                    if pygame.Rect.colliderect(moved_rect, node.rect):
                        blocked = True
                        break

                if not blocked: 
                    dist = pygame.Vector2((self.rect.x + x_offset), (self.rect.y + y_offset)).distance_to((player.rect.x, player.rect.y))
                    if dist < smallest_distance:
                        smallest_distance = dist
                        move_offset = [x_offset, y_offset] * 2
        
        self.move(move_offset[0], move_offset[1])      
