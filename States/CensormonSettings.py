import os
import re
import time
import random
import pygame
import pygame_gui
from States.State import State
from States.Loading import Loading

class CensormonSettings(State):
    
    def __init__(self, game):
        # print("CensormonSettings init")
        State.__init__(self, game)
        
        self.censor_start_btn_w, self.censor_start_btn_h = 310, 50

        self.easy_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.censor_start_btn_w/2, self.game.SCREEN_H/3), (self.censor_start_btn_w, self.censor_start_btn_h)), manager=self.game.UIManager, object_id="easy_btn", text="Easy")
        self.medium_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.censor_start_btn_w/2, 1.5 * self.game.SCREEN_H/3), (self.censor_start_btn_w, self.censor_start_btn_h)), manager=self.game.UIManager, object_id="medium_btn", text="Medium")
        self.hard_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.censor_start_btn_w/2, 2 * self.game.SCREEN_H/3), (self.censor_start_btn_w, self.censor_start_btn_h)), manager=self.game.UIManager, object_id="hard_btn", text="Hard")

        
    def update(self, dt, actions):
        # On Button
        if actions["easy_btn"] or actions["medium_btn"] or actions["hard_btn"]:
            self.easy_btn.hide()
            self.medium_btn.hide()
            self.hard_btn.hide()
            
            # Start Censormon
            if actions["easy_btn"]:
                # Censormon Game transition
                actions["easy_btn"] = False
                new_state = Loading(self.game,0)
                new_state.enter_state()

            if actions["medium_btn"]:
                # Censormon Game transition
                actions["medium_btn"] = False
                new_state = Loading(self.game,1)
                new_state.enter_state()
                
            if actions["hard_btn"]:
                # Censormon Game transition
                actions["hard_btn"] = False
                new_state = Loading(self.game,2)
                new_state.enter_state()

        self.game.reset_keys()

    def render(self, display):
        display.fill("#FFF6DE")
        self.game.draw_text(display, "Pick a difficulty",
                            "black", self.game.GAME_W/2, self.game.GAME_H/4, self.game.header_font)
