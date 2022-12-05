import pygame


class Achievement(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        # upload the image
        self.screen = screen
        self.image = pygame.image.load('images/barrel_blue.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def draw(self):
        intX = int(self.x)
        intY = int(self.y)
        self.rect.topright = (intX, intY)
        self.screen.blit(self.image, self.rect)


