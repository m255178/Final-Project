import pygame
import sys
from background import draw_background, TILE_SIZE
from car import Car
import math

pygame.init()

WINDOW_WIDTH = 12 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))
tiles = math.ceil(WINDOW_WIDTH / bg.get_width()) + 1
scroll = 0

car = Car(screen)

clock = pygame.time.Clock()




while True:

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                car.moving_up = False
            elif event.key == pygame.K_DOWN:
                car.moving_down = False
        print(event)


    pygame.display.set_caption("Speedy Car")


    clock.tick(33)

    i = 0
    while i < tiles:
        screen.blit(bg, (bg.get_width()*i + scroll, 0))
        i += 1
    scroll -= 10
    if abs(scroll) > bg.get_width():
        scroll = 0

    pygame.display.update()

    car.draw()
    car.move_car()
    pygame.display.flip()
