import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, hero):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 77, 109, 243
        self.speed = 4.5
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top
        self.y = float(self.rect.y)

    def draw_bullet(self):
        '''отрисовка пуль через спрайты'''
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y