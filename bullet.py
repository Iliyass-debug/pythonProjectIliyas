import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, pushka):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = (130, 190, 50)
        self.speed = 1.5
        self.rect.centerx = pushka.rect.centerx
        self.rect.top = pushka.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)