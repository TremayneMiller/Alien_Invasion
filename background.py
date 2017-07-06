import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, image, top = 0, left = 0):
        Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
