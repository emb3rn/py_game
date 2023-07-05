import pygame
from Enemy import C_Enemy

class C_EnemyManager():
    def __init__(self, screen, entity_size, player_list):
        self.screen = screen
        self.ENTITY_SIZE = entity_size
        self.enemy_list = []
        self.player_list = player_list

    def init_enemy(self, amount):
        for x in range(0, amount):
            self.enemy_list.append(C_Enemy(self.ENTITY_SIZE))

    def render_enemies(self):
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                pygame.draw.rect(screen, entity.color, entity.rect, self.ENTITY_SIZE)

    def random_movement(self, randomness): #TODO: Remove for loop and call it within the move_to_cursor() func, then run it per entity
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                if entity.rect.x <= WINDOW_SIZE.x - 10 or WINDOW_SIZE.y - 10 <= 720 and (entity.rect.x + entity.rect.y >= 0): #scuffed boundry check
                    entity.move(randint(randomness*-1, randomness), randint(randomness*-1, randomness))

    def move_to_player(self, building_arr):
        for entity in self.enemy_list:
            if isinstance(entity, C_Enemy):
                closest_player = entity.closest_entity(self.player_list)
                entity.move_to_player(closest_player, building_arr)