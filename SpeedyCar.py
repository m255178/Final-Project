import pygame
import sys
from background import draw_background, TILE_SIZE


pygame.init()


WINDOW_WIDTH = 12 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    sys.exit()

    pygame.display.set_caption("Speedy Car")

    screen.blit(bg, bg.get_rect())



    pygame.display.flip()




