import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """单击开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #重置记分牌等
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bulllets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bulllets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bulllets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bulllets)

def update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()

    if stats.game_active:
        aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除子弹新建外星人
        bullets.empty()
        ai_settings.increase_speed()

        #升级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹位置，删除屏幕外子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bulllets):
    if len(bulllets) < ai_settings.bullets_allow:
        new_bullet = Bullet(ai_settings, screen, ship)
        bulllets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    # number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    number_aliens_x = 4
    number_rows = 1
    for row_number in range(number_rows):
        # 第一行外星人
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行容纳多少外星人"""
    # 间距为外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """常见一个外星人并放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测外星人和飞创碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """响应外星人撞到飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """检测外星人是否到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """检查最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
    sb.prep_high_score()
