import pygame
from pygame.surface import Surface
from color import Color

class Captcha_button:
    def __init__(self, screen, img, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.selected = False

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def toggle(self):
        self.selected = not self.selected

    def render(self):
        self.screen.blit(self.image, self.rect)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            hover_overlay = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            hover_overlay.fill((0, 0, 0, 60))
            self.screen.blit(hover_overlay, self.rect)

        if self.selected:
            pygame.draw.rect(self.screen, (0, 120, 255), self.rect, 4)