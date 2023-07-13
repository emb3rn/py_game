import pygame
from random import randint
class C_Entity():
    def __init__(self, size, window_size):
        self.WINDOW_SIZE = window_size
        #TODO: Implement self.x and self.y as float values, which will allow us to use deltaTime and adjust player movement speeds by casting it to int #2
        self.pos = pygame.Vector2(randint(0, self.WINDOW_SIZE.x), randint(0, self.WINDOW_SIZE.y))
        #
        self.rect = pygame.Rect(self.pos.x, self.pos.y, size, size)

    def move(self, x, y):
        #TODO: Change the self.pos instead and cast the self.pos to an int, which will allow for float values for the position, hence deltaTime. #2
        if (self.rect.x + x > 0 and self.rect.x + x < self.WINDOW_SIZE.x) and (self.rect.y + y > 0 and self.rect.y + y < self.WINDOW_SIZE.y):
            self.rect = self.rect.move(x, y)
   
    def closest_entity(self, ent_list):
        smallest_distance = float('inf')
        smallest_ent = 0

        for entity in ent_list:
            if isinstance(entity, C_Entity):
                dist = pygame.Vector2(self.rect.x, self.rect.y).distance_to((entity.rect.x, entity.rect.y))
                if dist < smallest_distance:
                    smallest_distance = dist
                    smallest_ent = entity
       
        return smallest_ent