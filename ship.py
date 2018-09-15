import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            if self.center < self.ai_settings.screen_width:
                self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            if self.center > 0:
                self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        """居中"""
        self.center = self.screen_rect.centerx