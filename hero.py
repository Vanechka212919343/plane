import pygame
import sys


class Hero:
    def __init__(self, screen):
        self.image = pygame.image.load("images/hero.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.speed = 5
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.speed
        if self.moving_left:
            self.rect.centerx -= self.speed
            
        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def output_hero(self):
        self.screen.blit(self.image, self.rect)