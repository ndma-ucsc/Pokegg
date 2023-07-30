import pygame
import pygame_gui
from States.State import State
from States.EggGame import EggGame
from States.CensormonSettings import CensormonSettings

class Title(State):
    def __init__(self, game):
        # print("Title init")
        State.__init__(self, game)

        # Create start buttons
        self.egg_start_btn_w, self.egg_start_btn_h = 310, 50
        self.censor_start_btn_w, self.censor_start_btn_h = 310, 50
        
        self.egg_start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.egg_start_btn_w/2, 2 * self.game.SCREEN_H/3), (self.egg_start_btn_w, self.egg_start_btn_h)), manager=self.game.UIManager, object_id="egg_start_btn", text="Egg Guesser")
        self.censor_start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.censor_start_btn_w/2, 2.3 * self.game.SCREEN_H/3), (self.censor_start_btn_w, self.censor_start_btn_h)), manager=self.game.UIManager, object_id="censor_start_btn", text="Censormon")

    def update(self, dt, actions):
        
        # On Button
        if actions["egg_start"] or actions["censor_start"]:
            self.egg_start_btn.hide()
            self.censor_start_btn.hide()

            # Start Egg Game
            if actions["egg_start"]:
                # Egg Game transition
                actions["egg_start"] = False
                new_state = EggGame(self.game)
                new_state.enter_state()
            
            # Start Censormon Settings
            elif actions["censor_start"]:
                # Censor Game transition
                actions["censor_start"] = False
                new_state = CensormonSettings(self.game)
                new_state.enter_state()

        self.game.reset_keys()

    def render(self, display):
        display.fill("#FFF6DE")
        self.game.draw_text(display, "Poké Egg Guesser",
                            "black", self.game.GAME_W/2, self.game.GAME_H/2, self.game.title_font)
