import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        # upload image for barriers
        self.image = pygame.image.load('images/barrier_white.png')
        self.image = pygame.transform.scale(self.image, (128, 5))
        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def draw(self, screen):
        # draw them on the screen
        screen.blit(self.image, self.rect)
