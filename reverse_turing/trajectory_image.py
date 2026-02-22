import pygame
from pygame.surface import Surface

class Trajectory_image:
    def __init__(self, screen, img, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))


    def render(self):
        self.screen.blit(self.image, self.rect)