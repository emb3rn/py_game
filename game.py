import pygame
from random import randint

pygame.init()

#WINDOW_SIZE = pygame.Vector2(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)
WINDOW_SIZE = pygame.Vector2(1500, 1200)
ENTITY_SIZE = 10
#FONT = pygame.font.Font("SegoeUI.ttf")

screen = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))
clock = pygame.time.Clock()
running = True

class C_BuildNode():
    def __init__(self, x, y, size) -> None:
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.color = "blue"
        self.structure = "empty"

class C_Entity():
    def __init__(self, size):
        #TODO: Implement self.x and self.y as float values, which will allow us to use deltaTime and adjust player movement speeds by casting it to int #2
        self.pos = pygame.Vector2(randint(0, WINDOW_SIZE.x), randint(0, WINDOW_SIZE.y))
        #
        self.rect = pygame.Rect(self.pos.x, self.pos.y, size, size)

    def move(self, x, y):
        #TODO: Change the self.pos instead and cast the self.pos to an int, which will allow for float values for the position, hence deltaTime. #2
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

class C_Enemy(C_Entity):
    def __init__(self, size):
        super().__init__(size)
        self.color = "red"

    def move_to_player(self, player):
        smallest_distance = float('inf')
        move_offset = [0, 0]
       
        for x_offset in [-1, 1]:             # Loop through every pixel around the enemy entities, -1 and +1 of their current X
            for y_offset in [-1, 1]:
               
                dist = pygame.Vector2((self.rect.x + x_offset), (self.rect.y + y_offset)).distance_to((player.rect.x, player.rect.y))
                if dist < smallest_distance:

                    smallest_distance = dist
                    move_offset = [x_offset, y_offset] * 2
       
        self.move(move_offset[0], move_offset[1])      

class C_Player(C_Entity):
    def __init__(self, size):
        super().__init__(size)
        self.color = "green"

    def keyboard_move(self, event):
        multi = 20
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

class C_PointerList():
    def __init__(self) -> None:
        self.enemy_list_ptr = 0
        self.player_list_ptr = 0
        self.ent_manager_ptr = 0
        self.player_manager_ptr = 0
   
    #DONE: Add all the pointers to differnet managers in here, so we can easily call manager functions from other managers
    #TODO: Implement usage of this
     
class C_EnemyManager():
    def __init__(self, screen, player_list):
        self.screen = screen
        self.enemy_list = []
        self.player_list = player_list

    def init_enemy(self, amount):
        for x in range(0, amount):
            self.enemy_list.append(C_Enemy(ENTITY_SIZE))

    def render_enemies(self):
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                pygame.draw.rect(screen, entity.color, entity.rect, ENTITY_SIZE)

    def random_movement(self, randomness): #TODO: Remove for loop and call it within the move_to_cursor() func, then run it per entity
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                if entity.rect.x <= WINDOW_SIZE.x - 10 or WINDOW_SIZE.y - 10 <= 720 and (entity.rect.x + entity.rect.y >= 0): #scuffed boundry check
                    entity.move(randint(randomness*-1, randomness), randint(randomness*-1, randomness))

    def move_to_player(self):
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                closest_player = entity.closest_entity(self.player_list)
                entity.move_to_player(closest_player)

class C_PlayerManager():
    def __init__(self):
        self.player_list = []
        self.building_grid = []

    def init_player(self, amount):
        for x in range(0, amount):
           self.player_list.append(C_Player(ENTITY_SIZE))

    def move_players(self, event):
        for player in self.player_list:
            if isinstance(player, C_Player):
                player.keyboard_move(event)
   
    def render_players(self):
        for player in self.player_list:
            if isinstance(player, C_Player):
                pygame.draw.rect(screen, player.color, player.rect, ENTITY_SIZE)

    #TODO: All of this building shit needs to be moved into a GameManager or MapManager

class C_MapManager():
    building_grid = 0
   
    def init_building_grid(self):
        size = int(WINDOW_SIZE.x / 60)
        amount = pygame.Vector2((WINDOW_SIZE.x / size), (WINDOW_SIZE.y / size))
        self.building_grid = [[None for _ in range(int(amount.y))] for _ in range(int(amount.x))]
        
        print("Size:" ,size)
        print("Amount", amount.x, " / ", amount.y)
        for i in range(0, int(amount.x)):
            for j in range(0, int(amount.y)):
                self.building_grid[i][j] = C_BuildNode(i * size, j * size, size)

    def render_build_grid(self):
        #TODO: To save performance on grid nodes which have nothing in them, implement two seperate arrays , usedNodes and unusedNodes
        for array in self.building_grid:
            for node in array:
                if isinstance(node, C_BuildNode) and node.structure != "empty":
                    pygame.draw.rect(screen, node.color, node.rect, node.size)
        
    def player_build(self):
        mouse_pos = pygame.mouse.get_pos()
        for array in self.building_grid:
            for node in array:
                if node.rect.collidepoint(mouse_pos):
                    node.structure = "something"


PlayerManager = C_PlayerManager()
PlayerManager.init_player(1)

MapManager = C_MapManager()
MapManager.init_building_grid()

EnemyManager = C_EnemyManager(screen, PlayerManager.player_list)
EnemyManager.init_enemy(100)

while running == True:
    for current_event in pygame.event.get():
        if current_event.type == pygame.QUIT:
            running = False
       
        if current_event.type == pygame.MOUSEBUTTONUP:
            #TODO: Implement buliding on click here
            print(f"Cursor pos: {pygame.mouse.get_pos()}")
            #MapManager.check_collide(pygame.mouse.get_pos())
       
        if current_event.type == pygame.KEYDOWN:
            #PlayerManager.move_players(current_event)
            pass

    screen.fill("dark green")

    EnemyManager.random_movement(5)
    EnemyManager.move_to_player()
   
    EnemyManager.render_enemies()
    PlayerManager.render_players()
    MapManager.render_build_grid()

    PlayerManager.move_players(pygame.key.get_pressed()) 
    if pygame.mouse.get_pressed()[0]:
        MapManager.player_build()

    pygame.display.flip()
    clock.tick(45)

pygame.quit()