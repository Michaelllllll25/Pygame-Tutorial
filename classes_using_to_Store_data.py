# pygame
"""
Create a Ball class to store x, y location and speed 
Get ball to move
Created many balls
Get balls to bounce off the side of the window
"""

import random
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

class Ball:
    def __init__(self, x: int, y: int, dx: int, dy: int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        r = random.randrange(0, 256)  # - 255
        g = random.randrange(0, 256)  # - 255
        b = random.randrange(0, 256)  # - 255
        self.color = (r, g, b) # (0, 0, 0)




pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#-------------------------------
# Initialize global variables
#           x | y | dx | dy
balls = [
    Ball(50, 50, 5, 1),
    Ball(100, 200, 5, 2),
    Ball(80, 88, -3, 3)
]

for _ in range(10):       # gen 10 balls
    x = random.randrange(0, WIDTH)    # 0 - WIDTH
    y = random.randrange(0, HEIGHT)
    dx = random.randrange(-5, 5)
    dy = random.randrange(-5, 5)
    b = Ball(x, y, dx, dy)
    balls.append(b)

#-------------------------------

running = True
while running:
    # EVEN HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    for ball in balls:
        if ball.x > WIDTH or ball.x < 0:
            ball.dx *= -1  # if speed is positive and hits wall reverse speed

        # ADD Y-AXIS CHECK
        # Account for the radius (the balls get clipped)
        #       - Create a radius attribute in the Ball class
        #       - Randomize radius for each

        ball.x += ball.dx     # speed
        ball.y += ball.dy     # ^^^^^




    # DRAWING
    screen.fill((255, 255, 255))        # always the first drawing command

    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), 30)

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)

    #----------------------------


pygame.quit()
