import pygame


class Car():
    def __init__(self,screen):
        self.image = pygame.image.load('images/car_blue_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 65))
        self.rect = self.image.get_rect()
        self.x = 750
        self.y = 500
        self.screen = screen
        self.moving_up = False
        self.moving_down = False

    def draw(self):

        intX = int(self.x)
        intY = int(self.y)
        self.rect.center = (intX, intY)
        rot_car = pygame.transform.rotate(self.image, 270)

        rot_rect = rot_car.get_rect(center=self.rect.center)

        self.screen.blit(rot_car, rot_rect)


