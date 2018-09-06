import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    #init
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.scrennt_width, settings.scrennt_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)

    #循环
    while True:

        gf.check_events(ship)

        ship.update()

        gf.update_screen(settings, screen, ship)


run_game()
