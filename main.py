import os
import sys
import time
import asyncio
import pygame
import pygame_gui

from States.Title import Title


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Poké Egg Guesser")
        self.GAME_W, self.GAME_H = 1280, 720
        self.SCREEN_W, self.SCREEN_H = 1600, 900
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.UIManager = pygame_gui.UIManager((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.actions = {"start": False, "text_entry": "a"}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.load_states()

    async def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            await asyncio.sleep(0)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing, self.running = False, False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.actions["start"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.actions["start"] = False
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "input_field":
                self.actions["text_entry"] = event.text

            self.UIManager.process_events(event)

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)
        self.UIManager.update(pygame.time.Clock().tick(60)/1000)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(
            self.game_canvas, (self.SCREEN_W, self.SCREEN_H)), (0, 0))
        self.UIManager.draw_ui(self.screen)
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, color, x, y, font):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "MainSprite")
        self.font_dir = os.path.join(self.assets_dir, "Font")
        self.title_font = pygame.font.Font(
            os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 64)
        self.header_font = pygame.font.Font(
            os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 32)
        self.normal_font = pygame.font.Font(
            os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 16)

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

def main():
    game = Game()
    while game.running:
        asyncio.run(game.game_loop())
    pygame.quit()

if __name__ == "__main__":
    main()