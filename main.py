import pygame, controls
from hero import Hero
from pygame.sprite import Group
from stats import Stats

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((700, 1000))
    pygame.display.set_caption("Space Invaders")
    #background_image = pygame.transform.scale(pygame.image.load("path/to/background/image.png"), (700, 1000))

    

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

        controls.update(screen, hero, enemys, bullets)
        controls.update_bullets(screen, bullets, enemys)
        controls.update_enemys(hero, stats, screen, bullets, enemys)
        

start_game()





