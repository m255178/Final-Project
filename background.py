import pygame
import os


grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    ]

TILE_SIZE = 128

# 0 is grass, 1 is grass/dirt, 2 is topside of track, 3 is bottom side of track, 4 is stands
grass = pygame.image.load(os.path.join('images/land_grass11.png'))
grass_dirt = pygame.image.load(os.path.join('images/land_grass13.png'))
track1 = pygame.image.load(os.path.join('images/road_asphalt04.png'))
track2 = pygame.image.load(os.path.join('images/road_asphalt40.png'))
stands = pygame.image.load(os.path.join('images/tribune_full.png'))
stands = pygame.transform.scale(stands, (128,128))

ground = [grass, grass_dirt, track1, track2, stands]

def draw_background(bg_size):
    bg = pygame.Surface(bg_size)
    for r, grid_list in enumerate(grid):
        for c, grid_element in enumerate(grid_list):
            bg.blit(ground[grid_element], (c * TILE_SIZE, r * TILE_SIZE))
    return bg


