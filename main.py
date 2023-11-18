import pygame, controls
from hero import Hero
from pygame.sprite import Group
from stats import Stats

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((700, 900))
    pygame.display.set_caption("Space Invaders")
    background=pygame.image.load("images/background.jpg")

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    enemys = Group()
    controls.create_army(screen,enemys)
    stats = Stats()

    flag = True
    while flag:
        controls.events(screen, hero, bullets)
        hero.moving_hero(screen)

        controls.update(screen,background, hero, enemys, bullets)
        controls.update_bullets(screen, bullets, enemys)
        controls.update_enemys(hero, stats, screen, bullets, enemys)
        

start_game()





