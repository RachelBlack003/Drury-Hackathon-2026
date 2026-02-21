import pygame
from ui import UI

from typing import Optional
from state_manager.screen import Screen

class Game:
    def __init__(self, width: int, height: int):

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Reverse Turing Test — Are You Human?')

        self.clock = pygame.time.Clock()
        self.running = True

        self.current_screen: Optional[Screen] = None

    def run(self):
        while self.running:
            fr = self.clock.tick(60)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
               
                if self.current_screen:
                    self.current_screen.handle_event(event)
                    
            if self.current_screen:
                self.current_screen.update(fr)
                self.current_screen.draw()
            
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
