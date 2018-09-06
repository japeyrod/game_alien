import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹管理类"""

    def __init__(self, ai_setting, screen, ship):
        """在飞船处创建子弹对象"""

