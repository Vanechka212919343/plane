import pygame

class Hero():
    def __init__(self, screen):
        #This code snippet is defining a constructor (__init__) for a class. 
        # It calls the parent class's constructor using super().__init__().
        #  It then loads an image file called "hero.png" using the Pygame library and assigns it to the image attribute.
        #  Finally, it gets the rectangle of the image and assigns it to the rect attribute.
        self.image = pygame.image.load("images/hero.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.x = self.screen_rect.centerx

    def output_hero(self):
        self.screen.blit(self.image, self.rect)