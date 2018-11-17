import pygame
import random

def show(a):
    print("----")
    for i in a:
        print(i)

def drawfield(a, screen):
    zoom = 30
    for i in range(len(a)):
        for j in range(len(a[i])):
            pygame.draw.rect(screen, ((255,255,255),(0,0,0))[a[i][j]],
                             [j*zoom,i*zoom, zoom, zoom], 0)


def around(a):
    a = a.copy()
    empty_line = [[0 for i in range(len(a[0])+2)]]
    for i in range(len(a)): a[i] = [0] + a[i] + [0]
    return empty_line+a+empty_line

def something(q,b):
    for i in range(1,len(q)-1):
        for j in range(1,len(q[i])-1):
            k = - q[i][j] + sum([q[y][x] for y in range(i-1, i+2) for x in range(j-1,j+2)])
            if k < 2 or k > 3: b[i-1][j-1] = 0
            if k == 3: b[i-1][j-1] = 1

def step(a):
    b = a.copy()
    q = around(a.copy())
    something(q,b)
    return b


if __name__ == '__main__':
    pygame.init()

    size = (500, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Half Life")

    done = False
    clock = pygame.time.Clock()
    fps = 2
    counter = 0

    pressing_down = False

    a = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,1,0,1,1,0,0,0],
            [0,1,1,0,1,1,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,1,0,1,0,0,0,0],
            [0,0,1,0,1,0,0,0,0],
            [0,0,1,0,1,0,0,0,0],
        ]

    # Loop as long as done == False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        screen.fill((255,255,255))
        a = step(a)
        drawfield(a, screen)
        # Select the font to use, size, bold, italics

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
