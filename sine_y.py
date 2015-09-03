# let's play with curves.

# we will need the math module for trigonometry functions.
import math
# we will use pygame for the purposes of displaying simple graphics.
import pygame
from pygame.locals import *
# (pygame.locals is a collectiong of constants, like the names of keys e.g. K_SPACE for the spacebar.)

# set some constants.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_COLOR = (255, 255, 255)
AMPLITUDE = 100 #amplitude of sine wave produced by sin().
FREQUENCY = math.pi/2

# initialize pygame.
pygame.init()

# we will render a circle with a point acting as the centre.
px = 0.0 # initial value for the point's x
py = SCREEN_HEIGHT/2.0 # initial value for he point's y

# create a window.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# create a clock.
clock = pygame.time.Clock()

# boolean for when to stop.
stop = False

# we're going to clear the screen BEFORE the main loop so that each new blit of the point will leave a trail.
screen.fill((0,0,0))
# we're also going to add horizontal lines at SCREEN_HEIGHT/2+AMPLITUDE, SCREEN_HEIGHT/2, and SCREEN_HEIGHT/2-AMPLITUDE
LINE_COLOR = (0, 0, 255)
start_posx = 0
end_posx = SCREEN_WIDTH
posy = (SCREEN_HEIGHT/2)-AMPLITUDE
pygame.draw.line(screen, LINE_COLOR, (start_posx, posy), (end_posx, posy))
posy = (SCREEN_HEIGHT/2)
pygame.draw.line(screen, LINE_COLOR, (start_posx, posy), (end_posx, posy))
posy = (SCREEN_HEIGHT/2)+AMPLITUDE
pygame.draw.line(screen, LINE_COLOR, (start_posx, posy), (end_posx, posy))
# main loop

phase = 1 # phase is a value that is going to range from 1 to 360, and it's going to control the point's height.
          # the values 1 to 360 are because i'm going to use the sin() function, which takes radians, whith i will
          # convert from degrees.
x, y = px, py # the values we will be changing are not the same as the values we initially set
              # TODO: are they then constants? might require a style change

while (not stop):
    # render first, then input, then update.
    # render here.
    clock.tick(60)
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(x), int(y)), 1) # draw the point.
    pygame.display.update()

    # handle input here.
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                stop = True
        if event.type == QUIT:
            stop = True
    # if escape is pressed or the X is clicked, stop is set to True.
    if stop:
        break # if stop is set to true, we break the loop.

    # update values here.
    phase += FREQUENCY
    if phase > 360:
        phase = phase-360
    x += 1
    if x > SCREEN_WIDTH:
        x = 0
    y = py+math.sin(math.radians(phase))*AMPLITUDE

# when the loop falls through, we quit pygame and end the program.
pygame.quit()

