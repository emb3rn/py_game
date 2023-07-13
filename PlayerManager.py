import pygame
from Player import C_Player

class C_PlayerManager():
    def __init__(self, screen, entity_size, window_size, building_grid):
        self.screen = screen
        self.ENTITY_SIZE = entity_size
        self.WINDOW_SIZE = window_size
        self.building_grid = building_grid
        self.player_list = []

    def init_player(self, amount):
        for x in range(0, amount):
           self.player_list.append(C_Player(self.ENTITY_SIZE, self.WINDOW_SIZE, self.building_grid))

    def move_players(self, event):
        for player in self.player_list:
            if isinstance(player, C_Player):
                player.keyboard_move(event)
   
    def render_players(self):
        for player in self.player_list:
            if isinstance(player, C_Player):
                pygame.draw.rect(self.screen, player.color, player.rect, self.ENTITY_SIZE)

    #TODO: All of this building shit needs to be moved into a GameManager or MapManager

