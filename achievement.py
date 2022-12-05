import pygame
from random import randint, choice

class Achievement(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.sprite_type = 'obstacle'


        self.screen = screen
        self.image = pygame.image.load('images/barrel_blue.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        # mask
        self.mask = pygame.mask.from_surface(self.image)

        self.x = 1536
        self.y = randint(400, 610)
        self.cone_drop_speed = 10
        self.moving_left = True

    def draw(self):
        intX = int(self.x)
        intY = int(self.y)
        self.rect.topright = (intX, intY)
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= self.cone_drop_speed
            self.x -= self.cone_drop_speed
