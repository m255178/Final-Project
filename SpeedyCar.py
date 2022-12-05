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

# make a group for obstacles
obstacle_group = pygame.sprite.Group()

# make a bunch of cones using a counter with random x and y positions
counter = 0
x = 450
while counter < 50:
    x = random.randint(1560, 10000)
    y = random.randint(400, 620)
    cone = Cones(screen, x, y)
    obstacle_group.add(cone)
    counter = counter + 1

# make a group for achievements
achievement_group = pygame.sprite.Group()
# make achievements using counter with random x and y positions
while counter < 100:
    x = random.randint(1560, 10000)
    y = random.randint(400, 620)
    achievement = Achievement(screen, x, y)
    achievement_group.add(achievement)
    counter = counter + 1

# create wall group
wall_group = pygame.sprite.Group()

# create a main group for sprite groups

# draw horizontal barriers along the track for the cars
for x in range(0, WINDOW_WIDTH, TILE_SIZE):
    for y in (400, 620):
        wall = Wall((x, y))
        wall_group.add(wall)

# initialize music for tire screeches
pygame.mixer.init()
pygame.mixer.music.load('tires.mp3')

# set a font for the game over page
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
            # up and down arrows for moving blue car up and down
            elif event.key == pygame.K_UP:
                car.moving_up = True
                pygame.mixer.music.play()
            elif event.key == pygame.K_DOWN:
                car.moving_down = True
                pygame.mixer.music.play()
            # w and s keys for moving red car up and down
            elif event.key == pygame.K_w:
                car2.moving_up = True
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                car2.moving_down = True
                pygame.mixer.music.play()
        # make sure the cars stop moving when buttons are released
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

    # window caption
    pygame.display.set_caption("Speedy Car")

    # use a clock tick for the speed of background movement and obstacle movement
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

    # call car.update() to check for collisions and to move car up and down
    car.update(wall_group, obstacle_group, achievement_group)
    car2.update(wall_group, obstacle_group, achievement_group)

    # draw barriers
    wall_group.draw(screen)

    # draw the cones using a for loop
    for cone in obstacle_group:
        cone.x = cone.x - 10
        cone.draw()

    # draw the achievments using a for loop
    for achievement in achievement_group:
        achievement.x = achievement.x - 10
        achievement.draw()

    # this is for counting for loops
    x -= 1


    # game over page if car 1 or car 2 gets to the end of the track
    if car.x == 0 or car2.x == 0:
        while True:
            # set up a screen
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
            # press q or the X to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

    # update screen

    pygame.display.update()

    # flip the display
    pygame.display.flip()
