import pygame
import sys
from hero import Hero
from pygame.locals import *

def start_game():
    #основна функция для описания игры
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Самая гут игра")
    bg_color = (255,255,255)
    screen.fill(bg_color)
    pygame.display.flip()


    
    #объекты классов
    hero = Hero(screen)

    flag = True
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.rect.y -= 10
                elif event.key == pygame.K_s:
                    hero.rect.y += 10
                elif event.key == pygame.K_a:
                    hero.rect.x -= 10
                elif event.key == pygame.K_d:
                    hero.rect.x += 10
            

        pygame.display.flip()
        screen.fill((0,0,0))
        hero.output_hero()

start_game()
       