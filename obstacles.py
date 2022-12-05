import pygame
from random import randint, choice

class Cones(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        self.sprite_type = 'obstacle'


        self.screen = screen
        self.image = pygame.image.load('images/cone_straight.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        # mask
        self.mask = pygame.mask.from_surface(self.image)

        self.x = x
        self.y = y
        self.cone_drop_speed = 10
        self.moving_left = True

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        if self.moving_left:
            self.rect.x -= self.cone_drop_speed
            self.x -= self.cone_drop_speed


