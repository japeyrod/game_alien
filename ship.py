import pygame


class Ship():

    def __init__(self, screen):
        """初始化初始位置"""
        self.screen = screen

        #加载图像，外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #设置到底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)