import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien


def run_game():
    # init
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.scrennt_width, settings.scrennt_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(settings, screen)
    alien = Alien(settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, aliens)

    # 循环
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        gf.update_screen(settings, screen, ship, bullets, alien)


run_game()
