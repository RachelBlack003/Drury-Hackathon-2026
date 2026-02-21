
import pygame
from pygame.surface import Surface
from pygame.event import Event



class UI:
    def __init__(self, screen: Surface):
        self.screen: Surface = screen

    def handle_input(self, event: Event):
        pass