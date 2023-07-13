import pygame

class C_BuildNode():
    def __init__(self, x, y, size) -> None:
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.color = pygame.Color(177, 83, 0)
        self.structure = "empty"

class C_MapManager():
    def __init__(self, window_size, screen, player_list):
        self.WINDOW_SIZE = window_size
        self.screen = screen
        self.player_list = player_list
    
    empty_grid = []
    structure_grid = []
   
    def init_building_grid(self):
        node_amount = 60

        size = int(self.WINDOW_SIZE.x / node_amount)
        amount = pygame.Vector2((self.WINDOW_SIZE.x / size), (self.WINDOW_SIZE.y / size))
        self.empty_grid = [[None for _ in range(int(amount.y))] for _ in range(int(amount.x))] #TODO: You dont need a 2d array for this, just keep an normal array because each rect knows its own position
        
        print("Size:" ,size)
        print("Amount", amount.x, " / ", amount.y)
        for i in range(0, int(amount.x)):
            for j in range(0, int(amount.y)):
                self.empty_grid[i][j] = C_BuildNode(i * size, j * size, size)

    def render_build_grid(self):
        #TODO: To save performance on grid nodes which have nothing in them, implement two seperate arrays , usedNodes and unusedNodes
        for node in self.structure_grid:
            if isinstance(node, C_BuildNode) and node.structure != "empty":
                pygame.draw.rect(self.screen, node.color, node.rect, node.size)
    
    def player_build(self):
        mouse_pos = pygame.mouse.get_pos()
        for array in self.empty_grid:
            for node in array:
                if isinstance(node, C_BuildNode) and node.rect.collidepoint(mouse_pos):
                    node.structure = "something"
                    #Check if player is in the way 
                    blocked = False 
                    for player in self.player_list:
                        if pygame.Rect.colliderect(node.rect, player.rect):
                            blocked = True
                            break
                        if not blocked:
                            self.structure_grid.append(node)