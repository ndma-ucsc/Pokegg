from States.State import State

class Title(State):
    def __init__(self, game):
        State.__init__(self,game)
        
    def update(self, dt):
        pass
    
    def render(self, display):
        display.fill(("#FFF6DE"))
        self.game.draw_text(display, "Poke Egg Guesser", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)