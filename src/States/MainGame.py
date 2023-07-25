import os
import pygame
import pygame_gui


class MainGame:
    def __init__(self, display, gameStateManager, UIManager):
        print("Loaded State: MainGame")
        self.display = display
        self.display.fill(pygame.Color("#DDFBDF"))
        self.screen_size_w = self.display.get_width()
        self.screen_size_h = self.display.get_height()
        
        self.gameStateManager = gameStateManager
        self.UIManager = UIManager
        
        self.asset_path = "assets\MainSprite"
        asset_list = os.listdir(self.asset_path)
        self.assets = {}
        for a in asset_list:
            self.assets[a] = pygame.image.load(f"{self.asset_path}\{a}")

    def run(self):
        usr_txt = ""

        # self.display.blit(
        #     self.assets["ABRA.png"], (self.screen_size_w/2 - self.assets["ABRA.png"].get_width()/2, self.screen_size_h/ - self.assets["ABRA.png"].get_height()/2))
