import pygame
import pygame_gui
from States.State import State
from States.MainGame import MainGame


class Title(State):
    def __init__(self, game):
        # print("Title init")
        State.__init__(self, game)

        # Create Start Button
        self.start_b_w, self.start_b_h = 200, 50
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
            (self.game.SCREEN_W/2 - self.start_b_w/2, 2 * self.game.SCREEN_H/3), (self.start_b_w, self.start_b_h)), manager=self.game.UIManager, object_id="start_button", text="Start")

    def update(self, dt, actions):
        # On Start button press
        if actions["start"]:
            self.start_button.hide()

            # State transition
            new_state = MainGame(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill(("#FFF6DE"))
        self.game.draw_text(display, "Poké Egg Guesser",
                            "black", self.game.GAME_W/2, self.game.GAME_H/2, self.game.title_font)
