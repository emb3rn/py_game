import pygame
from PlayerManager import C_PlayerManager
from MapManager import C_MapManager
from EnemyManager import C_EnemyManager

pygame.init()

# WINDOW_SIZE = pygame.Vector2(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)
WINDOW_SIZE = pygame.Vector2(1500, 1200)
ENTITY_SIZE = 10
# FONT = pygame.font.Font("SegoeUI.ttf")

screen = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))
clock = pygame.time.Clock()
running = True

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
            # TODO: Implement buliding on click here
            print(f"Cursor pos: {pygame.mouse.get_pos()}")
            # MapManager.check_collide(pygame.mouse.get_pos())

        if current_event.type == pygame.KEYDOWN:
            # PlayerManager.move_players(current_event)
            pass

    screen.fill("dark green")

    EnemyManager.random_movement(2)
    EnemyManager.move_to_player(MapManager.structure_grid)

    EnemyManager.render_enemies()
    PlayerManager.render_players()
    MapManager.render_build_grid()

    PlayerManager.move_players(pygame.key.get_pressed())

    if pygame.mouse.get_pressed()[0]:
        MapManager.player_build()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
