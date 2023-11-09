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

def update(screen, hero, bullets, enemys):
    screen.fill(0)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.output_hero()
    enemys.update()
    pygame.display.flip()

def moving_bullets(screen, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen,enemys):
    enemy = Enemy(screen)
    enemy_wight = enemy.rect.width

    num_enemy_x = int((600 - 2*enemy_wight) / enemy_wight)
    for i in range(num_enemy_x):
        enemy = Enemy(screen)
        enemy.x = enemy_wight + enemy_wight * i
        enemy.rect.x = enemy.x
        enemys.add(enemy)
