import pygame


class Button():

    def __init__(self, game, text, x, y, w, h, enabled):
        self.game = game
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = self.game.button_font.render(self.text, True, "black")
        button_rect = pygame.rect.Rect((self.x,self.y), (self.w,self.h))
        pygame.draw.rect(self.game.screen, "white", button_rect, 0, 3)
        pygame.draw.rect(self.game.screen, "black", button_rect, 2, 3)
        self.game.screen.blit(button_text, (self.x/2 - len(self.text)/2, self.y/2 - 20))