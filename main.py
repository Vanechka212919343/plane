import pygame, controls
from hero import Hero
from pygame.sprite import Group

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    #background_image = pygame.image.load('images/background.jpg')

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    enemys = Group()

    flag = True
    while flag:
       
        controls.events(screen, hero, bullets)
        hero.moving_hero(screen)
        controls.update(screen, hero, bullets, enemys)
        controls.moving_bullets(screen, bullets)
        controls.create_army(screen, enemys)

        #screen.blit(background_image, (0, 0))
        pygame.display.update()
        clock.tick(60)

        
start_game()