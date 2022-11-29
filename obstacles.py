import pygame
from pygame.sprite import Sprite


class Cones():
    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('images/cone_straight.png')
        self.rect = self.image.get_rect()

        self.x = 1536
        self.y = 512
        self.cone_drop_speed = 5
        self.moving_left = True


    def draw(self):

        intX = int(self.x)
        intY = int(self.y)
        self.rect.center = (intX, intY)

        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.x -= 1
