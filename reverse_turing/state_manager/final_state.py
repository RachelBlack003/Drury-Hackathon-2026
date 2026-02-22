from state_manager.screen import Screen
from game import Game
import pygame

class FinalEvaluation(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont(None, 50)
        self.small_font = pygame.font.SysFont(None, 36)

        self.result_text = self.evaluate_player()

    def evaluate_player(self):

        #TODO: Put the text in the correct spot 
        
        result_score = sum(self.game.results)
        
        if result_score == 20: 
            
            return "Some Text"
        elif result_score == 40:
            return "Some Text"
        elif result_score == 60:
            return "Some Text"
        elif result_score == 80:
            return "Some Text"
        elif result_score == 100:
            return "Some Text"
        

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.running = False

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((10, 10, 20))

        title = self.font.render("INTERROGATOR REPORT", True, (255,255,255))
        result = self.small_font.render(self.result_text, True, (200,200,200))

        self.screen.blit(title, (200, 200))
        self.screen.blit(result, (200, 300))