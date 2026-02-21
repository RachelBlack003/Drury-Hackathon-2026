import pygame
from pygame.surface import Surface
from color import Color

class Button:
    def __init__(self, screen, text, x, y, size, padding=10, font_color = (0,0,0), bg_color = (240,240,240)):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.padding = padding
        self.color = font_color
        self.bg_color = bg_color

        self.font = pygame.font.Font(pygame.font.get_default_font(), size)
        self.font_surface = self.font.render(text, True, font_color)

        self.text_rect = self.font_surface.get_rect(center=(x, y))
        self.button_rect = self.text_rect.inflate(padding * 2, padding * 2)

    def is_selected(self, mouse_pos):
        return self.button_rect.collidepoint(mouse_pos)

    def render(self):
        mouse_pos = pygame.mouse.get_pos()
        color = tuple(int(col/1.15) for col in self.bg_color) if self.button_rect.collidepoint(mouse_pos) else self.bg_color
        pygame.draw.rect(self.screen, color, self.button_rect)
        self.screen.blit(self.font_surface, self.text_rect)