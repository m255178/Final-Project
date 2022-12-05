import pygame
import sys
from background import draw_background, TILE_SIZE
from car import Car
from car2 import Car_2
import math
from obstacles import Cones
from walls import Wall
from achievement import Achievement
import random

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

obstacle_group = pygame.sprite.Group()

counter = 0
x = 450
while counter < 5:
    y = random.randint(400,620)
    cone = Cones(screen, 1565,y)
    obstacle_group.add(cone)
    counter = counter + 1




achievement = Achievement(screen)
achievement_group = pygame.sprite.Group()
achievement_group.add(achievement)

# create wall group
wall_group = pygame.sprite.Group()

# create a main group for sprite groups
main_group = pygame.sprite.Group()
# draw horizontal barriers along the track for the cars
for x in range(0, WINDOW_WIDTH, TILE_SIZE):
    for y in (400, 620):
        wall = Wall((x, y))
        wall_group.add(wall)

pygame.mixer.init()
pygame.mixer.music.load('tires.mp3')

font = pygame.font.SysFont('Helvetica', 80)

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
                pygame.mixer.music.play()
            elif event.key == pygame.K_DOWN:
                car.moving_down = True
                pygame.mixer.music.play()
            elif event.key == pygame.K_w:
                car2.moving_up = True
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                car2.moving_down = True
                pygame.mixer.music.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                car.moving_up = False
                pygame.mixer.music.stop()
            elif event.key == pygame.K_DOWN:
                car.moving_down = False
                pygame.mixer.music.stop()
            elif event.key == pygame.K_w:
                car2.moving_up = False
                pygame.mixer.music.stop()
            elif event.key == pygame.K_s:
                car2.moving_down = False
                pygame.mixer.music.stop()

    pygame.display.set_caption("Speedy Car")



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

    for cone in obstacle_group:
        cone.x = cone.x - 10
        cone.draw(screen)

    x -= 1
    clock.tick(60)


    # call update_car()
    car.update(wall_group, obstacle_group, achievement_group)
    car2.update(wall_group, obstacle_group, achievement_group)

    wall_group.draw(screen)

    achievement.draw()
    achievement.update()

    # call the main group
    main_group.add(wall_group)
    main_group.add(obstacle_group)

    if car.x == 0 or car2.x == 0:
        while True:
            screen.fill((0, 81, 255))
            img = font.render(
                f"GAME OVER - Press Q", True, (255, 255, 255))
            img_rect = img.get_rect()
            img_rect.center = screen.get_rect().center
            screen.blit(img, img_rect)
            # draw text on screen
            screen.blit(img, img_rect)
            pygame.display.flip()
            clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

    # update screen

    pygame.display.update()

    pygame.display.flip()
