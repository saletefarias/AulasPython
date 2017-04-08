#! /usr/bin/env python
import pygame, sys
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()


screen = pygame.display.set_mode((956, 560), 0, 32)

background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

ship_filename = 'ship.png'
ship = pygame.image.load(ship_filename).convert_alpha()
ship_position = [randrange(956), randrange(560)]

pygame.display.set_caption('Hello World')

clock = pygame.time.Clock()
while True:
    speed = {
        'x': 0,
        'y': 0
    }
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        speed['y'] = -5
    elif pressed_keys[K_DOWN]:
        speed['y'] = 5
    if pressed_keys[K_LEFT]:
        speed['x'] = -5
    elif pressed_keys[K_RIGHT]:
        speed['x'] = 5
    screen.blit(background, (0, 0))
    ship_position[0] += speed['x']
    ship_position[1] += speed['y']
    screen.blit(ship, ship_position)
    pygame.display.update()
    time_passed = clock.tick(30)
