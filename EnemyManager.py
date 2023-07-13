import pygame
from random import randint
from Enemy import C_Enemy

class C_EnemyManager():
    def __init__(self, screen, entity_size, player_list, window_size):
        self.screen = screen
        self.ENTITY_SIZE = entity_size
        self.enemy_list = []
        self.player_list = player_list
        self.WINDOW_SIZE = window_size


    def init_enemy(self, amount):
        for x in range(0, amount):
            self.enemy_list.append(C_Enemy(self.ENTITY_SIZE, self.WINDOW_SIZE))

    def render_enemies(self):
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                pygame.draw.rect(self.screen, entity.color, entity.rect, self.ENTITY_SIZE)

    def random_movement(self, randomness): #TODO: Remove for loop and call it within the move_to_cursor() func, then run it per entity
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                entity.move(randint(randomness*-1, randomness), randint(randomness*-1, randomness))

    def move_to_player(self, building_arr):
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                closest_player = entity.closest_entity(self.player_list)
                entity.move_to_player(closest_player, building_arr) 