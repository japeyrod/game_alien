import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #init
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.scrennt_width, settings.scrennt_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #循环
    while True:



        screen.fill(settings.bg_color)

        ship.blitme()

        pygame.display.flip()


run_game()
