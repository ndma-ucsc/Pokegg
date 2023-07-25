import os
import time
import sys
import pygame
import pygame_gui


class Game():
    def __init__(self):
        pygame.init()
        self.GAME_W, self.GAME_H = 1600, 900
        self.SCREEN_W, self.SCREEN_H = 1600, 900
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        
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

    def update(self):
        pass

    def render(self):
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
        
        
        
if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()