import os
import re
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
        self.SCREEN_W, self.SCREEN_H = 1280, 720
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.UIManager = pygame_gui.UIManager((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.actions = {"egg_start": False, "censor_start": False,
                        "text_entry": "a", "skipping": False, "next": False, "next_field": False,
                        "easy_btn": False, "medium_btn": False, "hard_btn": False,
                        "enter": False}
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
                if event.key == pygame.K_SPACE:
                    self.actions["enter"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.actions["enter"] = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     self.actions["start"] = True
            # if event.type == pygame.MOUSEBUTTONUP:
            #     self.actions["start"] = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "egg_start_btn":
                self.actions["egg_start"] = True
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "input_field":
                self.actions["text_entry"] = re.sub(r'\W+', '', event.text)
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "skip_button":
                self.actions["skipping"] = True
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "next_button":
                self.actions["next"] = True
            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == "hidden_field":
                self.actions["next_field"] = True

            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "censor_start_btn":
                self.actions["censor_start"] = True
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "easy_btn":
                self.actions["easy_btn"] = True
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "medium_btn":
                self.actions["medium_btn"] = True
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "hard_btn":
                self.actions["hard_btn"] = True

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
        pygame.display.update()

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
        self.egg_sprite_dir = os.path.join(self.assets_dir, "EggSprite")
        self.pkmn_sprite_dir = os.path.join(
            self.assets_dir, "PkmnSprite")
        self.font_dir = os.path.join(self.assets_dir, "Font")
        self.title_font = pygame.font.Font(
            os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 64)
        self.header_font = pygame.font.Font(
            os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 32)
        self.normal_font = pygame.font.Font(
            os.path.join(self.font_dir, "PKMN RBYGSC.ttf"), 16)

        self.themes_dir = os.path.join(self.assets_dir, "Themes")
        self.UIManager.get_theme().load_theme(
            os.path.join(self.themes_dir, "button.json"))

        # Load sprites to dict
        self.pkmn_sprites = {}

        for sprite in os.listdir(self.pkmn_sprite_dir):
            # self.pkmn_sprites["".join(sprite.split())] = pygame.image.load(
            #     os.path.join(self.pkmn_sprite_dir, sprite))
            self.pkmn_sprites["".join(sprite.split())] = pygame.transform.scale(pygame.image.load(
                os.path.join(self.pkmn_sprite_dir, sprite)), (200, 200))


    def load_states(self):

        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False


game = Game()
asyncio.run(game.game_loop())
pygame.quit()
