import os
import time
import sys
import pygame
import pygame_gui

from States.Title import Title
from Button import Button


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Poke Egg Guesser")
        self.GAME_W, self.GAME_H = 1600, 900
        self.SCREEN_W, self.SCREEN_H = 1600, 900
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.actions = {"start": False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.load_states()
        
    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing, self.running = False, False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if startButton.enabled == True:
                    # self.actions["start"] = True:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                # if startButton.enabled == False:
                    # self.actions["start"] = False:
                pass

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(
            self.game_canvas, (self.SCREEN_W, self.SCREEN_H)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)
        
    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "MainSprite")
        self.font_dir = os.path.join(self.assets_dir, "Font")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 64)
        self.button_font = pygame.font.Font(os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 20)
        
    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
        
        
if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()
    pygame.quit()