from States.State import State
from States.MainGame import MainGame


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, dt, actions):
        if actions["start"]:
            new_state = MainGame(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill(("#FFF6DE"))
        self.game.draw_text(display, "Poke Egg Guesser",
                            "black", self.game.GAME_W/2, self.game.GAME_H/2)
