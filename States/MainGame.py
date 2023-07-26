import os
import random
import pygame
import pygame_gui
from States.State import State


class MainGame(State):

    def __init__(self, game):
        print("MainGame init")
        State.__init__(self, game)
        self.sprites = {}
        for sprite in os.listdir(os.path.join(self.game.sprite_dir)):
            if "_1" in os.path.join(self.game.sprite_dir, sprite):
                continue
            self.sprites[sprite] = pygame.image.load(
                os.path.join(self.game.sprite_dir, sprite))
        # print(self.sprites.keys())

        self.input_w, self.input_h = 500, 50
        self.input_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.input_w/2, 2 * self.game.SCREEN_H/3 - self.input_h/2), (self.input_w, self.input_h)), manager=self.game.UIManager, object_id="input_field")

        self.current_prompt, _ = random.choice(list(self.sprites.items()))
        # print(self.current_prompt)

        self.points = 0
        self.round = 0

    def update(self, dt, actions):
        if actions["text_entry"]:
            if actions["text_entry"].lower() == self.current_prompt.rstrip(".png").lower():
                self.points += 1
            self.round += 1
            self.current_prompt, _ = random.choice(list(self.sprites.items()))
            self.input_field.clear()
            self.input_field.enable()
            self.input_field.focus()
            actions["text_entry"] = ""

    def render(self, display):
        display.fill("#FFF6DE")

        self.game.draw_text(display, "Who's that Pokémon?",
                            "black", self.game.GAME_W/2, self.game.GAME_H/4, self.game.header_font)

        display.blit(self.sprites[self.current_prompt], (self.game.GAME_W/2 - self.sprites[self.current_prompt].get_width(
        )/2, self.game.GAME_H/2 - self.sprites[self.current_prompt].get_height()/2))

        ratio_text = f"{self.points} / {self.round}"
        self.game.draw_text(display, ratio_text,
                            "black", self.game.normal_font.size(ratio_text)[0], self.game.normal_font.size(ratio_text)[0]/2, self.game.normal_font)
