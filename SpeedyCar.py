import pygame
import sys
from background import draw_background, TILE_SIZE
from car import Car
from car2 import Car_2
import math
from obstacles import Cones

# initialize the game
pygame.init()

# set window dimensions
WINDOW_WIDTH = 12 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

# draw background
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))
# make the background move
tiles = math.ceil(WINDOW_WIDTH / bg.get_width()) + 1
scroll = 0

# instance of cars
car = Car(screen)
car2 = Car_2(screen)

# timer for scrolling background
clock = pygame.time.Clock()

cone = Cones(screen)

# main game loop
while True:

    # key events for quitting game and moving car
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_UP:
                car.moving_up = True
            elif event.key == pygame.K_DOWN:
                car.moving_down = True
            elif event.key == pygame.K_w:
                car2.moving_up = True
            elif event.key == pygame.K_s:
                car2.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                car.moving_up = False
            elif event.key == pygame.K_DOWN:
                car.moving_down = False
            elif event.key == pygame.K_w:
                car2.moving_up = False
            elif event.key == pygame.K_s:
                car2.moving_down = False

    pygame.display.set_caption("Speedy Car")

    clock.tick(40)

    # scrolling the screen constantly
    i = 0
    while i < tiles:
        screen.blit(bg, (bg.get_width() * i + scroll, 0))
        i += 1
    scroll -= 10
    if abs(scroll) > bg.get_width():
        scroll = 0

    # draw cars
    car.draw()
    car2.draw()

    # call move_car()
    car.move_car()
    car2.move_car()

    cone.draw()
    cone.moving_left = True

    # update screen
    pygame.display.update()

    pygame.display.flip()
