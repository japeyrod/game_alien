import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bulllets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bulllets)

def check_keyup_events(event, ai_settings, screen, ship, bulllets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bulllets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bulllets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bulllets)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹位置，删除屏幕外子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bulllets):
    if len(bulllets) < ai_settings.bullets_allow:
        new_bullet = Bullet(ai_settings, screen, ship)
        bulllets.add(new_bullet)

