import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #生成位置,左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """准确绘制"""
        self.screen.blit(self.image, self.rect)
