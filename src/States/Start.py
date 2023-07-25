class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
    def run(self):
        print("Entered State: Start")
        self.display.fil("blue")