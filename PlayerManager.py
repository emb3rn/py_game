import pygame
from Player import C_Player

class C_PlayerManager():
    def __init__(self, screen, entity_size):
        self.screen = screen
        self.ENTITY_SIZE = entity_size
        self.player_list = []
        self.building_grid = []

    def init_player(self, amount):
        for x in range(0, amount):
           self.player_list.append(C_Player(self.ENTITY_SIZE))

    def move_players(self, event):
        for player in self.player_list:
            if isinstance(player, C_Player):
                player.keyboard_move(event)
   
    def render_players(self):
        for player in self.player_list:
            if isinstance(player, C_Player):
                pygame.draw.rect(self.screen, player.color, player.rect, self.ENTITY_SIZE)

    #TODO: All of this building shit needs to be moved into a GameManager or MapManager

