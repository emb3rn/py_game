import pygame
from Entity import C_Entity

class C_Player(C_Entity):
    def __init__(self, size):
        super().__init__(size)
        self.color = "green"

    def keyboard_move(self, event):
        multi = 5
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