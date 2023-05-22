import pygame
from pygame.locals import *
from Tiles import Tile
screen = width, hight = (800, 800)
pygame.init()
screen = pygame.display.set_mode((screen))
pygame.display.set_caption("bounce queen")
screen.fill((95, 234, 250))
pygame.display.update()
freddy = pygame.image.load('Freddie-Mercury-hoofd.png')
freddy_loc = freddy.get_rect()
freddy_loc.center = width/2
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(freddy, freddy_loc)
    pygame.display.update()
    pygame.display.flip()
