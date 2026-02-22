import pygame
from button import Button
from text_handler import Question_Text_handler
from textbox import Textbox

class Preference:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.done = False
        self.soft_done = False
        self.font = pygame.font.SysFont(None, 40)

        self.Burnt_Sienna = Button(
            screen = self.screen,
            text = "Burnt Sienna", 
            x= 200,
            y = 230, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (233, 116, 81)
        )

        self.Smaragdine = Button(
            screen = self.screen,
            text = "  Smaragdine  ", 
            x= 600,
            y = 230, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (74, 153, 118)
        )
        self.Banan_appeal = Button(
            screen = self.screen,
            text = "Banan-appeal", 
            x= 600,
            y = 380, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (252,235,183)
        )
        self.Blue = Button(
            screen = self.screen,
            text = "       Blue        ", 
            x= 200,
            y = 380, 
            size = 50,
            padding=15,
            font_color= (255,255,255),
            bg_color= (255,255,255)
        )
        self.Pass = Button(
            screen = self.screen,
            text = "Pass", 
            x= 700,
            y = 465, 
            size = 30,
            padding=15,
            font_color= (0,0,0),
            bg_color= (230,230,230)
        )

        self.Text_handler = Question_Text_handler("preference")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next()
                if _continue:
                    self.Textbox.update_text(text)
                elif self.Text_handler.is_final_text():
                    self.done = True
                    self.is_done()
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.soft_done:
            if self.Smaragdine.is_selected(event.pos):
                self.lose()
            if self.Banan_appeal.is_selected(event.pos):
                self.lose()
            if self.Blue.is_selected(event.pos):
                self.lose()
            if self.Burnt_Sienna.is_selected(event.pos):
                self.lose()
                self.is_done()
            if self.Pass.is_selected(event.pos):
                self.win()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

    def win(self):
        self.soft_done = True
        self.Text_handler.win()
        self.Textbox.update_text(self.Text_handler.get_text())

    def lose(self):
        self.soft_done = False
        self.Text_handler.lose()
        self.Textbox.update_text(self.Text_handler.get_text())

    def update(self, dt):
        pass

    def draw(self, screen):
        if not self.Text_handler.is_active():
            self.Smaragdine.render()
            self.Burnt_Sienna.render()
            self.Banan_appeal.render()
            self.Blue.render()
            self.Pass.render()
        self.Textbox.render()

    def is_done(self):
        return self.done