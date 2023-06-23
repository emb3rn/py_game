import pygame
import random

WINDOW_SIZE = pygame.Vector2(2000, 1500)

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))
clock = pygame.time.Clock()
running = True

entity_list = []

class C_Entity():
    def __init__(self, size):
        self.rect = pygame.Rect(random.randint(100, 1200), random.randint(100, 700), size, size)

    def move(self):
        pass

class C_EntityManager():
    def __init__(self, screen, ent_list):
        self.screen = screen
        self.entity_list = ent_list

    def init_enemy(self, amount):
        for x in range(0, amount):
            self.entity_list.append(C_Entity(20))

    def render_entities(self):
        for entity in self.entity_list:
            if isinstance(entity, C_Entity):
                pygame.draw.rect(screen, "red", entity.rect, 20)

    def move_entites(self, randomness):
        for entity in self.entity_list:
            if isinstance(entity, C_Entity):
                if entity.rect.x <= WINDOW_SIZE.x - 10 or WINDOW_SIZE.y - 10 <= 720 and (entity.rect.x + entity.rect.y >= 0): #scuffed boundry check
                    entity.rect = entity.rect.move(random.randint(randomness*-1, randomness), random.randint(randomness*-1, randomness))

    def move_to_cursor(self):
        for entity in self.entity_list:
            if isinstance(entity, C_Entity):
                smallest_distance = 99999999 
                move_offset = [0, 0]
                
                for x_offset in [-1, 1]:             ## Loop through every pixel around the enemy entities, -1 and +1 of their current X
                    for y_offset in [-1, 1]:
                        
                        dist = pygame.Vector2((entity.rect.x + x_offset), (entity.rect.y + y_offset)).distance_to(pygame.mouse.get_pos())
                        if dist < smallest_distance:
                            smallest_distance = dist
                            move_offset = [x_offset, y_offset] * 2
                
                entity.rect = entity.rect.move(move_offset[0], move_offset[1])

EntityManager = C_EntityManager(screen, entity_list)
EntityManager.init_enemy(100)
print(EntityManager.entity_list)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    EntityManager.move_entites(5)
    EntityManager.move_to_cursor()
    EntityManager.render_entities()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()