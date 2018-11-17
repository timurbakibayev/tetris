import pygame
import random
def drawfield(a, screen):
    zoom = 30
    for i in range(len(a)):
        for j in range(len(a[i])):
            pygame.draw.rect(screen, ((255,255,255),(0,0,0))[a[i][j]],
                             [j*zoom,i*zoom, zoom, zoom], 0)


def step(a):
    b = a.copy()

    for i in range(len(a)):
        for j in range(len(a[i])):
            k = 0
            if i > 0 and a[i-1][j]:
                k += 1
            if i < len(a)-1 and a[i+1][j]:
                k += 1
            if j > 0 and a[i][j-1]:
                k += 1
            if j < len(a[i])-1 and a[i][j+1]:
                k += 1
            if i > 0 and j > 0 and a[i-1][j-1]:
                k += 1
            if i > 0 and j < len(a[i])-1 and a[i-1][j+1]:
                k += 1
            if i < len(a)-1 and j > 0 and a[i+1][j-1]:
                k += 1
            if i < len(a)-1 and j < len(a[i])-1 and a[i+1][j+1]:
                k += 1

            if k < 2 or k > 3:
                b[i][j] = 0




    return b


if __name__ == '__main__':
    pygame.init()

    size = (400, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Half Life")

    done = False
    clock = pygame.time.Clock()
    x = 1
    fps = 2
    counter = 0

    pressing_down = False

    a = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,1,0,0,0],
            [0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
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
