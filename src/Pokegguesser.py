import sys
import pygame
import pygame_gui

from GameStateManager import GameStateManager
from States.Title import Title
from States.MainGame import MainGame

SCREEN_W, SCREEN_H = 1280, 720
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.UIManager = pygame_gui.UIManager((SCREEN_W, SCREEN_H))

        self.gameStateManager = GameStateManager("mainGame")
        self.title_state = Title(self.screen, self.gameStateManager, self.UIManager)
        self.mainGame_state = MainGame(self.screen, self.gameStateManager, self.UIManager)

        # All states
        self.states = {"title_state": self.title_state,
                       "mainGame": self.mainGame_state}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
