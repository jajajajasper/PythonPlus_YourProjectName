import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect(topleft= pos)