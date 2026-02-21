from state_manager.screen import Screen
import pygame

class FinalEvaluation(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont(None, 50)
        self.small_font = pygame.font.SysFont(None, 36)

        # Example evaluation logic
        self.result_text = self.evaluate_player() #TODO 

    def evaluate_player(self):
        # Placeholder logic
        # TODO: compute from stored score
        return "Evaluation Complete: HUMAN DETECTED"

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