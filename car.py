import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # upload the image
        self.image = pygame.image.load('images/car_blue_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 65))
        self.rect = self.image.get_rect()
        # set x and y so that the car starts in the middle of the window
        self.x = 750
        self.y = 500
        self.screen = screen
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        # set x and y for where car starts
        intX = int(self.x)
        intY = int(self.y)
        self.rect.center = (intX, intY)
        # rotate the car so it is facing right
        rot_car = pygame.transform.rotate(self.image, 270)

        rot_rect = rot_car.get_rect(center=self.rect.center)
        # blit the car
        self.screen.blit(rot_car, rot_rect)
        if self.x == 1400:
            self.draw()

    def update(self, wall_group, obstacle_group, achievement_group):
        # move the car up and down
        if self.moving_up:
            self.y -= 7
        if self.moving_down:
            self.y += 7

        # check to see if the car collides with the wall, obstacles, or achievements
        if pygame.sprite.spritecollide(self, wall_group, False):
            # go back to the old rectangle
            self.x -= 5
        if pygame.sprite.spritecollide(self, obstacle_group, False):
            self.x -= 10
        if pygame.sprite.spritecollide(self, achievement_group, False):
            self.x += 10

