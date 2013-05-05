#!/usr/bin/env python

import pygame
import time
from pygame.locals import *

joysticks = []
keyboard = True # if true, creates a capture window so keyboard events can be caught too

LEFT = "turnleft"
RIGHT = "turnright"
ACCEL = "accelerate"
BREAK = "stopaccelerate"
STRAIGHT = "stopturning"


def init():
    pygame.init()
    global joysticks
    global keyboard
    if keyboard:
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Capture window')
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()

def events():
    while True:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 273:  # accelerate
                    yield ACCEL
                elif event.key == 276:  # left
                    yield LEFT
                elif event.key == 275:  # right
                    yield RIGHT
            elif event.type == KEYUP:
                if event.key == 273:  # accelerate
                    yield BREAK
                elif event.key == 276:  # left
                    yield STRAIGHT
                elif event.key == 275:  # right
                    yield STRAIGHT
            elif event.type == JOYAXISMOTION:
                if event.axis == 0:
                    if event.value <= -0.2:
                        yield LEFT
                    elif event.value >= 0.2:
                        yield RIGHT
                    elif -0.2 < event.value < 0.2:
                        yield STRAIGHT
            elif event.type == JOYBUTTONDOWN:
                if event.button == 0:  # accelerate
                    yield ACCEL
                elif event.button == 1:  # break
                    yield BREAK
            elif event.type == JOYBUTTONUP:
                if event.button == 0:  # accelerate
                    yield BREAK

if __name__ == "__main__":
    init()
    for i in events():
        print(i)
