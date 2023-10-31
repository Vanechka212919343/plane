import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, hero):
        super(Bullet, self).__init__()
        self.rect = pygame.Rect(0,0,4,12)
        self.color = 255, 206, 38
        self.speed=5.0
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top= hero.rect.top
        self.y = float(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y