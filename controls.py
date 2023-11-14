import pygame
import sys
from bullet import Bullet
from enemy import Enemy

def events(screen, hero, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.move_right = True
            if event.key == pygame.K_LEFT:
                hero.move_left = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, hero)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero.move_right = False
            if event.key == pygame.K_LEFT:
                hero.move_left = False

def update(screen, hero, enemys, bullets):
    screen.fill(0)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.output_hero()
    enemys.draw(screen)
    pygame.display.flip()


def update_bullets(screen, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_enemys(enemys):
    enemys.update()


def create_army(screen, enemys):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((600 - 2 * enemy_width) / enemy_width)
    for enemy_num in range(number_enemy_x):
        enemy = Enemy(screen)
        enemy.x = enemy_width + enemy_width * enemy_num
        enemy.rect.x = enemy.x
        enemys.add(enemy)