import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # init
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建游戏按钮
    play_button = Button(settings, screen, "Play")
    #创建用于存储游戏信息的实例
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen)
    # alien = Alien(settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    # 循环
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            # print(len(bullets))
            gf.update_aliens(settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(settings, screen, stats, sb, ship, bullets, aliens, play_button)


run_game()
