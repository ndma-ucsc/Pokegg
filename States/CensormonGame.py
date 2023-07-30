import os
import re
from PIL import Image
import random
import pygame
import pygame_gui
from States.State import State


class CensormonGame(State):

    def __init__(self, game, diff):
        # print("EggGame init")
        State.__init__(self, game)
    
        
        # print(self.sprites.keys())
        
        self.sprites = {}
        self.correct_sprite = self.game.pkmn_sprites
        diffs = [16, 10, 8]
        for sprite in os.listdir(self.game.pkmn_sprite_dir):
            # self.pkmn_sprites["".join(sprite.split())] = pygame.image.load(
            #     os.path.join(self.game.pkmn_sprite_dir, sprite))
            sprite_img = Image.open(os.path.join(self.game.pkmn_sprite_dir, sprite))
            pixelate_img = sprite_img.resize((diffs[diff], diffs[diff]), resample=Image.Resampling.BILINEAR).resize(sprite_img.size, Image.Resampling.NEAREST).save("./assets/temp/temp.png")
            self.sprites["".join(sprite.split())] = pygame.transform.scale(pygame.image.load("./assets/temp/temp.png"), (200, 200))

        # Text field
        self.input_w, self.input_h = 500, 50
        self.input_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.input_w/2, 2 * self.game.SCREEN_H/3 - self.input_h/2), (self.input_w, self.input_h)), manager=self.game.UIManager, object_id="input_field")

        # Skip Button
        self.skip_b_w, self.skip_b_h = 150, 50
        skip_button = pygame.Rect((self.game.SCREEN_W/2 + self.input_w / 2, 2 *
                                  self.game.SCREEN_H/3 - self.input_h/2), (self.skip_b_w, self.skip_b_h))
        self.skip_button = pygame_gui.elements.UIButton(
            relative_rect=skip_button, manager=self.game.UIManager, object_id="skip_button", text="Skip")

        self.next_b_w, self.next_b_h = 150, 50
        next_button = pygame.Rect((self.game.SCREEN_W/2 + self.input_w / 2, 2 *
                                  self.game.SCREEN_H/3 - self.input_h/2), (self.next_b_w, self.next_b_h))
        self.next_button = pygame_gui.elements.UIButton(
            relative_rect=next_button, manager=self.game.UIManager, object_id="next_button", text="Next")
        self.next_button.hide()

        # Prep first prompt
        self.current_prompt, _ = random.choice(list(self.sprites.items()))
        # print(self.current_prompt)

        self.points = 0
        self.round = 0

        self.prompt_text = "Who's that Pokémon?"
        self.default_prompt_text = "Who's that Pokémon?"
        
        self.reveal = False

    def update(self, dt, actions):

        self.default_prompt_text = "Who's that Pokémon?"

        # Text field catch
        if actions["text_entry"]:
            self.skip_button.hide()
            self.next_button.show()
            self.input_field.clear()
            self.input_field.disable()
            self.reveal = True
            # Correct answer
            if "".join(actions["text_entry"].lower().split()) == self.current_prompt.replace(".png", "").lower():

                self.prompt_text = f"Correct!"

                if actions["next"] or actions["enter"]:
                    self.next_button.hide()
                    self.skip_button.show()
                    self.prompt_text = self.default_prompt_text

                    self.points += 1
                    self.round += 1
                    self.sprites.pop(self.current_prompt)
                    self.current_prompt, _ = random.choice(
                        list(self.sprites.items()))
                    self.input_field.enable()
                    self.input_field.focus()
                    actions["text_entry"] = ""
                    actions["next"] = False
                    self.reveal = False


            # Wrong answer
            else:
                self.prompt_text = f"Correct answer was " + \
                    self.current_prompt.replace(".png","").title()

                if actions["next"] or actions["enter"]:
                    self.next_button.hide()
                    self.skip_button.show()
                    self.prompt_text = self.default_prompt_text

                    self.round += 1
                    self.sprites.pop(self.current_prompt)
                    self.current_prompt, _ = random.choice(
                        list(self.sprites.items()))
                    self.input_field.enable()
                    self.input_field.focus()
                    actions["text_entry"] = ""
                    actions["next"] = False
                    self.reveal = False
                    

        # Skip button catch
        elif actions["skipping"]:
            self.skip_button.hide()
            self.next_button.show()
            self.input_field.clear()
            self.input_field.disable()
            self.reveal = True
            
            self.prompt_text = f"Correct answer was " + self.current_prompt.replace(".png", "").title()

            if actions["next"] or actions["enter"]:
                self.next_button.hide()
                self.skip_button.show()
                self.prompt_text = self.default_prompt_text

                self.round += 1
                self.sprites.pop(self.current_prompt)
                self.current_prompt, _ = random.choice(
                    list(self.sprites.items()))
                self.input_field.enable()
                self.input_field.focus()
                actions["text_entry"] = ""
                actions["next"] = False
                actions["skipping"] = False
                self.reveal = False
                

    def render(self, display):
        display.fill("#FFF6DE")

        self.game.draw_text(display, self.prompt_text,
                            "black", self.game.GAME_W/2, self.game.GAME_H/4, self.game.header_font)

        if not self.reveal:
            display.blit(self.sprites[self.current_prompt], (self.game.GAME_W/2 - self.sprites[self.current_prompt].get_width(
            )/2, self.game.GAME_H/2 - self.sprites[self.current_prompt].get_height()/2))
        else:
            display.blit(self.correct_sprite[self.current_prompt], (self.game.GAME_W/2 - self.correct_sprite[self.current_prompt].get_width(
            )/2, self.game.GAME_H/2 - self.correct_sprite[self.current_prompt].get_height()/2))

        ratio_text = f"{self.points} / {self.round}"
        self.game.draw_text(display, ratio_text,
                            "black", self.game.normal_font.size(ratio_text)[0], self.game.normal_font.size(ratio_text)[0]/2, self.game.normal_font)
