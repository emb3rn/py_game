import pygame
from random import randint

pygame.init()

WINDOW_SIZE = pygame.Vector2(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)
ENTITY_SIZE = 20

screen = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))
clock = pygame.time.Clock()
running = True

class C_Entity():
    def __init__(self, size):
        self.rect = pygame.Rect(randint(0, WINDOW_SIZE.x), randint(0, WINDOW_SIZE.y), size, size)

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

class C_Enemy(C_Entity):
    def __init__(self, size):
        super().__init__(size)
        self.color = "red"

    def move_to_cursor(self):
        smallest_distance = 99999999 
        move_offset = [0, 0]
        
        for x_offset in [-1, 1]:             ## Loop through every pixel around the enemy entities, -1 and +1 of their current X
            for y_offset in [-1, 1]:
                
                dist = pygame.Vector2((self.rect.x + x_offset), (self.rect.y + y_offset)).distance_to(pygame.mouse.get_pos())
                if dist < smallest_distance:
                    smallest_distance = dist
                    move_offset = [x_offset, y_offset] * 2
        
        self.move(move_offset[0], move_offset[1])       

class C_Player(C_Entity):
    def __init__(self, size):
        super().__init__(size)
        self.color = "green"

    def keyboard_move(self, event):
        multi = 40
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move(0, -1*multi)
            if event.key == pygame.K_DOWN:
                self.move(0, 1*multi)
            if event.key == pygame.K_LEFT:
                self.move(-1*multi, 0)
            if event.key == pygame.K_RIGHT:
                self.move(1*multi, 0)

class C_PointerList():
    pass #TODO: Add all the pointers to differnet managers in here, so we can easily call manager functions from other managers

class C_EntityManager():
    def __init__(self, screen):
        self.screen = screen
        self.entity_list = []
        self.player_list = []

    def init_enemy(self, amount):
        for x in range(0, amount):
            self.entity_list.append(C_Enemy(ENTITY_SIZE))

    def render_enemies(self):
        for entity in self.entity_list:
            if isinstance(entity, C_Enemy):
                pygame.draw.rect(screen, entity.color, entity.rect, ENTITY_SIZE)

    def random_movement(self, randomness): #TODO: Remove for loop and call it within the move_to_cursor() func, then run it per entity
        for entity in self.entity_list:
            if isinstance(entity, C_Enemy):
                if entity.rect.x <= WINDOW_SIZE.x - 10 or WINDOW_SIZE.y - 10 <= 720 and (entity.rect.x + entity.rect.y >= 0): #scuffed boundry check
                    entity.move(randint(randomness*-1, randomness), randint(randomness*-1, randomness))

    def move_to_cursor(self):
        for entity in self.entity_list:
            if isinstance(entity, C_Enemy):
                entity.move_to_cursor()


class C_PlayerManager():
    def __init__(self):
        self.player_list = []

    def init_player(self):
       self.player_list.append(C_Player(ENTITY_SIZE)) 

    def move_players(self, event):
        for player in self.player_list:
            if isinstance(player, C_Player):
                player.keyboard_move(event)
    
    def render_players(self):
        for player in self.player_list:
            if isinstance(player, C_Player):
                pygame.draw.rect(screen, player.color, player.rect, ENTITY_SIZE)

EntityManager = C_EntityManager(screen)
PlayerManager = C_PlayerManager()
EntityManager.init_enemy(100)
PlayerManager.init_player()

while running == True:
    for current_event in pygame.event.get():
        if current_event.type == pygame.QUIT:
            running = False
       
        if current_event.type == pygame.MOUSEBUTTONUP:
            # THIS IS GOING TO HAVE BUILDING FOR WHEN THE PLAYER CLICKS
            print(f"Cursor pos: {pygame.mouse.get_pos()}")
        
        if current_event.type == pygame.KEYDOWN:
            PlayerManager.move_players(current_event)
            
    screen.fill("black")

    EntityManager.random_movement(5)
    EntityManager.move_to_cursor()
    EntityManager.render_enemies()
    PlayerManager.render_players()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()