import pygame
from settings import *
from pygame.locals import *

size = width, height
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("bounce queen")
screen.fill((95, 234, 250))
pygame.display.update()
done = False

fred = pygame.image.load("fred.png")
fred = pygame.transform.scale(fred, (89,107))
fred_loc = fred.get_rect()
fred_loc.center = width/2, height*0.8
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(fred, fred_loc)
    pygame.display.update()
pygame.quit()