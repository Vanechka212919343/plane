import pygame, controls
from hero import Hero
from pygame.sprite import Group

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((700, 1000))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.jpg')

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    inosogradosmexicanos = Group()

    flag = True
    while flag:
        screen.blit(background_image, (0, 0))
        pygame.display.update()
        clock.tick(60)
        controls.events(screen, hero, bullets) 
        hero.moving_hero(screen)
        controls.update(screen, hero, bullets)
        controls.update_bullets(screen, hero, bullets)
        controls.create_army(screen)
       
 
start_game()