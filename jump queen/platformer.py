import pygame, sys
from settings import *
from Tiles import Tile

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100,100),200))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 255))
    test_tile.draw(screen)
    pygame.display.update()



    clock.tick(60)