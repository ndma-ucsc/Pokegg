import pygame
import sys

from GameStateManager import GameStateManager
from States.Start import Start

SCREEN_W, SCREEN_H = 1280,720
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager()
        self.start = Start(self.screen, self.gameStateManager)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            self.clock.tick(FPS)
            

if __name__ == "__main__":
    game = Game()
    game.run()