import os
import pygame
from States.State import State


class MainGame(State):

    def __init__(self, game):
        State.__init__(self, game)
        self.sprites = {}
        for sprite in os.listdir(os.path.join(self.game.sprite_dir)):
            self.sprites[sprite] = pygame.image.load(os.path.join(self.game.sprite_dir, sprite))

    def update(self, dt, actions):
        pass
    
    
    def render(self, display):
        display.fill("#FFF6DE")
        display.blit(self.sprites["ABRA.png"], (0,0))