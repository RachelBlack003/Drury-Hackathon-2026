import pygame
from pygame.surface import Surface
from color import Color

class Button:
    def __init__(self, screen, text, x, y, size, padding=10):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.padding = padding

        self.font = pygame.font.Font(pygame.font.get_default_font(), size)
        self.font_surface = self.font.render(text, True, (0, 0, 0))

        self.text_rect = self.font_surface.get_rect(center=(x, y))
        self.button_rect = self.text_rect.inflate(padding * 2, padding * 2)

    def is_selected(self, mouse_pos):
        return self.button_rect.collidepoint(mouse_pos)

    def render(self):
        mouse_pos = pygame.mouse.get_pos()
        color = (200, 200, 200) if self.button_rect.collidepoint(mouse_pos) else (223, 223, 223)
        pygame.draw.rect(self.screen, color, self.button_rect)
        self.screen.blit(self.font_surface, self.text_rect)