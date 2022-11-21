import pygame
import sys
from background import draw_background, TILE_SIZE
from car import Car

pygame.init()

WINDOW_WIDTH = 12 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))

car = Car(screen)


def redraw_window():
    screen.blit(bg, (bgX, 0))  # draws our first bg image
    pygame.display.update()  # updates the screen


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
    bgX = -500
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()

    redraw_window()


    pygame.display.set_caption("Speedy Car")

    screen.blit(bg, bg.get_rect())

    car.draw()

    pygame.display.flip()
