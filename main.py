import pygame
import sys
from hero import Hero

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")

    clock = pygame.time.Clock()
    FPS = 60

    hero = Hero(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hero.moving_right = True
                if event.key == pygame.K_a:
                    hero.moving_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    hero.moving_right = False
                if event.key == pygame.K_a:
                    hero.moving_left = False

        hero.update()

        screen.fill(0)
        hero.output_hero()

        pygame.display.flip()
        clock.tick(FPS)
start_game()