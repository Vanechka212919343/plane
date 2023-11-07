import pygame

class enemy(object):
    def __init__(self, screen):
        super(enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        

    def output_enemy(self):
        self.screen.blit(self.image, self.rect)

    def moving_enemy(self):
        self.y+=0.1
        self.rect.y=self.y
        for bullet in bullet.copy():
            if bullet.rect.bottom <= 0:
                bullet.remove(bullet)

    def create_army(screen):
        for i in range(50):
            enemy = Enemy(screen)
            enemy_width = enemy.rect.width

            num_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
            for i in range(num_enemy_x):
                enemy = Enemy(screen)
                enemy.x = enemy_width + enemy_width * i
                enemy.rect.x = enemy.x
                enemys.add(enemy)
            
           
