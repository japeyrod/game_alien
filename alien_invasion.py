import sys
import pygame

from settings import Settings


def run_game():
    #init
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.scrennt_width, settings.scrennt_height))
    pygame.display.set_caption("Alien Invasion")

    #循环
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)

        pygame.display.flip()


run_game()
