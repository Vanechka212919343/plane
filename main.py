import pygame
import sys
from hero import Hero

def start_game():
    #основна функция для описания игры
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption( "Space Invaders")
    clock = pygame.time.Clock()


    
    #объекты классов
    hero = Hero(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hero.move_left = True
                if event.key == pygame.K_d:
                    hero.move_right = True
                if event.key == pygame.K_a:
                    hero.move_left = False
                if event.key == pygame.K_d:
                    hero.move_right = False
        
            

        screen.fill(0)
        hero.output_hero()
        pygame.display.flip() 
        hero.update_moving()
        

start_game()
       