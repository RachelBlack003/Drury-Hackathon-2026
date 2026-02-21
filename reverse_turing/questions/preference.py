import pygame
from button import Button

class Preference:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.done = False
        self.font = pygame.font.SysFont(None, 40)

        self.Burnt_Sienna = Button(
            screen = self.screen,
            text = "Burnt Sienna", 
            x= 200,
            y = 200, 
            size = 40,
            padding=15,
            font_color= (255,255,255),
            bg_color= (233, 116, 81)
        )

        self.Smaragdine = Button(
            screen = self.screen,
            text = "  Smaragdine  ", 
            x= 600,
            y = 200, 
            size = 40,
            padding=15,
            font_color= (255,255,255),
            bg_color= (74, 153, 118)
        )
        self.Banan_appeal = Button(
            screen = self.screen,
            text = "Banan-appeal", 
            x= 600,
            y = 400, 
            size = 40,
            padding=15,
            font_color= (255,255,255),
            bg_color= (252,235,183)
        )
        self.Blue = Button(
            screen = self.screen,
            text = "       Blue        ", 
            x= 200,
            y = 400, 
            size = 40,
            padding=15,
            font_color= (255,255,255),
            bg_color= (255,255,255)
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

    def update(self, dt):
        pass

    def draw(self, screen):
        text = self.font.render("Preference", True, (255,255,255))
        screen.blit(text, (250, 300))
        self.Smaragdine.render()
        self.Burnt_Sienna.render()
        self.Banan_appeal.render()
        self.Blue.render()

    def is_done(self):
        return self.done