import pygame
from button import Button
from textbox import Textbox

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
            y = 250, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (233, 116, 81)
        )

        self.Smaragdine = Button(
            screen = self.screen,
            text = "  Smaragdine  ", 
            x= 600,
            y = 250, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (74, 153, 118)
        )
        self.Banan_appeal = Button(
            screen = self.screen,
            text = "Banan-appeal", 
            x= 600,
            y = 400, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (252,235,183)
        )
        self.Blue = Button(
            screen = self.screen,
            text = "       Blue        ", 
            x= 200,
            y = 400, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (255,255,255)
        )
        self.Pass = Button(
            screen = self.screen,
            text = "Pass", 
            x= 700,
            y = 495, 
            size = 30,
            padding=15,
            font_color= (0,0,0),
            bg_color= (230,230,230)
        )

        self.textBox = Textbox(
            screen=self.screen,
            text="Select your favorite color.",
            y=550
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.Smaragdine.is_selected(event.pos):
                self.done = True
                self.is_done()
            if self.Banan_appeal.is_selected(event.pos):
                self.done = True
                self.is_done()
            if self.Blue.is_selected(event.pos):
                self.done = True
                self.is_done()
            if self.Burnt_Sienna.is_selected(event.pos):
                self.done = True
                self.is_done()
            if self.Pass.is_selected(event.pos):
                self.done = True
                self.is_done()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

    def update(self, dt):
        pass

    def draw(self, screen):
        self.Smaragdine.render()
        self.Burnt_Sienna.render()
        self.Banan_appeal.render()
        self.Blue.render()
        self.Pass.render()
        self.textBox.render()

    def is_done(self):
        return self.done