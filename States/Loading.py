import os
import re
import time
import random
import pygame
import pygame_gui
from States.State import State
from States.CensormonGame import CensormonGame

class Loading(State):
    def __init__(self, game, diff):
        # print("Loading init")
        State.__init__(self, game)
        self.diff = diff
        
    def update(self, dt, actions):
        new_state = CensormonGame(self.game, self.diff)
        new_state.enter_state()

    def render(self, display):
        display.fill("#FFF6DE")
        self.game.draw_text(display, "Loading...",
                            "black", self.game.GAME_W/2, self.game.GAME_H/2, self.game.title_font)