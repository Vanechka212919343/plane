import pygame
import sys

def start_game():
    #основна функция для описания игры
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Самая гут игра")

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag=False
                sys.exit()


start_game()